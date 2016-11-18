#encoding: utf-8
from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

# models
from .models.colamedica import ColaMedica
from .models.mascota import Mascota
from .models.consulta import HallasgosClinicos, Diagnostico, Pruebas, Tratamiento
from .models.notas import Notas
from .models.vacunacion import Vacunacion
from .models.historia import Historial
from .models.atencion import Atencion

from apps.clivet.models.trabajador import Trabajador

class HistoriaAdmin(admin.ModelAdmin):
    model = Historial
    search_fields = ('num_historia',)
    list_display = ('num_historia','mascota','get_dueño','created_ath', 'veterinario', 'get_direccion','get_ciudad', 'get_telefono','get_especie','get_raza', 'get_color','get_sexo', 'get_edad', )

    def get_direccion(self, obj):
        return obj.mascota.dueño.direccion
    get_direccion.admin_order_field  = 'mascota'  #Allows column order sorting
    get_direccion.short_description = 'Direccion'

    def get_dueño(self, obj):
        return obj.mascota.dueño
    get_dueño.admin_order_field  = 'mascota'  #Allows column order sorting
    get_dueño.short_description = 'Dueño'

    def get_telefono(self, obj):
        return obj.mascota.dueño.telefono
    get_telefono.admin_order_field  = 'dueño'  #Allows column order sorting
    get_telefono.short_description = 'Telefono'

    def get_ciudad(self, obj):
        return obj.mascota.dueño.ciudad
    get_ciudad.admin_order_field  = 'mascota'  #Allows column order sorting
    get_ciudad.short_description = 'Ciudad'

    def get_especie(self, obj):
        return obj.mascota.especie
    get_especie.admin_order_field  = 'mascota'  #Allows column order sorting
    get_especie.short_description = 'Especie'

    def get_raza(self, obj):
        return obj.mascota.raza
    get_raza.admin_order_field  = 'mascota'  #Allows column order sorting
    get_raza.short_description = 'Raza'

    def get_color(self, obj):
        return obj.mascota.color
    get_color.admin_order_field  = 'mascota'  #Allows column order sorting
    get_color.short_description = 'Color'

    def get_sexo(self, obj):
        return obj.mascota.genero
    get_sexo.admin_order_field  = 'mascota'  #Allows column order sorting
    get_sexo.short_description = 'Sexo'

    def get_edad(self, obj):
        return obj.mascota.fecha_nacimiento
    get_edad.admin_order_field  = 'mascota'  #Allows column order sorting
    get_edad.short_description = 'Edad'


class ColaMedicaAdmin(admin.ModelAdmin):
    model = ColaMedica
    search_fields = ('historia',)
    list_display = ('historia', 'fecha','descripcion','medico',)

class AtencionAdmin(admin.ModelAdmin):
    model = Atencion
    search_fields = ('colamedica__historia__num_historia',)
    list_display = ('get_numhistoria','get_hmascota', 'get_hmascota', 'get_hdueño', )

    def get_numhistoria(self, obj):
        return obj.colamedica.historia.num_historia
    get_numhistoria.admin_order_field  = 'colamedica'  #Allows column order sorting
    get_numhistoria.short_description = 'N° Historia'

    def get_hmascota(self, obj):
        return obj.colamedica.historia.mascota
    get_hmascota.admin_order_field  = 'colamedica'  #Allows column order sorting
    get_hmascota.short_description = 'Mascota'

    def get_hmascota(self, obj):
        return obj.colamedica.historia.mascota.especie
    get_hmascota.admin_order_field  = 'colamedica'  #Allows column order sorting
    get_hmascota.short_description = 'Especie'

    def get_hdueño(self, obj):
        return obj.colamedica.historia.mascota.dueño
    get_hdueño.admin_order_field  = 'colamedica'  #Allows column order sorting
    get_hdueño.short_description = 'Dueño'


admin.site.register(Mascota)
admin.site.register(ColaMedica, ColaMedicaAdmin)
admin.site.register(Notas)
admin.site.register(Diagnostico)
admin.site.register(HallasgosClinicos)
admin.site.register(Pruebas)
admin.site.register(Tratamiento)
admin.site.register(Vacunacion)
admin.site.register(Historial, HistoriaAdmin)
admin.site.register(Atencion, AtencionAdmin)
