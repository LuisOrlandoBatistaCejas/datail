from django.db import models


class Comprobante(models.Model):
    ruc = models.TextField(db_column='Ruc')  # Field name made lowercase. This field type is a guess.
    numero = models.TextField(db_column='Numero')  # Field name made lowercase. This field type is a guess.
    identificacion = models.TextField(blank=True, null=True)  # This field type is a guess.
    fecha = models.TextField()
    direccion = models.TextField(blank=True, null=True)
    telefono = models.TextField(blank=True, null=True)  # This field type is a guess.
    email = models.TextField(blank=True, null=True)  # This field type is a guess.
    subtotal = models.TextField(blank=True, null=True)  # This field type is a guess.
    descuento = models.TextField(blank=True, null=True)  # This field type is a guess.
    iva = models.TextField(blank=True, null=True)  # This field type is a guess.
    total = models.TextField(blank=True, null=True)  # This field type is a guess.
    anulada = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        db_table = 'comprobante'
        unique_together = (('ruc', 'numero'),)

