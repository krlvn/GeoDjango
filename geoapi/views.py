from dadata import Dadata
from httpx import HTTPStatusError

from django.conf import settings
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import City
from .serializers import CitySerializer


class GetNeighbours(APIView):
    def get(self, request):

        address = request.query_params.get('address', default='Москва')
        radius = int(request.query_params.get('radius', default=50))

        # Определяет координаты по адресу через api Dadata
        try:
            dadata = Dadata(settings.DADATA['TOKEN'],
                            settings.DADATA['SECRET'])
            result = dadata.clean('address', address)
        except HTTPStatusError as err:
            raise PermissionDenied('Ошибка аутентификации.')

        user_city_fields = {
            'address': result['result'],
            'geo': Point(float(result['geo_lon']),
                         float(result['geo_lat']),
                         srid=4326)
        }
        user_city = City(**user_city_fields)

        user_city_serializer = CitySerializer(instance=user_city, many=False)

        neighbours = (City.objects
                      .filter(geo__distance_lte=(user_city.geo, D(km=radius)))
                      .order_by(Distance('geo', user_city.geo))
                      )

        neighbours_serializer = CitySerializer(instance=neighbours, many=True)

        response = {
            'user': user_city_serializer.data,
            'neighbours': neighbours_serializer.data
        }

        return Response(response)
