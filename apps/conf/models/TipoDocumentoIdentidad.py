u"""Módulo Model Tipo Documento"""

from django.db import models


class TipoDocumentoIdentidad(models.Model):
    u"""
    TipoDocumentoIdentidad Modelo.

    Basado en la tabla 2 sunat.
    """
    numero = models.CharField(max_length=3, verbose_name="Número")
    descripcion = models.CharField(max_length=100, verbose_name="Descripción")

    class Meta:
        verbose_name = "Tipo Documenento Identidad"
        verbose_name_plural = "Tipos Documentos Identidad"

    def __str__(self):
        return "%s" % (self.descripcion)
