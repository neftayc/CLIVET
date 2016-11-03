from django.contrib import admin

from .models.Categoria import Categoria
from .models.Departamento import Departamento
from .models.Producto import Producto
from .models.UnidadMedida import UnidadMedida
from .models.Venta import Venta
from .models.Venta_Detalle import Detalle_Venta

admin.site.register(Departamento)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(UnidadMedida)
admin.site.register(Venta)
admin.site.register(Detalle_Venta)
