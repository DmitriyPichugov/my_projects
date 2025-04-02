from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):
    context = {
        'title': 'DesDistrict - Главная',
        'content': 'Магазин мебели DesDistrict'
    }
    
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'DesDistrict - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о том, почему этот магазин такой классныйи какой хороший товар'
    }
    
    return render(request, 'main/about.html', context)
