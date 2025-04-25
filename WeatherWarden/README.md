# WeatherWarden

WeatherWarden — это «умный» веб-приложение на Django + Channels + FastAPI, позволяющее:

- Добавлять любимые города и получать **текущую погоду** (температура, ощущается как, влажность, ветер, описание, иконка) через OpenWeatherMap API на русском языке.  
- Мгновенно обновлять данные **WebSocket**-соединением (Django Channels + Daphne).  
- **Кэшировать** запросы в Redis, чтобы снижать нагрузку на API.  
- Получать погоду для **текущей геолокации** по кнопке «Моя локация» (HTML5 Geolocation + отдельный endpoint).  
- **Автодополнять** названия городов при вводе (OpenWeather Geo API + `<datalist>`).  
- Переключаться между **светлой и тёмной** темами с анимацией и запоминанием выбора в `localStorage`.  
- Красиво отображать данные в формате **Bootstrap 5 cards** с иконками Font Awesome, неоновой обводкой и адаптивным дизайном.

## Структура проекта

```
WeatherWarden/
├── WeatherWarden/            # Django-конфиг (settings, главный urls.py, api.py для Channels+FastAPI)
├── weather/                  # Приложение Django
│   ├── migrations/
│   ├── templates/weather/    # HTML-шаблоны (index.html)
│   ├── static/               # CSS, JS, изображения (favicon)
│   ├── views.py              # Представления (index, delete_city, weather_by_coords)
│   ├── models.py             # Модель City
│   └── forms.py              # Форма CityForm
├── manage.py
└── requirements.txt          # Все зависимости проекта
```

## Установка и запуск

1. **Клонировать репозиторий**  
   ```bash
   git clone https://github.com/DmitriyPichugov/my_projects.git
   cd my_projects/WeatherWarden
   ```

2. **Создать и активировать виртуальное окружение**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Установить зависимости**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Настроить Redis**  
   - Установить и запустить `redis-server` локально на порту 6379.  
   - Если нужно, поменять URL Redis в `api.py`.

5. **Выполнить миграции и собрать статику**  
   ```bash
   python manage.py migrate
   python manage.py collectstatic
   ```

6. **Запустить Daphne (ASGI-сервер)**  
   ```bash
   daphne -b 127.0.0.1 -p 8000 WeatherWarden.api:app
   ```

7. **Открыть в браузере**  
   ```
   http://localhost:8000/
   ```

## Конфигурация

- **API_KEY** для OpenWeatherMap хранится в `views.py` и `api.py` (константа `API_KEY`).  
- **STATICFILES_DIRS** и **STATIC_URL**: проверьте в `settings.py`, чтобы статика (`favicon.ico` и др.) раздавалась корректно.  

## Основные эндпоинты

- `/` — главная страница с формой и списком городов.  
- `/delete/<city_name>/` — удаление города.  
- `/weather-by-coords/?lat=<lat>&lon=<lon>` — возвращает JSON текущей погоды по координатам.  
- `ws://<host>/ws/weather/<city>/` — WebSocket для периодических обновлений (раз в минуту).

## Frontend-фичи

- **Карточки** Bootstrap с анимацией hover и неоновой обводкой в тёмной теме.  
- **Переключатель темы**: плавный bounce-эффект для иконки луны/солнца.  
- **Autocompletion** поля города через OpenWeather Geo API и `<datalist>`.  
- **Кнопка геолокации**: добавляет отдельную карточку под формой, обновляемую по WebSocket и доступную к ручному закрытию/автоудалению.

## Contributing

1. Форкаем репозиторий и создаём новую ветку.  
2. Вносим правки, добавляем тесты.  
3. Делаем PR в `main` и ждём ревью.

## License

Проект распространяется под лицензией MIT.  

---

### Использованные источники (поисковик)

1. Verdy Evantyo, “Make a Weather Application using Django” — пример простого Django-приложения для погоды citeturn2search0  
2. LaurentiusVAdela, “Weather-Forecast-Web-App-with-Django-Framework” (GitHub) — структура типового weather-приложения citeturn2search1  
3. Reddit, r/Fantasy обсуждение “Weather Warden series” — не относится к коду проекта citeturn2search2  
4. eBay и Goodreads — не имеют отношения к проекту citeturn2search3turn2search9  
5. Elspeth Cooper Blog — фэнтези-литература, не релевантно citeturn2search5turn2search7  

_Эти ресурсы не содержат документации по вашему коду, поэтому было принято решение написать `README.md` вручную на основе анализа структуры и обсуждения в чате._
