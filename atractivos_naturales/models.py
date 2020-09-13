from django.db import models
# Create your models here.

class TipoAN(models.Model):
    nombre_tipo_an = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'TipoAN'
        verbose_name_plural = 'Tipos de Atractivos Naturales'
        ordering = ['nombre_tipo_an']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre_tipo_an

class AtractivoNatural(models.Model):
    nombre_an = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='atractivos_naturales/',blank=True, null=True)
    direccion_an = models.CharField(max_length=100,blank=True, null=True)
    longitud_an = models.CharField(max_length=200,blank=True, null=True)
    latitud_an = models.CharField(max_length=200,blank=True, null=True)
    tipo_id = models.ForeignKey(TipoAN, on_delete=models.CASCADE)
    # para conocer cuanto una atractivo_naturales se Registro
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'AtractivoNatural'
        verbose_name_plural = 'Atractivos Naturales'
        ordering = ['nombre_an']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre_an
