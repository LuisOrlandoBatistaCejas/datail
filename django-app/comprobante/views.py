from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from .serializers import DetallesSerializer
from .models import Comprobante
from comprobante_detalles.models import ComprobanteDetalles
from django.db.models import Q

class ComprobanteViewset(viewsets.ModelViewSet):
    serializer_class = DetallesSerializer
    queryset = Comprobante.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['id']

    def get_queryset(self):
        if(self.request.query_params):
            if(self.request.query_params.get("id", None)):
                return Comprobante.objects.filter(Q(id=self.request.query_params.get("id", None)))
        else:
            return self.queryset


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        for detail in ComprobanteDetalles.objects.filter(comprobante_ruc=instance.ruc, comprobante_numero=instance.numero):
            detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
