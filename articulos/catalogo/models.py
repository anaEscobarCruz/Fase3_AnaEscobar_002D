from django.db import models


# Create your models here.
from django.db import models
from django.urls import reverse
import uuid

class Producto1(models.Model):
    id=models.IntegerField(primary_key=True, help_text="Código del producto")
    nom=models.CharField(max_length=200)
    prec=models.IntegerField(help_text="Precio producto")
    cant=models.IntegerField()
    img=models.ImageField(upload_to='images_2/', null=True, blank=True)
    def __str__(self):
        return f' {self.id} ({self.nom})'

    def get_absolute_url(self):
        return reverse('prod-detail', args=[int(self.id)])