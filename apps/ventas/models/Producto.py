from django.db import models
from ..models.Categoria import Categoria
from ..models.UnidadMedida import UnidadMedida


class Producto(models.Model):
    nombre = models.CharField('Nombre', max_length=50, unique=True)
    codigo = models.CharField('Código', max_length=50, unique=True)
    categoria = models.ForeignKey('Categoria', Categoria)
    fechaVencimiento = models.DateField('Fecha de Vencimiento')
    unidadMedidaV = models.ForeignKey(
        UnidadMedida, related_name='ventas', verbose_name="Unidad de medida de Ventas")
    unidadMedidaC = models.ForeignKey(UnidadMedida, related_name='compras',
                                      verbose_name='Unidad de medida de Compras')
    precioV = models.DecimalField(
        'Precio de venta', max_digits=10, decimal_places=2)
    precioC = models.DecimalField(
        'Precio de Compra', max_digits=10, decimal_places=2)
    existencia = models.IntegerField('Cantidad de Productos')
    MontoReal = models.DecimalField(
        'Monto Real', max_digits=10, decimal_places=2)
    igv = models.DecimalField('IGV', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
