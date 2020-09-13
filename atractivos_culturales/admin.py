from django.contrib import admin
from .models import TipoAC,AtractivoCultural
# Register your models here.
admin.site.register(TipoAC)

class AtractivoCulturalAdmin(admin.ModelAdmin):
    list_display=('nombre','descripcion','direccion','longitud','latitud','tipo_id')
    search_fields=('nombre','descripcion')
    list_filter=('nombre',)

admin.site.register(AtractivoCultural,AtractivoCulturalAdmin)
