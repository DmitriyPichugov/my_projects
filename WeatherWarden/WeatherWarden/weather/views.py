import requests
from django.shortcuts import render

from weather.forms import CityForm
from weather.models import City


def index(request):
    appid = 'e39ac3f2f5bae75c9559fa53d6a2af70'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    
    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()
    
    form = CityForm()
    cities = City.objects.all()
    all_cities = []
    
    for city in cities:
        response = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': response["main"]["temp"],
            'icon': response["weather"][0]["icon"]
        }
        
        all_cities.append(city_info)
    
    context = {'all_info': all_cities, 'form': form}
    
    return render(request, 'weather/index.html', context)
