# Базовый образ с Python 3.12
FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    libpq-dev gcc chromium chromium-driver \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=web_d.settings \
    PATH="/usr/lib/chromium:${PATH}"

# Открытие порта
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]