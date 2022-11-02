# What is this?
This project demonstrates the capabilities of GeoDgango in conjunction with DRF and a third party API

# How it works?
The user enters an address and radius into the form. 
After that, the app get coordinates from the geocoding API (dadata.ru) and all nearest addresses are shown on the map.

## Stack:
- Python 3.10
- Django 4.1.3
- Django Rest Framework
- PostgreSQL 14 (PostGis, GDAL)
- OpenLayers (OpenStreetMap), JQuery
- API Dadata

## Installation without Docker:
1. Get `token` and `secret` from `dadata.ru`
2. Copy `example.env` to `.env`
3. Install PostgreSQL 14 with PostGis and GDAL
4. Run `pip install -r requirements.txt`
5. Run `python manage.py migrate`
6. Run `python manage.py importcities cities`
7. Done!

## Installation with Docker:
1. Get `token` and `secret` from `dadata.ru`
2. Copy `example.env` to `.env`
3. Run `docker-compose build`
4. Run `docker-compose up -d`
4. Run `docker-compose run app python manage.py importcities cities`
5. Done!
