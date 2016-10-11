from django.contrib import admin

from .models.Categoria import Categoria
from .models.Departamento import Departamento
from .models.Producto import Producto
from .models.UnidadMedida import UnidadMedida

admin.site.register(Departamento)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(UnidadMedida)
