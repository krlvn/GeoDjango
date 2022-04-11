import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('postal_code',
                 models.PositiveIntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=120)),
                ('federal_district',
                 models.CharField(blank=True, max_length=20)),
                ('region_type', models.CharField(blank=True, max_length=10)),
                ('region', models.CharField(blank=True, max_length=120)),
                ('area_type', models.CharField(blank=True, max_length=10)),
                ('area', models.CharField(blank=True, max_length=120)),
                ('city_type', models.CharField(blank=True, max_length=10)),
                ('city', models.CharField(blank=True, max_length=120)),
                ('settlement_type',
                 models.CharField(blank=True, max_length=10)),
                ('settlement', models.CharField(blank=True, max_length=120)),
                ('kladr_id',
                 models.PositiveBigIntegerField(blank=True, null=True)),
                ('fias_id', models.CharField(blank=True, max_length=36)),
                ('fias_level',
                 models.PositiveSmallIntegerField(blank=True, null=True)),
                ('capital_marker',
                 models.PositiveSmallIntegerField(blank=True, null=True)),
                ('okato',
                 models.PositiveBigIntegerField(blank=True, null=True)),
                ('oktmo',
                 models.PositiveBigIntegerField(blank=True, null=True)),
                ('tax_office',
                 models.PositiveSmallIntegerField(blank=True, null=True)),
                ('timezone', models.CharField(blank=True, max_length=50)),
                ('geo',
                 django.contrib.gis.db.models.fields.PointField(srid=4326,
                                                                unique=True)),
                ('population', models.CharField(blank=True, max_length=10)),
                ('foundation_year',
                 models.CharField(blank=True, max_length=20)),
            ],
            options={
                'db_table': 'cities',
            },
        ),
    ]
