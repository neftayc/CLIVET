from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

# models
from .models import Especie

class EspecieAdmin(admin.ModelAdmin):

    search_fields = ('especie',)
    list_display = (
        'especie',)

admin.site.register(Especie, EspecieAdmin)
