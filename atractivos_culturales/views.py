from django.shortcuts import render
from django.views.generic import CreateView, ListView,UpdateView, DeleteView
from django.urls import reverse_lazy
from atractivos_culturales.forms import FormularioAtractivoCultural
from atractivos_culturales.models import AtractivoCultural

class ListarAtractivoCultural(ListView):
    model = AtractivoCultural
    template_name = 'atractivos_culturales/listar_atractivos.html' #queryset = libro.objects.all()  objectList

# Create your views here.
class RegistrarAtractivoCultural(CreateView):
    model = AtractivoCultural
    form_class = FormularioAtractivoCultural
    template_name = 'atractivos_culturales/crear_atractivo.html'
    success_url = reverse_lazy('atractivos_culturales:listado_atractivos')

class ActualizarAtractivoCultural(UpdateView):
    model = AtractivoCultural
    template_name = 'atractivos_culturales/crear_atractivo.html'
    form_class = FormularioAtractivoCultural
    success_url = reverse_lazy('atractivos_culturales:listado_atractivos')
#eliminar usuarios
class EliminarAtractivoCultural(DeleteView):
    model = AtractivoCultural
    success_url = reverse_lazy('atractivos_culturales:listado_atractivos')
