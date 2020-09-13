from django import forms
from empresa.models import Empresa,Producto

class FormularioEmpresa(forms.ModelForm):
    #registro de atractivosnaturales
    class Meta:
        model = Empresa
        fields = ('nombre','direccion','longitud','latitud','descripcion','imagen','tipo_id','productos')
        labels = {
            #como quiero que se vean los labels
            'nombre': 'Nombre de la empresa',
            'direccion':'Dirección',
            'longitud':'coordenadas Longitud',
            'latitud': 'coordenadas Latitud',
            'descripcion':'Descripción',
            'imagen': 'Imagen',
            'tipo_id': 'Tipo de empresa',
            'producto':'productos que realiza'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre de la empresa',
                }
            ),
            'direccion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la dirección',
                }
            ),
            'longitud': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'longitud',
                }
            ),
            'latitud': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'latitud',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripción',
                }
            ),
            'imagen': forms.FileInput(
                attrs = {
                    'placeholder': 'cargue una imagen',
                }
            ),
            'tipo_id': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Seleccione el tipo',
                }
            ),
            'productos': forms.SelectMultiple(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Seleccione los productos',
                }
            )
        }

class FormularioProducto(forms.ModelForm):
    #registro de atractivosnaturales
    class Meta:
        model = Producto
        fields = ('nombre','detalle','imagen')
        labels = {
            #como quiero que se vean los labels
            'nombre': 'Nombre del producto',
            'detalle':'Detalle del producto',
            'imagen': 'Imagen'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre del producto',
                }
            ),
            'detalle': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una detalle del producto',
                }
            ),
            'imagen': forms.FileInput(
                attrs = {
                    'placeholder': 'cargue una imagen',
                }
            )
        }
