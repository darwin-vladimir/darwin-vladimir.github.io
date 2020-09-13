from django.shortcuts import render
from django.views.generic import CreateView, ListView,UpdateView, DeleteView
from django.urls import reverse_lazy
from atractivos_naturales.forms import FormularioAtractivoNatural
from atractivos_naturales.models import AtractivoNatural

class ListarAtractivoNatural(ListView):
    model = AtractivoNatural
    template_name = 'atractivos_naturales/listar_atractivos.html' #queryset = libro.objects.all()  objectList

# Create your views here.
class RegistrarAtractivoNatural(CreateView):
    model = AtractivoNatural
    form_class = FormularioAtractivoNatural
    template_name = 'atractivos_naturales/crear_atractivo.html'
    success_url = reverse_lazy('atractivos_naturales:listado_atractivos')

class ActualizarAtractivoNatural(UpdateView):
    model = AtractivoNatural
    template_name = 'atractivos_naturales/crear_atractivo.html'
    form_class = FormularioAtractivoNatural
    success_url = reverse_lazy('atractivos_naturales:listado_atractivos')
#eliminar usuarios
class EliminarAtractivoNatural(DeleteView):
    model = AtractivoNatural
    success_url = reverse_lazy('atractivos_naturales:listado_atractivos')
