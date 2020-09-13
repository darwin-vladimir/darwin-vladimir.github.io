from django.contrib import admin
from empresa.models import TipoEmp,Empresa,Producto
# Register your models here.
admin.site.register(TipoEmp)

class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre','detalle','imagen','created_at')
    search_fields=('nombre','detalle')
    list_filter=('nombre',)
admin.site.register(Producto,ProductoAdmin)

class EmpresaAdmin(admin.ModelAdmin):
    list_display=('nombre','direccion','longitud','latitud','descripcion','imagen','tipo_id')
    search_fields=('nombre','descripcion')
    list_filter=('nombre',)

admin.site.register(Empresa,EmpresaAdmin)
