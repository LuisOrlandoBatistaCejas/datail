from django.db import models
from comprobante.models import Comprobante

class ComprobanteDetalles(models.Model):
    id = models.TextField(db_column='Id', unique=True, primary_key=True, auto_created=True)  # Field name made lowercase. This field type is a guess.
    comprobante_ruc = models.ForeignKey(Comprobante, related_name='Ruc', on_delete=models.CASCADE,db_column='comprobante_Ruc')  # Field name made lowercase. This field type is a guess.
    comprobante_numero = models.ForeignKey(Comprobante,related_name='Numero',on_delete=models.CASCADE, db_column='comprobante_Numero')  # Field name made lowercase. This field type is a guess.
    codigo_principal = models.TextField(blank=True, null=True)  # This field type is a guess.
    descripcion = models.TextField(blank=True, null=True)  # This field type is a guess.
    cantidad = models.TextField()  # This field type is a guess.
    precio = models.TextField(blank=True, null=True)  # This field type is a guess.
    descuento = models.TextField(blank=True, null=True)  # This field type is a guess.
    total = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        db_table = 'comprobante_detalles'