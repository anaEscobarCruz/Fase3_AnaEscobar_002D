from django.db import models
import uuid
from django.db.models import F, Sum, IntegerField , CharField
from django.db.models.fields import DateTimeField
from catalogo.models import Producto1
from django.contrib.auth import get_user_model
User = get_user_model()

class Orden(models.Model):
    id=models.CharField(primary_key=True, max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto1, on_delete=models.CASCADE)
    completado = models.BooleanField(default=False)
    creado_el = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return self.orderline_set.aggregate(
            total=Sum(F("producto1_prec") * F("cant"), output_field=IntegerField())
        )["total"] or IntegerField(0)

    def str(self):
        return self.id

    class Meta:
        db_table = 'ordenes'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']

class OrderLine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto1, on_delete=models.CASCADE)
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    cant = models.IntegerField(default=1)
    creado_el = models.DateTimeField(auto_now_add=True)

    def str__(self):
        return f'{str(self.cantidad)} de {self.producto.NombreProd}'

    class Meta:
        db_table = 'orderlines'
        verbose_name = 'Línea de pedido'
        verbose_name_plural = 'Líneas de pedidos'
        ordering = ['id']
