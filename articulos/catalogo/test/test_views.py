from django.test import TestCase, Client
from django.test import client
from django.urls import reverse
from catalogo.models import Producto, Stock
import json


class ProductoTestCase(TestCase):

    def test_project_list_GET(self):
        client = Client()

        response = client.get(reverse('list'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'budget/project-list')