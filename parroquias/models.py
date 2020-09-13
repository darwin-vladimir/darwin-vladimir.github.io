from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
import uuid
# Create your models here.

class Parroquia(models.Model):
    nombre_parr = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    longitud = models.CharField(max_length=200,blank=True, null=True)
    latitud = models.CharField(max_length=200,blank=True, null=True)
    slug = models.SlugField(null=False, blank=False, unique=True )
    imagen = models.ImageField(upload_to='parroquias/')
    historia = models.TextField(blank=True, null=True)
    info_general = models.TextField(blank=True, null=True)
    situacion_geografica=models.TextField(blank=True, null=True)
    
    # para conocer cuanto una parroquias se Registro
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name= 'Parroquia'
        verbose_name_plural = 'Parroquias'
        ordering = ['nombre_parr']

    #def save(self, *arg, **Kwargs):
    #    self.slug = slugify(self.nombre_parr)
    #    super(Parroquia,self).save(*arg, **Kwargs)

    #para que se muestre por nombre en el admin
    def __str__(self):
        return self.nombre_parr

#generar slug unico
def set_slug(sender, instance, *args, **kwargs):  #callback
    if instance.nombre_parr and not instance.slug:
        slug = slugify(instance.nombre_parr)
        while Parroquia.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.nombre_parr,str(uuid.uuid4())[:8])
            )
        instance.slug = slug
#antes de guardar ejecute slug
pre_save.connect(set_slug, sender=Parroquia)
