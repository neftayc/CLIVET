from django.db import models
from ..models.Categoria import Categoria
from ..models.UnidadMedida import UnidadMedidaC


class Producto(models.Model):
    nombre = models.CharField('Nombre', max_length=50, unique=True)
    codigo = models.CharField('Código', max_length=50, unique=True,
                              blank=True,
                              help_text='El codigo debe ser lalala')
    categoria = models.ForeignKey('Categoria', Categoria)
    fechaVencimiento = models.DateField(
        'Fecha de vencimiento', blank=True, null=True)
    unidad_medida = models.ForeignKey(
        UnidadMedidaC,
        related_name='unidad_de_medida',
        verbose_name="U. medida compra a ventas")
    precioV = models.DecimalField(
        'Precio de venta', max_digits=10, decimal_places=2)
    precioC = models.DecimalField(
        'Precio de Compra', max_digits=10, decimal_places=2)
    existencia = models.PositiveIntegerField(
        'Cantidad de Productos', default=0)
    MontoReal = models.DecimalField(
        'Monto Real', max_digits=10, decimal_places=2)
    igv = models.DecimalField('IGV', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
