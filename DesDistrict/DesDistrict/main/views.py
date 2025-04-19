from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'DesDistrict - Главная'
        context['content'] = 'Магазин мебели DesDistrict'
        return context
        

class AboutView(TemplateView):
    template_name = 'main/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'DesDistrict - О нас'
        context['content'] = 'О нас'
        context['text_on_page'] = 'Текст о том, почему этот магазин такой классныйи какой хороший товар'
        return context
    
# def index(request):
#     context = {
#         'title': 'DesDistrict - Главная',
#         'content': 'Магазин мебели DesDistrict'
#     }
    
#     return render(request, 'main/index.html', context)

# def about(request):
#     context = {
#         'title': 'DesDistrict - О нас',
#         'content': 'О нас',
#         'text_on_page': 'Текст о том, почему этот магазин такой классныйи какой хороший товар'
#     }
    
#     return render(request, 'main/about.html', context)
