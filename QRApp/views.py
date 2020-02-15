from django.http import HttpResponse
from rest_framework import status, generics
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.utils import json
from QRApp import models
from QRApp.serializers import GtinSerializer


class GtinViewPagination(LimitOffsetPagination):
    """
    :argument
    """
    default_limit = 1
    max_limit = 1


def get_gtin():
    """
    :arg
    """
    output = []
    try:
        serializer = GtinSerializer(GtinView.queryset, many=True)
        results = output.append(serializer.data)
        return HttpResponse(results, indent=2, content_type='application/json', status=status.HTTP_200_OK)
    except TypeError:
        return HttpResponse(json.dumps({'Error': 'Exception'}), status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)


class GtinView(generics.ListAPIView):
    """
    :argument
    """
    queryset = models.Gtin.objects.all()
    serializer_class = GtinSerializer
    pagination_class = GtinViewPagination
