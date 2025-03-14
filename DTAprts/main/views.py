import plotly.express as px
import pandas as pd
from django.shortcuts import render
from .models import Apartment


def index(request):
    return render(request, 'main/index.html')

def about(request):
    apartments = Apartment.objects.all().values()
    df = pd.DataFrame(apartments)

    if df.empty or 'price' not in df.columns:
        context = {'error': 'Нет данных для отображения графиков'}
        return render(request, 'main/about.html', context)

    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['square'] = pd.to_numeric(df['square'], errors='coerce')
    df['commission'] = pd.to_numeric(df['commission'], errors='coerce')
    df['rooms'] = pd.to_numeric(df['rooms'], errors='coerce')
    
    price_min = float(request.GET.get('price_min', 0) or 0)
    price_max = request.GET.get('price_max')
    price_max = float(price_max) if price_max else float('inf')

    rooms_min = float(request.GET.get('rooms_min', 0) or 0)
    rooms_max = request.GET.get('rooms_max')
    rooms_max = float(rooms_max) if rooms_max else float('inf')

    square_min = float(request.GET.get('square_min', 0) or 0)
    square_max = request.GET.get('square_max')
    square_max = float(square_max) if square_max else float('inf')

    commission_filter = request.GET.get('commission_filter', 'all')
    
    filtered_df = df[
        (df['price'].between(price_min, price_max)) &
        (df['rooms'].between(rooms_min, rooms_max)) &
        (df['square'].between(square_min, square_max))
    ]
    
    if commission_filter == '<50':
        filtered_df = filtered_df[filtered_df['commission'] < 50]
    elif commission_filter == '>50':
        filtered_df = filtered_df[filtered_df['commission'] >= 50]

    if filtered_df.empty:
        context = {'error': 'Нет данных, соответствующих выбранным фильтрам'}
        return render(request, 'main/about.html', context)

    price_fig = px.histogram(filtered_df, x='price', title='Распределение цен')
    avg_price_by_district = filtered_df.groupby('district')['price'].mean().reset_index()
    avg_price_fig = px.bar(avg_price_by_district, x='district', y='price', title='Средняя цена по районам')
    scatter_fig = px.scatter(filtered_df, x='square', y='price', title='Цена vs Площадь')

    price_analysis = (
        f"График показывает распределение цен на квартиры. Средняя цена: {filtered_df['price'].mean():.0f} руб., "
        f"медиана: {filtered_df['price'].median():.0f} руб. Диапазон: {filtered_df['price'].min():.0f}–{filtered_df['price'].max():.0f} руб."
    )
    district_analysis = (
        f"Средняя цена по районам варьируется. Самый дорогой: {avg_price_by_district.loc[avg_price_by_district['price'].idxmax(), 'district']} "
        f"({avg_price_by_district['price'].max():.0f} руб.), самый дешёвый: {avg_price_by_district.loc[avg_price_by_district['price'].idxmin(), 'district']} "
        f"({avg_price_by_district['price'].min():.0f} руб.)."
    )
    scatter_analysis = (
        f"Диаграмма показывает зависимость цены от площади. Медиана площади: {filtered_df['square'].median():.0f} м². "
        f"С увеличением площади цена в целом растёт."
    )

    filtered_apartments = Apartment.objects.filter(
        price__gte=price_min, price__lte=price_max,
        rooms__gte=rooms_min, rooms__lte=rooms_max,
        square__gte=square_min, square__lte=square_max
    )
    
    if commission_filter == '<50':
        filtered_apartments = filtered_apartments.filter(commission__lt=50)
    elif commission_filter == '>50':
        filtered_apartments = filtered_apartments.filter(commission__gte=50)
    
    context = {
        'price_fig': price_fig.to_html(full_html=False),
        'avg_price_fig': avg_price_fig.to_html(full_html=False),
        'scatter_fig': scatter_fig.to_html(full_html=False),
        'price_analysis': price_analysis,
        'district_analysis': district_analysis,
        'scatter_analysis': scatter_analysis,
        'filtered_apartments': filtered_apartments,
        'median_square': filtered_df['square'].median(),
    }

    return render(request, 'main/about.html', context)