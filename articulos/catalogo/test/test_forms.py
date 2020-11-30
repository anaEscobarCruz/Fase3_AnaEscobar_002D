from django.test import TestCase
from articulos.catalogo.models import Producto1
from articulos.catalogo.forms import ProdForms

class ProductoFormsTest(TestCase):
    def test_valid_form(self):
        prod = Producto1.objects.create(nom = "Espejo aniverñe" , id = "587")
        data = {'nom': prod.nom,'id': prod.id,}
        form = ProdForms(data)
        self.assertTrue(form)

    def test_invalid_form(self):
        prod = Producto1.objects.create(nom = "" , id= "587")
        data = {'nom': prod.nom,'id': prod.id}
        form = ProdForms(data)
        self.assertTrue(form)
