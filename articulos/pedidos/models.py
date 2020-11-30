from django.db import models
import uuid
from catalogo.models import Producto1

class Pedidos(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    producto=models.ForeignKey(Producto1,on_delete=models.CASCADE)