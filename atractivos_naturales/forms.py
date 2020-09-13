from django import forms
from .models import AtractivoNatural

class FormularioAtractivoNatural(forms.ModelForm):
    #registro de atractivosnaturales
    class Meta:
        model = AtractivoNatural
        fields = ('nombre_an','descripcion','direccion_an','longitud_an','latitud_an','imagen','tipo_id')
        labels = {
            'nombre_an': 'Nombre del Atractivo Natural',
            'descripcion':'Descripción',
            'direccion_an':'Direccion',
            'longitud_an':'coordenadas Longitud',
            'latitud_an': 'coordenadas Latitud',
            'imagen': 'Imagen',
            'tipo_id': 'Elija el tipo'
        }
        widgets = {
            'nombre_an': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'nombre del atractivo',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripcion',
                }
            ),
            'direccion_an': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la direccion',
                }
            ),
            'longitud_an': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'longitud',
                }
            ),
            'latitud_an': forms.TextInput(
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
            'tipo_id': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el tipo',
                }
            )
        }
