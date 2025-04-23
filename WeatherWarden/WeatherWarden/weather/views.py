import requests
import os
from django.shortcuts import redirect, render
from django.http import JsonResponse

from weather.forms import CityForm
from weather.models import City


API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY', 'default_key')


def index(request):
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        "?q={}&units=metric&lang=ru&appid=" + API_KEY
    )

    error_message = ""
    message = ""
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data["name"]

            response = requests.get(url.format(new_city)).json()
            if response.get("cod") == 200:
                real_city_name = response["name"]

                if City.objects.filter(name__iexact=real_city_name).exists():
                    error_message = "Город уже есть"
                else:
                    City(name=real_city_name).save()
                    message = "Город успешно добавлен!"
            else:
                error_message = "Город не найден"

    form = CityForm()
    cities = City.objects.all()
    all_cities = []

    for city in cities:
        response = requests.get(url.format(city.name)).json()
        if response.get("cod") != 200:
            continue

        city_info = {
            "city": response["name"],
            "temp": int(response["main"]["temp"]),
            "feels_like": int(response["main"]["feels_like"]),
            "humidity": response["main"]["humidity"],
            "pressure": response["main"]["pressure"],
            "wind": response["wind"]["speed"],
            "description": response["weather"][0]["description"].capitalize(),
            "icon": response["weather"][0]["icon"],
        }
        all_cities.append(city_info)

    context = {
        "all_info": all_cities,
        "form": form,
        "error": error_message,
        "message": message,
    }
    return render(request, "weather/index.html", context)


def delete_city(request, city_name):
    City.objects.filter(name__iexact=city_name).delete()
    return redirect("home")


def weather_by_coords(request):
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")
    if not lat or not lon:
        return JsonResponse({"error": "Параметры lat и lon обязательны"}, status=400)

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}&units=metric&lang=ru&appid={API_KEY}"
    )
    resp = requests.get(url)
    data = resp.json()

    if data.get("cod") != 200:
        return JsonResponse(
            {"error": data.get("message", "Ошибка при получении погоды")},
            status=resp.status_code,
        )

    result = {
        "city": data.get("name", "—"),
        "temp": int(data["main"]["temp"]),
        "feels_like": int(data["main"]["feels_like"]),
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "wind": data["wind"]["speed"],
        "description": data["weather"][0]["description"].capitalize(),
        "icon": data["weather"][0]["icon"],
    }
    return JsonResponse(result)
