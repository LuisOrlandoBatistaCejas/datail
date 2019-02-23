# coding=utf-8
from functools import reduce

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from .serializers import DetallesSerializer
from .models import ComprobanteDetalles
from django.db.models import Q
import operator

class DetailsViewset(viewsets.ModelViewSet):
    serializer_class = DetallesSerializer
    queryset = ComprobanteDetalles.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['id']

    def get_queryset(self):
        if(self.request.query_params):
            filters = []
            if(self.request.query_params.get("id", None)):
                filters.append(Q(id=self.request.query_params.get("id", None)))
            if (self.request.query_params.get("ruc", None)):
                filters.append(Q(comprobante_ruc=self.request.query_params.get("ruc", None)))
            if (self.request.query_params.get("numero", None)):
                filters.append(Q(comprobante_numero=self.request.query_params.get("numero", None)))

            return ComprobanteDetalles.objects.filter(reduce(operator.and_, filters))
        else:
            return self.queryset
