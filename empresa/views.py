from django.shortcuts import render
from django.views.generic import CreateView, ListView,UpdateView, DeleteView
from django.urls import reverse_lazy
from empresa.forms import FormularioEmpresa,FormularioProducto
from empresa.models import Empresa,Producto

class ListarEmpresa(ListView):
    model = Empresa
    template_name = 'empresa/listar_empresa.html' #queryset = libro.objects.all()  objectList

# Create your views here.
class RegistrarEmpresa(CreateView):
    model = Empresa
    form_class = FormularioEmpresa
    template_name = 'empresa/crear_empresa.html'
    success_url = reverse_lazy('empresa:listado_empresa')

class ActualizarEmpresa(UpdateView):
    model = Empresa
    template_name = 'empresa/crear_empresa.html'
    form_class = FormularioEmpresa
    success_url = reverse_lazy('empresa:listado_empresa')
#eliminar usuarios
class EliminarEmpresa(DeleteView):
    model = Empresa
    success_url = reverse_lazy('empresa:listado_empresa')

#********************************productos****************************
class ListarProducto(ListView):
    model = Producto
    template_name = 'empresa/listar_producto.html' #queryset = libro.objects.all()  objectList

# Create your views here.
class RegistrarProducto(CreateView):
    model = Producto
    form_class = FormularioProducto
    template_name = 'empresa/crear_producto.html'
    success_url = reverse_lazy('empresa:listado_producto')

class ActualizarProducto(UpdateView):
    model = Producto
    template_name = 'empresa/crear_producto.html'
    form_class = FormularioProducto
    success_url = reverse_lazy('empresa:listado_producto')
#eliminar usuarios
class EliminarProducto(DeleteView):
    model = Producto
    success_url = reverse_lazy('empresa:listado_producto')
