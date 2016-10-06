from django.db import models
from TimeStampedModel import TimeStampedModel
from Departamento import Departamento


class Categoria(TimeStampedModel):
    descripcion = models.CharField(max_length=50, unique=True)
    departamento = models.ForeignKey(Departamento)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.descripcion
