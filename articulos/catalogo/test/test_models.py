from django.test import TestCase
from articulos.catalogo.models import Producto1

class Producto1TestCase(TestCase):
    def setUp(self):
        Producto1.objects.create(id="977",nom="Tazón")

    def test_Producto1(self):
        producto = Producto1.objects.get(id="977")
        self.assertEqual(producto.nom, "Tazón")
    