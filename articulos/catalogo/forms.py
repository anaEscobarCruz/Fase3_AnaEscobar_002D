from .models import Producto1
from django import forms


class ProdForms(forms.ModelForm):

    id= forms.CharField(label='id',max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
    nom = forms.CharField(label='Nombre producto',max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
    prec = forms.CharField(label='Precio',max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))
    cant = forms.CharField(label='Cantidad',max_length=150,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Producto1
        fields = ('id','nom', 'prec','cant')