from django.db import models
from TimeStampedModel import TimeStampedModel


class Mascota(TimeStampedModel):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"

    def __str__(self):
        return self.nombre
