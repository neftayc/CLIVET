from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

# models
from .models.especie import Especie
from .models.mascota import Mascota

class MascotaAdmin(admin.ModelAdmin):

    search_fields = ('nombre',)
    list_display = (
        'num_historia','nombre','dueño','especie','genero','estado')

admin.site.register(Mascota, MascotaAdmin)
admin.site.register(Especie)
