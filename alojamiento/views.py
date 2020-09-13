from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from alojamiento.forms import FormularioAlojamientos
from alojamiento.models import Alojamiento

class ListarAlojamiento(ListView):
    model = Alojamiento
    template_name = 'alojamiento/listar_alojamientos.html' #queryset = libro.objects.all()  objectList
# Create your views here.
class RegistrarAlojamiento(CreateView):
    model = Alojamiento
    form_class = FormularioAlojamientos
    template_name = 'alojamiento/crear_alojamiento.html'
    success_url = reverse_lazy('alojamiento:listar_alojamientos')

class ActualizarAlojamiento(UpdateView):
    model = Alojamiento
    template_name = 'alojamiento/crear_alojamiento.html'
    form_class = FormularioAlojamientos
    success_url = reverse_lazy('alojamiento:listar_alojamientos')
#eliminar usuarios
class EliminarAlojamiento(DeleteView):
    model = Alojamiento
    success_url = reverse_lazy('alojamiento:listar_alojamientos')
