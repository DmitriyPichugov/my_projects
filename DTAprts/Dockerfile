# Базовый образ с Python 3.12
FROM python:3.12-slim

# Установите рабочую директорию
WORKDIR /app

# Скопируйте все файлы из текущей директории (DTAprts)
COPY . .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Запустите Django-сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]