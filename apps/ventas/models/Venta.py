from django.db import models

from apps.clivet.models.cliente import Cliente
from apps.clivet.models.trabajador import Trabajador


class Venta(models.Model):
    codigo = models.CharField(max_length=50, primary_key=True, unique=True)
    fechav = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    cliente = models.ForeignKey(Cliente)
    trabajador = models.ForeignKey(Trabajador)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return "%s %s %s" % (self.codigo, self.cliente.persona.first_name,
                             self.cliente.persona.last_name)
