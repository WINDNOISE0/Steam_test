FROM python:3.11-slim

WORKDIR /tests

RUN apt-get update && apt-get install -y \
    curl unzip chromium-driver chromium

RUN pip install --upgrade pip

COPY requirements.txt .
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["pytest", "-v", "--tb=short", "--color=yes", "--durations=5"]