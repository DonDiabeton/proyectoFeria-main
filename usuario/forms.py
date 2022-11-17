from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.forms import ModelForm
from tienda.models import Usuario, Direccion


class UserForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email']


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name']


class NuevaDireccion(ModelForm):
    class Meta:
        model = Direccion
        fields = ['departamento', 'municipio', 'zona', 'direccion', 'referencia']
