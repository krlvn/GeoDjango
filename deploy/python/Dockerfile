FROM python:3.9
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# GDAL for GeoDjango
RUN apt-get update && apt-get install -y gdal-bin

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN python manage.py collectstatic --noinput

CMD python manage.py migrate && uwsgi deploy/python/uwsgi.ini
