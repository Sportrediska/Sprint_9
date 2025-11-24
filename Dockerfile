# Создать образ на основе базового слоя,
# который содержит файлы ОС и интерпретатор Python 3.9.
# версия интерпритатора указывается проектная
FROM python:3.13-slim

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Копирование файлов проекта
COPY requirements.txt .
COPY . .

# Установка Python зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Установка Allure
RUN pip install allure-pytest

# Создание директорий для результатов
RUN mkdir -p /app/allure-results /app/reports

# Команда по умолчанию
CMD ["pytest", "--alluredir=/app/allure-results", "-v"]
