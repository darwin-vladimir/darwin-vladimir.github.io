from django import forms
from alojamiento.models import Alojamiento

class FormularioAlojamientos(forms.ModelForm):
    #registro de atractivosnaturales
    class Meta:
        model = Alojamiento
        fields = ('nombre','direccion','longitud','latitud','imagen','descripcion')
        labels = {
            #como quiero que se vean los labels
            'nombre': 'Nombre del Alojamiento',
            'direccion':'Dirección',
            'longitud':'coordenadas Longitud',
            'latitud': 'coordenadas Latitud',
            'imagen': 'Imagen',
            'descripcion':'Descripción'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre del Alojamiento',
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
            'imagen': forms.FileInput(
                attrs = {
                    'placeholder': 'cargue una imagen',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripción',
                }
            )
        }
