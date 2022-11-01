from django.contrib.gis.db import models


class City(models.Model):
    address = models.CharField(max_length=500)
    postal_code = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=120, blank=True)
    federal_district = models.CharField(max_length=20, blank=True)
    region_type = models.CharField(max_length=10, blank=True)
    region = models.CharField(max_length=120, blank=True)
    area_type = models.CharField(max_length=10, blank=True)
    area = models.CharField(max_length=120, blank=True)
    city_type = models.CharField(max_length=10, blank=True)
    city = models.CharField(max_length=120, blank=True)
    settlement_type = models.CharField(max_length=10, blank=True)
    settlement = models.CharField(max_length=120, blank=True)
    kladr_id = models.PositiveBigIntegerField(blank=True, null=True)
    fias_id = models.CharField(max_length=36, blank=True)
    fias_level = models.PositiveSmallIntegerField(blank=True, null=True)
    capital_marker = models.PositiveSmallIntegerField(blank=True, null=True)
    okato = models.PositiveBigIntegerField(blank=True, null=True)
    oktmo = models.PositiveBigIntegerField(blank=True, null=True)
    tax_office = models.PositiveSmallIntegerField(blank=True, null=True)
    timezone = models.CharField(max_length=50, blank=True)
    geo = models.PointField(unique=True)
    population = models.CharField(max_length=10, blank=True)
    foundation_year = models.CharField(max_length=20, blank=True)

    class Meta:
        db_table = 'cities'
