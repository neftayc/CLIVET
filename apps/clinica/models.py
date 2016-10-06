from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Especie(models.Model):

    especie = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __unicode__(self):
        return self.especie



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
