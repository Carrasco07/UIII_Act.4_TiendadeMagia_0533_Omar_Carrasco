from django.urls import path
from . import views

# =========================================================================
# CONFIGURACIÓN DE URLS DE LA APLICACIÓN (FINAL)
# =========================================================================

urlpatterns = [
    # URL de Inicio
    path('', views.inicio_TiendadeMagia, name='inicio_TiendadeMagia'),

    # =========================================================================
    # URLS PARA PRODUCTOS (Respetando tus nombres originales: actualizar_producto, borrar_producto)
    # =========================================================================
    path('productos/', views.ver_producto, name='ver_producto'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    
    # Actualización (GET)
    path('productos/actualizar/<int:producto_id>/', 
         views.actualizar_producto, 
         name='actualizar_producto'),
         
    # Actualización (POST)
    path('productos/actualizar/realizar/<int:producto_id>/', 
         views.realizar_actualizacion_producto, 
         name='realizar_actualizacion_producto'),
         
    # Borrar producto
    path('productos/borrar/<int:producto_id>/', 
         views.borrar_producto, 
         name='borrar_producto'),

    # =========================================================================
    # URLS PARA ÓRDENES DE VENTA
    # =========================================================================
    path('ordenes/', views.ver_ordenes, name='ver_ordenes'),
    path('ordenes/agregar/', views.agregar_orden, name='agregar_orden'),
    path('ordenes/editar/<int:pk>/', views.editar_orden, name='editar_orden'),
    path('ordenes/eliminar/<int:pk>/', views.eliminar_orden, name='eliminar_orden'),

    # =========================================================================
    # URLS PARA DETALLES DE ORDEN (Activadas para solucionar el error NoReverseMatch)
    # =========================================================================
    path('detalles/', views.ver_detalles, name='ver_detalles'),
    path('detalles/agregar/', views.agregar_detalle, name='agregar_detalle'),
    path('detalles/editar/<int:pk>/', views.editar_detalle, name='editar_detalle'),
    path('detalles/eliminar/<int:pk>/', views.eliminar_detalle, name='eliminar_detalle'),

    # =========================================================================
    # URLS PARA REPORTES
    # =========================================================================
    path('reportes/', views.ver_reportes, name='ver_reportes'),
]