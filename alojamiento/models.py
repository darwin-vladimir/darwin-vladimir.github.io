from django.db import models
# Create your models here.

class Alojamiento(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100,blank=True, null=True)
    longitud = models.CharField(max_length=200,blank=True, null=True)
    latitud = models.CharField(max_length=200,blank=True, null=True)
    imagen = models.ImageField(upload_to='alojamientos/',blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    # para conocer cuanto una atractivo_cultural se Registro
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'Alojamiento'
        verbose_name_plural = 'Alojamientos'
        ordering = ['nombre']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre
