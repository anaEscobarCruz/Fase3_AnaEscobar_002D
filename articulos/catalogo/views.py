from django.shortcuts import render
from . models import Producto
from django.views import generic

# Create your views here.
def Index(request) :
    produ = Producto.objects.all().count()

    return render(
        request,
        'index.html',
        context={'produ': produ},
    )
def confecciones(request) :

    return render(
        request,
        'confecciones.html',
    )
def estampados(request) :

    return render(
        request,
        'estampados.html',
    )
#Formulario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto

class ProdCreate(CreateView):
    model = Producto
    fields = ['nom', 'cant']

class ProdUpdate(UpdateView):
    model = Producto
    fields = ['nom', 'cant']

class ProdDelete(DeleteView):
    model = Producto
    sucess_url = reverse_lazy('productos')

class ProdDetailView(generic.DetailView):
    model = Producto
