from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from tienda.models import Usuario, Fabrica, Producto, Categoria


class UserForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'tipo']


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'tipo']


class PasswordChangeForm(forms.Form):
    new_password1 = forms.CharField(max_length=100)
    new_password2 = forms.CharField(max_length=100)


class NuevaFabrica(ModelForm):
    class Meta:
        model = Fabrica
        fields = ['nombre', 'estado', 'tipo']


class NuevaCategoria(ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'estado']


class NuevoProducto(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'precio_pedido',
                  'imagen', 'estado', 'categoria', 'fabrica']
