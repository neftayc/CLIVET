from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Especie(models.Model):

    especie = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    color = models.CharField(max_length=100)

    def __unicode__(self):
        return self.especie
