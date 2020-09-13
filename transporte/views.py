from django.shortcuts import render
from django.views.generic import CreateView, ListView,UpdateView, DeleteView
from django.urls import reverse_lazy
from transporte.forms import FormularioTransporte
from transporte.models import Transporte

class ListarTransporte(ListView):
    model = Transporte
    template_name = 'transporte/listar_transporte.html' #queryset = libro.objects.all()  objectList

# Create your views here.
class RegistrarTransporte(CreateView):
    model = Transporte
    form_class = FormularioTransporte
    template_name = 'transporte/crear_transporte.html'
    success_url = reverse_lazy('transporte:listado_transporte')

class ActualizarTransporte(UpdateView):
    model = Transporte
    template_name = 'transporte/crear_transporte.html'
    form_class = FormularioTransporte
    success_url = reverse_lazy('transporte:listado_transporte')
#eliminar usuarios
class EliminarTransporte(DeleteView):
    model = Transporte
    success_url = reverse_lazy('transporte:listado_transporte')
