# myGeoApp

Пользователь вводит в форму адрес и радиус поиска в километрах. Через API геокодирования сервиса Dadata определяются координаты, и из базы данных выбираются все адреса находящиеся в окружности указанного пользователем адреса.

Стек технологий:
- Python 3.9 
- Django 4 (Django Rest Framework)
- PostgreSQL 14 (PostGis, GDAL)
- OpenLayers (OpenStreetMap), JQuery
- API Dadata


Файл `example.env` переименовать в `.env` и указать в нём API-ключ и секретный ключ сервиса Dadata.

Развернуть контейнеры: `docker-compose up`
