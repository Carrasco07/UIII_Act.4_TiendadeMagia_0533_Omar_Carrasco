"""
backend_TiendadeMagia URL Configuration

La lista `urlpatterns` enruta URLs a vistas.
"""
from django.contrib import admin
from django.urls import path, include

# =========================================================================
# CONFIGURACIÓN DE URLS DEL PROYECTO (Paso 26)
# =========================================================================

urlpatterns = [
    # Acceso al sitio de administración de Django
    path('admin/', admin.site.urls),
    
    # Enlace a las URLs de la aplicación app_TiendadeMagia
    path('', include('app_TiendadeMagia.urls')), # Ruta raíz
]