from django.contrib import admin
from .models import TipoTransporte,Transporte
# Register your models here.
admin.site.register(TipoTransporte)

class TransporteAdmin(admin.ModelAdmin):
    list_display=('nombre','tipo_id','ruta','imagen','observaciones')
    search_fields=('nombre','tipo_id')
    list_filter=('nombre',)

admin.site.register(Transporte,TransporteAdmin)
