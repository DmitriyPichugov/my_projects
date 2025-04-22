import requests
from django.shortcuts import redirect, render

from weather.forms import CityForm
from weather.models import City


def index(request):
    appid = "e39ac3f2f5bae75c9559fa53d6a2af70"
    url = (
        "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="
        + appid
    )

    error_message = ""
    message = ""
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            new_city = form.cleaned_data["name"]

            # Проверка на наличие такого города в базе
            if City.objects.filter(name__iexact=new_city).exists():
                error_message = "Город уже есть"
            else:
                response = requests.get(url.format(new_city)).json()
                if response.get("cod") == 200:
                    form.save()
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

        # city_info = {
        #     "city": city.name,
        #     "temp": int(response["main"]["temp"]),
        #     "icon": response["weather"][0]["icon"],
        # }
        city_info = {
            "city": city.name,
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
