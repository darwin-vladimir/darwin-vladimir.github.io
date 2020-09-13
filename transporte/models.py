from django.db import models
# Create your models here.

class TipoTransporte(models.Model):
    nombre_tipo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'TipoTransporte'
        verbose_name_plural = 'Tipos de Tranporte'
        ordering = ['nombre_tipo']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre_tipo

class Transporte(models.Model):
    nombre = models.CharField(max_length=100)
    tipo_id = models.ForeignKey(TipoTransporte, on_delete=models.CASCADE)
    ruta = models.CharField(max_length=100,blank=True, null=True)
    imagen = models.ImageField(upload_to='transportes/',blank=True, null=True)
    observaciones = models.CharField(max_length=500,blank=True, null=True)
    # para conocer cuanto una atractivo_cultural se Registro
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'Transporte'
        verbose_name_plural = 'Transportes'
        ordering = ['nombre']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre
