from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from django.db.models import Q
from .serializers import DetallesSerializer

from .models import ComprobanteDetalles


# Create your tests here.
class ModelTestCase(TestCase):
    def setUp(self):
        self.comprobante_det = ComprobanteDetalles(
            comprobante_ruc='66666666',
            comprobante_numero='99999999',
            codigo_principal='TESTCODE',
            descripcion='TEST DESCRIPTION',
            cantidad='1',
            precio='8.00000',
            descuento='0.00000',
            total='8.00000'
        )
        self.client = APIClient()
        self.response = self.client.post(
            'rest/details',
            {
            'comprobante_ruc':'66666666',
            'comprobante_numero':'99999999',
            'codigo_principal':'TESTCODE',
            'descripcion':'TEST DESCRIPTION',
            'cantidad':'1',
            'precio':'8.00000',
            'descuento':'0.00000',
            'total':'8.00000'
            },
            format="json")

    def test_create(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_read(self):
        response = self.client.get(
            'rest/details/{}'.format(self.comprobante_det.id),format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.comprobante_det)

    def test_update(self):
        updated = self.comprobante_det
        updated.cantidad = 2
        res = self.client.put(
            'rest/details',
            updated,
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

