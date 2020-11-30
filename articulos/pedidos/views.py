from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Orden, OrderLine
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#Mostrar lista de pedidios del usuario
class PedidoList(ListView):
    model = Orden
    ordering = ["-id"]
    template_name = "ordenes/listado.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

#Muestra el detalle de un pedido
class PedidoDetail(DetailView):
    model = Orden
    template_name = "ordenes/detalle.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

class PedidoCreate(CreateView):
    model = Orden
    fields = ['nom', 'cant']

class PedidoDelete(DeleteView):
    model = Orden
    success_url = reverse_lazy('confecciones')