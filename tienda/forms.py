from django.forms import ModelForm
from .models import Compra


class NuevaCompra(ModelForm):
    class Meta:
        model = Compra
        fields = ['nombre', 'nit', 'direccion', 'telefono']
