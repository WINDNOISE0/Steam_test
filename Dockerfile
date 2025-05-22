FROM python:3.11-slim

# Установка зависимостей
RUN apt-get update && apt-get install -y \
    curl unzip chromium-driver chromium

# Установка selenium и seleniumbase
RUN pip install --upgrade pip
RUN pip install selenium seleniumbase

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /tests
COPY . .

CMD ["pytest"]
