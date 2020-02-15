from django.http import HttpResponse
from rest_framework import status, generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.utils import json

from .models import Gtin
from .serializers import GtinSerializer


class GtinViewPagination(LimitOffsetPagination):
    default_limit = 3
    # max_limit = 3


class GtinView(generics.ListAPIView):
    queryset = Gtin.objects.all()
    serializer_class = GtinSerializer
    pagination_class = GtinViewPagination

    def get_gtin(request):
        output = []
        try:
            serializer = GtinSerializer(GtinView.queryset, many=True)
            results = output.append(serializer.data)
            return HttpResponse(results, indent=2, content_type='application/json', status=status.HTTP_200_OK)
        except TypeError:
            return HttpResponse(json.dumps({'Error': 'Exception'}), status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
