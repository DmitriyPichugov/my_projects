from django.shortcuts import render


def login(request):
    context = {
        'title': 'DesDistrict - Авторизация'
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'DesDistrict - Регистрация'
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        'title': 'DesDistrict - Кабинет'
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    ...
