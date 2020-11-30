from django.contrib import admin

from . models import Orden, OrderLine
admin.site.register(Orden)
admin.site.register(OrderLine)
