from django.db import models

from apps.compras.models.Proveedor import Proveedor
from apps.clivet.models.trabajador import Trabajador

class Compra(models.Model):

    fe_compra = models.DateTimeField('Fecha de compra', auto_now_add=True)
    #comprobante = models.ImageField('Comprobante', upload_to='/tmp')
    comprobante = models.FileField(upload_to='comprobante_compra', verbose_name='Seleccione el archivo')
    total = models.DecimalField('Total', max_digits=20, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor)
    trabajador = models.ForeignKey(Trabajador)
    
    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return "%d" % (self.id)

