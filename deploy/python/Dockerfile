FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# GDAL for GeoDjango
RUN apt-get update && apt-get install -y gdal-bin

COPY app/ .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Gunicorn
RUN pip install --no-cache-dir Gunicorn
EXPOSE 8000
CMD python -m gunicorn config.wsgi:application --bind 0.0.0.0:8000
