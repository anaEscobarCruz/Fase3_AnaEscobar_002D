from django.shortcuts import render
from . models import Producto1
from django.views import generic

# Create your views here.
def Index(request) :
    produ = Producto1.objects.all().count()

    return render(
        request,
        'index.html',
        context={'produ': produ},
    )
def confecciones(request) :
    produ = Producto1.objects.all()
    return render(
        request,
        'confecciones.html',
        context={'producto':produ}
    )
def estampados(request) :
    produ = Producto1.objects.all().count()
    return render(
        request,
        'estampados.html',
        context={'producto':produ}
    )
#Formulario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto1

class ProdCreate(CreateView):
    model = Producto1
    fields = ['nom', 'cant']

class ProdUpdate(UpdateView):
    model = Producto1
    fields = ['nom', 'cant']

class ProdDelete(DeleteView):
    model = Producto1
    success_url = reverse_lazy('confecciones')

class ProdDetailView(generic.DetailView):
    model = Producto1
