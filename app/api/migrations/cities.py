import csv
from pathlib import Path

from django.contrib.gis.geos import Point
from django.db import migrations

DATA_FILENAME = 'city.csv'


def load_data(apps, schema_editor):
    city = apps.get_model('geoapi', 'City')
    csvfile = Path(__file__).parents[2] / DATA_FILENAME

    with open(str(csvfile), 'r', encoding='utf-8') as datafile:
        rows = csv.DictReader(datafile)
        for row in rows:
            fields = {
                'address': row['address'],
                'postal_code': int(row['postal_code']) if row[
                    'postal_code'] else None,
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
                'fias_level': int(row['fias_level']) if row[
                    'fias_level'] else None,
                'capital_marker': int(row['capital_marker']) if row[
                    'capital_marker'] else None,
                'okato': int(row['okato']) if row['okato'] else None,
                'oktmo': int(row['oktmo']) if row['oktmo'] else None,
                'tax_office': int(row['tax_office']) if row[
                    'tax_office'] else None,
                'timezone': row['timezone'],
                'geo': Point(float(row['geo_lon']),
                             float(row['geo_lat']),
                             srid=4326),
                'population': row['population'],
                'foundation_year': row['foundation_year']
            }

            city(**fields).save()


class Migration(migrations.Migration):
    dependencies = [
        ('geoapi', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]
