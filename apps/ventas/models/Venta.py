from django.db import models

from apps.clivet.models.cliente import Cliente
from apps.sad.models import User


class Venta(models.Model):
    fechav = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(
        max_digits=20, decimal_places=2, blank=True, null=True)
    cliente = models.ForeignKey(Cliente)
    user = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return " %s" % (self.id)
