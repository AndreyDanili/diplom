# использование исходного образа
FROM python:3.9

# задание рабочей директории
WORKDIR /src

# установка зависимостей
COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir -r /src/requirements.txt

# копирование файлов проекта
COPY . /src

EXPOSE 8000