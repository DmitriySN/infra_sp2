# Учебный проект контейнер Docker

### Описание
REST API YamDB - база отзывов пользователей о фильмах, книгах и музыке.

### Технологии
Python 3.7
Django 2.2.16
Rest API
Docker
Docker-compose

### Запуск проекта в dev-режиме

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/DmitriySN/infra_sp2
```

Войти в рабочий каталог:

```
cd infra_sp2
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate - Для linux
source env/Scripts/activate - Для windows
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r api_yamdb/requirements.txt
```

Выполнить миграции:

В settings.py изменить настройки на сервер баз данных SQLite, по умолчанию установлено на PostgreSQL

```
cd api_yamdb
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Запуск проекта в контейнерах docker-compose

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/DmitriySN/infra_sp2
```

Запустить терминал перейти в каталог с файлом /infra_sp2/infra/docker-compose.yaml
пересобрать контейнеры и запустить

```
docker-compose up -d --build
```

Выполнить миграции, создание суперпользователя и сгененировать статику

```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

Создать переменные окружения в каталоге infra_sp2/infra/ создайте файл .env

```
SECRET_KEY='12345' # укажите секретняй ключ (установите свой)
# переменные для сервера баз данных
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

Открыть в браузере

```
http://localhost/admin/
```

Создание дампа bd выполнялось в каталоге infra_sp2/infra/ командой

```
docker-compose exec web python manage.py dumpdata > fixtures.json
```

Для восстановления Необходимо узнать id контейнера с django и залить базу

```
docker container ls -a
docker cp fixtures.json <CONTAINER ID>:/app
# Предварительно настроено имя в docker-compose можно указать или сразу так
docker cp fixtures.json api_yamdb_django:/app
docker-compose exec web python manage.py loaddata fixtures.json

```

Можно удалить дамп базы из контейнера

```
docker exec -it <CONTAINER ID> bash
# или
docker exec -it api_yamdb_django bash
rm fixtures.json
exit
```

Остановить контейнеры после проверки работоспособности

```
docker-compose down -v
```

