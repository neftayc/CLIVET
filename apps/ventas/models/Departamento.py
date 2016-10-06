from django.db import models
from TimeStampedModel import TimeStampedModel


class Departamento(TimeStampedModel):
    descripcion = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return self.descripcion
