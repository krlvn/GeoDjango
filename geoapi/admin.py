from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import City


@admin.register(City)
class CityAdmin(OSMGeoAdmin):
    list_display = ('address',
                    'postal_code',
                    'country',
                    'federal_district',
                    'region_type',
                    'region',
                    'area_type',
                    'area',
                    'city_type',
                    'city',
                    'settlement_type',
                    'settlement',
                    'kladr_id',
                    'fias_id',
                    'fias_level',
                    'capital_marker',
                    'okato',
                    'oktmo',
                    'tax_office',
                    'timezone',
                    'geo',
                    'population',
                    'foundation_year'
                    )

