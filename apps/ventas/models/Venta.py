from django.db import models

from apps.clivet.models.cliente import Cliente
from apps.clivet.models.trabajador import Trabajador


class Venta(models.Model):
    fechaV = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    cliente = models.ForeignKey(Cliente)
    trabajador = models.ForeignKey(Trabajador)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return "%d" % (self.total)
