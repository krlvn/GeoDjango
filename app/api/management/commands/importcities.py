from django.core.management.base import BaseCommand, CommandError
from api.models import City

import csv
from pathlib import Path

from django.contrib.gis.geos import Point
from django.db import migrations

from django.conf import settings


class Command(BaseCommand):
    help = 'Импорт списка городов из CSV файла.'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        csvfile = settings.BASE_DIR / f'''data/{options['filename']}.csv'''

        try:
            with open(str(csvfile), 'r', encoding='utf-8') as f:
                rows = csv.DictReader(f)
                for row in rows:
                    fields = {
                        'address': row['address'],
                        'postal_code': int(row['postal_code']) if row['postal_code'] else None,
                        'country': row['country'],
                        'federal_district': row['federal_district'],
                        'region_type': row['region_type'],
                        'region': row['region'],
                        'area_type': row['area_type'],
                        'area': row['area'],
                        'city_type': row['city_type'],
                        'city': row['city'],
                        'settlement_type': row['settlement_type'],
                        'settlement': row['settlement'],
                        'kladr_id': int(row['kladr_id']) if row['kladr_id'] else None,
                        'fias_id': row['fias_id'],
                        'fias_level': int(row['fias_level']) if row['fias_level'] else None,
                        'capital_marker': int(row['capital_marker']) if row['capital_marker'] else None,
                        'okato': int(row['okato']) if row['okato'] else None,
                        'oktmo': int(row['oktmo']) if row['oktmo'] else None,
                        'tax_office': int(row['tax_office']) if row['tax_office'] else None,
                        'timezone': row['timezone'],
                        'geo': Point(float(row['geo_lon']), float(row['geo_lat']), srid=4326),
                        'population': row['population'],
                        'foundation_year': row['foundation_year']
                    }
                    City(**fields).save()

            self.stdout.write(self.style.SUCCESS(f'''Список городов из файла "data/{options['filename']}.csv" успешно импортирован.'''))
        except Exception as e:
            raise CommandError(f'ERROR: {e}')
