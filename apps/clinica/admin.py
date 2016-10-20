#encoding: utf-8
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

# models
from .models.colamedica import ColaMedica
from .models.mascota import Mascota
from .models.consulta import Consulta
from .models.notas import Notas
from .models.vacunacion import Vacunacion
from .models.historia import Historial


class HistoriaAdmin(admin.ModelAdmin):

    search_fields = ('num_historia',)
    list_display = (
        'num_historia', 'propietario','persona', 'veterinario', 'created_ath',)


admin.site.register(Mascota)
admin.site.register(ColaMedica)
admin.site.register(Notas)
admin.site.register(Consulta)
admin.site.register(Vacunacion)
admin.site.register(Historial, HistoriaAdmin)
