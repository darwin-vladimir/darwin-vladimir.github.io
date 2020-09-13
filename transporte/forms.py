from django import forms
from transporte.models import Transporte

class FormularioTransporte(forms.ModelForm):
    #registro de atractivosnaturales
    class Meta:
        model = Transporte
        fields = ('nombre','tipo_id','ruta','imagen','observaciones')
        labels = {
            #como quiero que se vena los labels
            'nombre': 'Nombre de la cooperativa o línea',
            'tipo_id':'Eliga el tipo de transporte',
            'ruta':'Ingrese El origen y destino',
            'imagen':'Cargue una imagen referente a la cooperativa o línea',
            'observaciones': 'ingrese información adicional',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Nombre de la cooperativa o línea',
                }
            ),
            'tipo_id': forms.Select(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el tipo',
                }
            ),
            'ruta': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el Origen y el destino',
                }
            ),
            'imagen': forms.FileInput(
                attrs = {
                    'placeholder': 'cargue una imagen',
                }
            ),
            'observaciones': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese información adicional que quiera registrar',
                }
            )
        }
