from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Especie(models.Model):

    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Especie"
        verbose_name_plural = "Especies"

    def __str__(self):
        return "%s" % (self.descripcion)

"""
class Autor(models.Model):
    nombre = models.CharField

class Libro(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.ForeignKey(codigo)
    tipo = models.ChoiceField()

class Ejemplar(models.Model):
    codigo = models.CharField(max_length=12)
    libro = models.ForeignKey(nombre)
    def __str__(self):
            return self.codigo
"""
