from django.shortcuts import render
from django.views.generic.list import ListView
from parroquias.models import Parroquia
from django.views.generic import TemplateView

# Create your views here.

class DatosParroquiaView(ListView):
    template_name = 'interfaz_turista/datos_generales.html'
    queryset = Parroquia.objects.get(pk=1)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class FomentoProdutivo(TemplateView):
    template_name = 'interfaz_turista/fomento_productivo.html'

class Turismo(TemplateView):
    template_name = 'interfaz_turista/turismo.html'

class Actividades(TemplateView):
    template_name = 'interfaz_turista/actividades.html'
