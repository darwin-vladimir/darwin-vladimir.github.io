from django.contrib import admin
from .models import TipoAN,AtractivoNatural
# Register your models here.
admin.site.register(TipoAN)


class AtractivoNaturalAdmin(admin.ModelAdmin):
    list_display=('nombre_an','descripcion','direccion_an','longitud_an','latitud_an','tipo_id')
    search_fields=('nombre_an','descripcion')
    list_filter=('nombre_an',)

admin.site.register(AtractivoNatural,AtractivoNaturalAdmin)
