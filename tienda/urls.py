from django.urls import path
from . import views


urlpatterns = [
    path('', views.productos),
    path('producto/<int:id>/', views.producto),
    path('carrito/', views.carrito),
    path('destacados/', views.destacados),
    path('contacto/', views.contacto),
    path('proveedores/', views.proveedores),
    path('fundaciones/', views.fundaciones),
    path('compra/', views.crear_compra),
    path('compra/exitosa', views.compra_exitosa)
]
