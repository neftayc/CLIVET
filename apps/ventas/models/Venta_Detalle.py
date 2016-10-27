from django.db import models

from ..models.Producto import Producto
from ..models.Venta import Venta


class Detalle_Venta(models.Model):
    producto = models.ForeignKey(Producto)
    venta = models.ForeignKey(Venta)
    cantidad = models.IntegerField()
    igv = models.DecimalField(decimal_places=2, max_digits=20)
    importe = models.DecimalField(decimal_places=2, max_digits=20)

    class Meta:
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalles Venta'

    def __str__(self):
        return "%d" % (self.cantidad)
