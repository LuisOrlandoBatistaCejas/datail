from rest_framework import serializers
from .models import Comprobante


class DetallesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comprobante
        fields = (
                  'id',
                  'ruc',
                  'numero',
                  'identificacion',
                  'fecha',
                  'direccion',
                  'telefono',
                  'email',
                  'subtotal',
                  'descuento',
                  'iva',
                  'anulada',
                  'total')
        read_only_field = ('id')
