from rest_framework import serializers
from .models import ComprobanteDetalles


class DetallesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComprobanteDetalles
        fields = (
                  'id',
                  'comprobante_ruc',
                  'comprobante_numero',
                  'codigo_principal',
                  'descripcion',
                  'cantidad',
                  'precio',
                  'descuento',
                  'total')
        read_only_fields = ('id',)
