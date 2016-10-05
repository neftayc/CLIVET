from django.db import models

class Proveedor(models.Model):
    tipodoc = models.TextField(max_length=30)
    numdoc = models.IntegerField(max_length=30)
    razon_social = models.CharField(max_length=50)
    representante_legal = models.TextField(max_length=50)
    apellidos = models.TextField(null=True, blank=True)
    direccion = models.TextField(max_length=30)
    telefono = models.IntegerField(max_length=9)
    email = models.EmailField(max_length=30)
    enti_bancaria = models.TextField(max_length=30)
    num_cuenta = models.IntegerField(max_length=30)
    estado = models.TextField(max_length=30)

