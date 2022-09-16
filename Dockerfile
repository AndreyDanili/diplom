# использование исходного образа
FROM python:3.9-alpine

# задание рабочей директории
WORKDIR /src

# установка psycopg2
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# установка зависимостей
COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir -r /src/requirements.txt


# копирование файлов проекта
COPY . /src

EXPOSE 8000