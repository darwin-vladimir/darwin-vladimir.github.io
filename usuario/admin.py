from django.contrib import admin
from usuario.models import Usuario

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('username','email','nombres','apellidos','cedula')
    search_fields=('username','nombres','apellidos','cedula')
    list_filter=('username',)

admin.site.register(Usuario,UserAdmin)
