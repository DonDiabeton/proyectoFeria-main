from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('registrar/', views.registrar),
    path('acceder/', views.acceder),
    path('perfil/', views.perfil),
    path('perfil/contrasena/', views.contrasena),
    path('perfil/direcciones/', views.direcciones),
    path('perfil/direcciones/registrar/', views.crear_direccion),
    path('perfil/direcciones/eliminar/<int:id>/', views.eliminar_direccion),
    path('perfil/compras/', views.compras),
    path('perfil/compras/detalle/<int:id>/', views.ver_compra),
    path('perfil/compras/cancelar/<int:id>/', views.cancelar_compra),
    path('salir/', views.salir),
]
