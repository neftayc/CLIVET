from django.db import models
from TimeStampedModel import TimeStampedModel
from Categoria import Categoria
from UnidadMedida import UnidadMedida


class Producto(TimeStampedModel):
    nombre = models.CharField(max_length=50, unique=True)
    codigo = models.CharField(max_length=50, unique=True)
    categoria = models.ForeignKey(Categoria)
    fechaVencimiento = models.DateField()
    unidadMedidaV = models.ForeignKey(UnidadMedida)
    unidadMedidaC = models.ForeignKey(UnidadMedida)
    precioV = models.DecimalField(max_digits=10, decima_place=2)
    precioC = models.DecimalField(max_digits=10, decima_place=2)
    existencia = models.IntegerField()
    MontoReal = models.DecimalField(max_digits=10, decima_place=2)
    igv = models.DecimalField(max_digits=10, decima_place=2)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
