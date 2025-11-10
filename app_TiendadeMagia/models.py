from django.db import models
from datetime import date 

# =========================================================================
# 1. CONSTANTES DE CHOICES (Definidas Globalmente)
# =========================================================================

ESTADO_CHOICES = [
    ('Pendiente', 'Pendiente'),
    ('Enviado', 'Enviado'),
    ('Entregado', 'Entregado'),
    ('Cancelado', 'Cancelado'),
]

METODO_CHOICES = [
    ('Efectivo', 'Efectivo'),
    ('Tarjeta', 'Tarjeta de Crédito/Débito'),
    ('Transferencia', 'Transferencia Bancaria'),
]

# =========================================================================
# 2. MODELO Producto
# =========================================================================

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.CharField(max_length=100, blank=True, null=True)
    stock = models.IntegerField(default=0)
    fecha_registro = models.DateField(default=date.today) 

    class Meta:
        verbose_name = "Producto de Magia"
        verbose_name_plural = "Productos de Magia"
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


# =========================================================================
# 3. MODELO OrdenDeVenta
# =========================================================================

class OrdenDeVenta(models.Model):
    cliente = models.CharField(max_length=100)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    direccion_envio = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # Uso de las constantes globales
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='Pendiente') 
    metodo_pago = models.CharField(max_length=50, choices=METODO_CHOICES, default='Efectivo')
    
    comentarios = models.TextField(blank=True, null=True) 

    class Meta:
        verbose_name = "Orden de Venta"
        verbose_name_plural = "Órdenes de Venta"
        ordering = ['-fecha_orden']

    def __str__(self):
        return f"Orden #{self.pk} - Cliente: {self.cliente}"


# =========================================================================
# 4. MODELO DetalleOrden
# =========================================================================

class DetalleOrden(models.Model):
    orden = models.ForeignKey(OrdenDeVenta, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Detalle de Orden"
        verbose_name_plural = "Detalles de Órdenes"
        unique_together = ('orden', 'producto') 
        
    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en Orden #{self.orden.pk}"

    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario