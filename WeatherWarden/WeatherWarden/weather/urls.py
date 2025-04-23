from django.urls import path

from weather import views


urlpatterns = [
    path('', views.index, name='home'),
    path('delete/<str:city_name>/', views.delete_city, name='delete_city'),
    path("weather-by-coords/", views.weather_by_coords, name="weather_by_coords")
]
