from django.test import TestCase
from models import Producto, Stock

class ProdTestCase(TestCase):
    def setUp(self):
        p1=Producto.objects.create(nom="Tazón")
        p2=Producto.objects.create(nom="Llavero")
        Stock.objects.create(id="T3", nom=p1, summary="Tazón mágico")
        Stock.objects.create(id="L2", nom=p2, summary="Llavero corazón")

def test_Prod_data(self):
    produ1 = Stock.objects.get(id="T3")
    self.assertEqual(produ1.Producto.nom, "Tazón")
    