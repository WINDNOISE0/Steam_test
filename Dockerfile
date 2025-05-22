FROM byrnedo/alpine-curl:0.1.8 as curl
RUN curl https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh > wait-for-it.sh

FROM python:3.9.0-alpine

# Копируем requirements.txt отдельно
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем остальной проект
COPY Steam_test/ /selenium_tests/
WORKDIR /selenium_tests/

# waiter
COPY --from=curl wait-for-it.sh wait-for-it.sh
RUN chmod +x wait-for-it.sh
RUN apk add bash
