import os
import json
import asyncio
import httpx
from fastapi import FastAPI
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.asgi import get_asgi_application
from django.urls import re_path
import redis.asyncio as aioredis


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WeatherWarden.settings")
API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY', 'default_key')

redis = aioredis.from_url(
    "redis://localhost:6379/0", encoding="utf-8", decode_responses=True
)

fastapi_app = FastAPI()


class WeatherWebSocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        asyncio.create_task(self.send_weather_updates())

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data=None, bytes_data=None):
        pass

    async def send_weather_updates(self):
        city = self.scope["url_route"]["kwargs"]["city"]
        cache_key = f"weather:{city}"
        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            "?q={}&units=metric&lang=ru&appid=" + API_KEY
        )

        async with httpx.AsyncClient() as client:
            while True:
                cached = await redis.get(cache_key)
                if cached:
                    print(f"[REDIS] Using cached data for {city}")
                    weather_data = json.loads(cached)
                else:
                    print(f"[API] Fetching fresh data for {city}")
                    response = await client.get(url.format(city))
                    weather_data = response.json()
                    if weather_data.get("cod") == 200:
                        await redis.set(cache_key, json.dumps(weather_data), ex=60)
                    else:
                        await self.send(
                            text_data=json.dumps({"error": "Город не найден"})
                        )
                        break

                await self.send(
                    text_data=json.dumps(
                        {
                            "city": city,
                            "country": weather_data["sys"]["country"],
                            "temp": int(weather_data["main"]["temp"]),
                            "feels_like": weather_data["main"]["feels_like"],
                            "humidity": weather_data["main"]["humidity"],
                            "pressure": weather_data["main"]["pressure"],
                            "wind_speed": weather_data["wind"]["speed"],
                            "wind_deg": weather_data["wind"].get("deg", 0),
                            "clouds": weather_data["clouds"]["all"],
                            "description": weather_data["weather"][0]["description"],
                            "icon": weather_data["weather"][0]["icon"],
                            "timestamp": weather_data["dt"],
                        }
                    )
                )

                await asyncio.sleep(60)


django_app = get_asgi_application()

websocket_routes = [
    re_path(r"^ws/weather/(?P<city>[^/]+)/?$", WeatherWebSocketConsumer.as_asgi()),
]

app = ProtocolTypeRouter(
    {
        "http": django_app,
        "websocket": URLRouter(websocket_routes),
    }
)
