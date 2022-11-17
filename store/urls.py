from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tienda/', include('tienda.urls')),
    path('administracion/', include('administracion.urls')),
    path('', include('usuario.urls')),
]
