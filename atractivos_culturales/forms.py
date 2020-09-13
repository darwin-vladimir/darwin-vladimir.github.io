from django import forms
from .models import AtractivoCultural

class FormularioAtractivoCultural(forms.ModelForm):
    #registro de atractivosnaturales
    class Meta:
        model = AtractivoCultural
        fields = ('nombre','descripcion','direccion','longitud','latitud','imagen','tipo_id','fecha')
        labels = {
            #como quiero que se vena los labels
            'nombre': 'Nombre del Atractivo Cultural',
            'descripcion':'Descripción',
            'direccion':'Dirección',
            'longitud':'coordenadas Longitud',
            'latitud': 'coordenadas Latitud',
            'imagen': 'Imagen',
            'tipo': 'Elija el tipo',
            'fecha': 'Engrese la fecha si se trata de una festividad'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre del atractivo',
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese una descripción',
                }
            ),
            'direccion_an': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la dirección',
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
            ),
            'fecha': forms.DateInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'seleccine la fecha si se trata de una festividad',
                }
            )
        }
