# Generated by Django 4.1.3 on 2022-11-02 11:41

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500, verbose_name='Address')),
                ('postal_code', models.PositiveIntegerField(blank=True, null=True, verbose_name='Postal Code')),
                ('country', models.CharField(blank=True, max_length=120, verbose_name='Country')),
                ('federal_district', models.CharField(blank=True, max_length=20, verbose_name='Federal District')),
                ('region_type', models.CharField(blank=True, max_length=10, verbose_name='Region Type')),
                ('region', models.CharField(blank=True, max_length=120, verbose_name='Region')),
                ('area_type', models.CharField(blank=True, max_length=10, verbose_name='Area Type')),
                ('area', models.CharField(blank=True, max_length=120, verbose_name='Area')),
                ('city_type', models.CharField(blank=True, max_length=10, verbose_name='City Type')),
                ('city', models.CharField(blank=True, max_length=120, verbose_name='City')),
                ('settlement_type', models.CharField(blank=True, max_length=10, verbose_name='Settlement Type')),
                ('settlement', models.CharField(blank=True, max_length=120, verbose_name='Settlement')),
                ('kladr_id', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Kladr ID')),
                ('fias_id', models.CharField(blank=True, max_length=36, verbose_name='Fias ID')),
                ('fias_level', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Fias Level')),
                ('capital_marker', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Capital')),
                ('okato', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='OKATO')),
                ('oktmo', models.PositiveBigIntegerField(blank=True, null=True, verbose_name='OKTMO')),
                ('tax_office', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Tax Office')),
                ('timezone', models.CharField(blank=True, max_length=50, verbose_name='Timezone')),
                ('geo', django.contrib.gis.db.models.fields.PointField(srid=4326, unique=True, verbose_name='Geo')),
                ('population', models.CharField(blank=True, max_length=10, verbose_name='Population')),
                ('foundation_year', models.CharField(blank=True, max_length=20, verbose_name='Doundation Year')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Date of creating')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Date of editing')),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'ordering': ('address',),
            },
        ),
    ]
