from django.db import models
from TimeStampedModel import TimeStampedModel


class UnidadMedida(TimeStampedModel):
    nombre = models.CharField(max_length=50, unique=True)
    simbolo = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidad de Medidas"

    def __str__(self):
        return self.nombre
