from django.contrib import admin

# Register your models here.
from . models import Producto, Stock
admin.site.register(Producto)
admin.site.register(Stock)