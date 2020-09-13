from django.db import models
# Create your models here.

class TipoEmp(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'TipoEmp'
        verbose_name_plural = 'Tipos de Empresa'
        ordering = ['nombre']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    detalle = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='productos/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'Producto'
        verbose_name_plural = 'Productos de la empresa'
        ordering = ['nombre']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100,blank=True, null=True)
    longitud = models.CharField(max_length=200,blank=True, null=True)
    latitud = models.CharField(max_length=200,blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='empresa/',blank=True, null=True)
    tipo_id = models.ForeignKey(TipoEmp, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    # para conocer cuando  se Registro
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['nombre']
    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre
