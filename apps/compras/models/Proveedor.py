from django.db import models

class Proveedor(models.Model):


    Tipo_Documento = (
        ('RUC', 'Registro Único de Comprobante'),
        ('DNI', 'Documento nacional de Identidad'),
    )

    Estado_proveedor = (
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    )

    tipodoc = models.CharField('Tipo de Documento', max_length=30, choices=Tipo_Documento, default='Registro Único de Comprobante')
    numdoc = models.IntegerField('Número de documento', max_length=30)
    razon_social = models.CharField('Razon social', max_length=50)
    representante_legal = models.CharField('Representante legal', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=30)
    direccion = models.CharField('Direccion', max_length=30)
    telefono = models.IntegerField('Telefono', max_length=9)
    email = models.EmailField('Email', max_length=30)
    enti_bancaria = models.CharField('Entidad bancaria', max_length=30)
    num_cuenta = models.IntegerField('Número de cuenta', max_length=30)
    estado = models.CharField('Estado', max_length=30, choices=Estado_proveedor, default='Activo')

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return "%s" % (self.razon_social)

