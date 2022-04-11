from rest_framework_gis.serializers import GeoFeatureModelSerializer
from .models import City


class CitySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = City
        geo_field = 'geo'
        fields = ('address',)
