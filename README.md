# Тестовое задание для Selleron

## Задание
Требуется создать простую API-систему, имитирующую деятельно службы доставки (за основу можно взять существующую службу 
доставки или придумать собственную).

## Запуск проекта
- Клонировать репозиторий
- Установить зависимости (команда в терминале: poetry install)
- Активировать виртуальное окружение (poetry shell) 
- Создать файл .env и заполнить его данными из файла .env.sample
- Создать базу данных в postresql
- Создать (python manage.py makemigrations) и применить миграции (python3 manage.py migrate)
- Загрузить данные в базу данных (python3 manage.py loaddata db.json)
- Запустить проект "python manage.py runserver"

## Документация к API
- создать заявку - POST/http://localhost:8000/create
- получить список заявок - GET/http://localhost:8000
- получить заявку - GET/http://localhost:8000/view/pk
- удалить заявку - DELETE/http://localhost:8000/delete/pk