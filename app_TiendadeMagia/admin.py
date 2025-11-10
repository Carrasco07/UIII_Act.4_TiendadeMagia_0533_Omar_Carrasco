from django.contrib import admin
from .models import Producto, OrdenDeVenta, DetalleOrden

# =========================================================================
# CLASES ADMIN PARA PERSONALIZAR EL PANEL
# =========================================================================

class ProductoAdmin(admin.ModelAdmin):
    # list_display, list_filter y ordering corregidos para usar 'fecha_registro'
    list_display = (
        'nombre', 
        'categoria', 
        'precio', 
        'stock', 
        'proveedor', 
        'fecha_registro' # <-- CORREGIDO
    )
    
    list_filter = (
        'categoria', 
        'proveedor', 
        'fecha_registro' # <-- CORREGIDO
    )
    search_fields = ('nombre', 'categoria', 'proveedor')
    ordering = ('nombre',)

class DetalleOrdenInline(admin.TabularInline):
    """Permite editar los detalles directamente desde la orden."""
    model = DetalleOrden
    extra = 1 # Número de formularios vacíos a mostrar
    readonly_fields = ('precio_unitario',) # El precio se obtiene del producto

class OrdenDeVentaAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 
        'cliente', 
        'fecha_orden', 
        'total', 
        'estado', 
        'metodo_pago',
        'comentarios'
    )
    list_filter = ('estado', 'metodo_pago')
    search_fields = ('cliente', 'pk')
    ordering = ('-fecha_orden',)
    inlines = [DetalleOrdenInline]

# =========================================================================
# REGISTRO DE MODELOS
# =========================================================================

admin.site.register(Producto, ProductoAdmin)
admin.site.register(OrdenDeVenta, OrdenDeVentaAdmin)
admin.site.register(DetalleOrden)