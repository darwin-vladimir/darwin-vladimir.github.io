from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Parroquia
# Create your views here.
class ParroquiasListView(ListView):
    template_name = 'parroquias/lista_parroquias.html'
    queryset = Parroquia.objects.all().order_by('nombre_parr')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message']='Listado de parroquias'
        context['parroquias'] = context['parroquia_list']
        print('parroquia_list')
        return context

class ParroquiaDetailView(DetailView):
    model = Parroquia
    template_name = 'parroquias/parroquia.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

class ParroquiaSearchListView(ListView):
    template_name='parroquias/search.html'
    def get_queryset(self):
        return Parroquia.objects.filter(nombre_parr__icontains=self.query())

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['parroquia_list'].count()
        return context
