# WeatherWarden - Веб приложение для отслеживания погоды

WeatherWarden - умное веб-приложение для отслеживания погоды в ваших любимых городах (OpenWeatherMap API), с живыми обновлениями по WebSocket (реализованным через FastAPI), кэшированием в Redis и автодополнением городов на русском с хранением в базе данных MySQL.

---
## Функциональность

- Добавлять города и смотреть **текущую погоду** (температура, «ощущается как», влажность, ветер, описание, иконки) через OpenWeatherMap API.  
- Получать **автоматические обновления** через WebSocket (Django Channels + Daphne + FastAPI).  
- **Кэшировать** ответы в Redis (TTL 60 с) для экономии вызовов API.  
- Определять погоду по **геолокации** пользователя и показывать отдельную карточку с возможностью ручного или автоматического закрытия.  
- Использовать **автодополнение** названий городов на русском с помощью Geo-API OpenWeatherMap.  
- Переключаться между **светлой и тёмной** темами с плавной анимацией, настроенной сс использованием JavaScript.

Интерфейс построен на Bootstrap 5 и Font Awesome, адаптивен под мобильные устройства.

---

## Технологии

- `Бэкенд`: **Django 5.0.6**, **Python 3.13.2**, **Channels 4.x** + **Daphne** (WebSocket), **FastAPI** (ASGI-роутинг внутри `api.py`), **httpx**, **redis-asyncio** (асинхронные запросы к API и Redis), **OpenWeatherMap API** (`lang=ru`)
- `База данных`: **MySQL**, **Redis** (кэширование)
- `Фронтенд`: **HTML**, **Bootstrap 5**, **Font Awesome 6** (CSS/JS)  
- `Развертывание`: **Docker**, **Docker Compose**  
- Список всех Python-пакетов в `requirements.txt`

---

## Структура проекта

```text
WeatherWarden/
├── api.py                 # ASGI-конфиг: ProtocolTypeRouter + FastAPI + Channels
├── Dockerfile             # Сборка контейнера веб-приложения
├── docker-compose.yml     # Сервис web (+ Daphne), redis, (по желанию) nginx
├── .env                   # API ключи и прочие переменные окружения
├── manage.py              # Утилита Django
├── requirements.txt       # Зависимости Python
├── db.sqlite3             # SQLite-БД (для dev)
├── dump.rdb               # Дамп Redis (если нужен)
├── static/                # Статические файлы
│   └── images/
│       └── favicon.ico
├── weather/               # Приложение Django
│   ├── migrations/        # Миграции модели City
│   ├── templates/weather/ # Шаблоны (index.html)
│   ├── static/weather/    # CSS/JS (если есть)
│   ├── views.py           # index, delete_city, weather_by_coords
│   ├── models.py          # City (name)
│   ├── forms.py           # CityForm
│   └── urls.py            # Локальная маршрутизация
└── WeatherWarden/         # Конфиг Django-проекта
    ├── __init__.py
    ├── settings.py        # Настройки (DATABASES, STATIC, CHANNEL_LAYERS)
    ├── urls.py            # Главный urls.py (+static в DEBUG)
    └── asgi.py            # Точка входа ASGI для Django
```

---

## Установка и запуск через Docker

1. **Склонировать** репозиторий:
   ```bash
   git clone https://github.com/DmitriyPichugov/my_projects.git
   cd my_projects/WeatherWarden
   ```

2. **Создать `.env`** в корне (пример):
   ```ini
   DEBUG=True
   SECRET_KEY=ваш_секретный_ключ
   OPENWEATHER_API_KEY=e39ac3f2f5bae75c9559fa53d6a2af70
   ```

3. **Собрать и запустить** контейнеры:
   ```bash
   docker compose up --build -d
   ```

4. **Применить миграции**:
   ```bash
   docker compose exec web python manage.py migrate
   ```

5. **(Опционально)** Создать суперпользователя:
   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

6. **Открыть** в браузере:
   ```
   http://localhost:8000/
   ```

---

## Локальный запуск (без Docker)

1. Создать и активировать виртуальное окружение:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Установить зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Запустить Redis локально:
   ```bash
   redis-server
   ```

4. Прописать в `.env` ключ API и другие настройки.

5. Выполнить миграции и собрать статические файлы:
   ```bash
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

6. Запустить Daphne:
   ```bash
   daphne -b 0.0.0.0 -p 8000 api:app
   ```

---
