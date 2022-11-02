from django.contrib.gis.db import models


class City(models.Model):
    address = models.CharField(max_length=500, verbose_name='Address')
    postal_code = models.PositiveIntegerField(blank=True, null=True, verbose_name='Postal Code')
    country = models.CharField(max_length=120, blank=True, verbose_name='Country')
    federal_district = models.CharField(max_length=20, blank=True, verbose_name='Federal District')
    region_type = models.CharField(max_length=10, blank=True, verbose_name='Region Type')
    region = models.CharField(max_length=120, blank=True, verbose_name='Region')
    area_type = models.CharField(max_length=10, blank=True, verbose_name='Area Type')
    area = models.CharField(max_length=120, blank=True, verbose_name='Area')
    city_type = models.CharField(max_length=10, blank=True, verbose_name='City Type')
    city = models.CharField(max_length=120, blank=True, verbose_name='City')
    settlement_type = models.CharField(max_length=10, blank=True, verbose_name='Settlement Type')
    settlement = models.CharField(max_length=120, blank=True, verbose_name='Settlement')
    kladr_id = models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Kladr ID')
    fias_id = models.CharField(max_length=36, blank=True, verbose_name='Fias ID')
    fias_level = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Fias Level')
    capital_marker = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Capital')
    okato = models.PositiveBigIntegerField(blank=True, null=True, verbose_name='OKATO')
    oktmo = models.PositiveBigIntegerField(blank=True, null=True, verbose_name='OKTMO')
    tax_office = models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Tax Office')
    timezone = models.CharField(max_length=50, blank=True, verbose_name='Timezone')
    geo = models.PointField(unique=True, verbose_name='Geo')
    population = models.CharField(max_length=10, blank=True, verbose_name='Population')
    foundation_year = models.CharField(max_length=20, blank=True, verbose_name='Doundation Year')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Date of creating', editable=False)
    update_date = models.DateTimeField(auto_now=True, verbose_name='Date of editing', editable=False)
    deleted = models.BooleanField(default=False)

    class Meta():
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ('address',)

    def __str__(self):
        return f'{self.pk} {self.address}'

    def delete(self, *args):
        self.deleted = True
        self.save()
