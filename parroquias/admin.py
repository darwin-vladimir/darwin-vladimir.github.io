from django.contrib import admin
from .models import Parroquia

class ParroquiaAdmin(admin.ModelAdmin):
    fields = ('nombre_parr', 'direccion','longitud','latitud','imagen','historia','info_general','situacion_geografica' )
    list_display = ('__str__','slug','created_at')

# Register your models here.
admin.site.register(Parroquia, ParroquiaAdmin)
