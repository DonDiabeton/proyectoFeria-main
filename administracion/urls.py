from django.urls import path, re_path
from . import views


urlpatterns = [
    # fabrica
    path('fabricas/', views.fabricas),
    path('fabricas/registrar/', views.registrar_fabrica),
    re_path(r'fabricas/(desactivar|activar)/(\d+)/', views.activar_fabrica),
    # categoria
    path('categorias/', views.categorias),
    path('categorias/registrar/', views.registrar_categoria),
    re_path(r'categorias/(desactivar|activar)/(\d+)/', views.activar_categoria),
    # producto
    path('inventario/', views.inventario),
    path('productos/registrar/', views.registrar_producto),
    path('productos/editar/<int:id>/', views.editar_producto),
    re_path(r'productos/(desactivar|activar)/(\d+)/', views.activar_productos),
    # pedidos
    path('pedidos/', views.pedidos),
    path('pedidos/registrar/', views.registrar_pedido),
    path('pedidos/registrar/<int:fabrica>/', views.registrar_pedido),
    path('pedidos/detalle/<int:id>/', views.detalle_pedido),
    re_path(r'pedidos/(cancelar|recibir)/(\d+)/', views.procesar_pedido),
    # usuarios
    path('usuarios/', views.usuarios),
    path('usuarios/registrar/', views.registrar_usuario),
    path('usuarios/editar/<int:id>/', views.editar_usuario),
    path('usuarios/contrasena/<int:id>/', views.editar_contrasena_usuario),
    re_path(r'usuarios/(deshabilitar|habilitar)/(\d+)/', views.activar_usuario),
]
