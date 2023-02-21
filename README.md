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

Запустить терминал перейти в каталог с файлом /infra/docker-compose.yaml
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

Открыть в браузере

```
http://localhost/admin/
```

Остановить контейнеры после проверки работоспособности

```
docker-compose down -v
```

