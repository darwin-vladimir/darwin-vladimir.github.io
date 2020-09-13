from django.urls import path
from django.contrib.auth.decorators import login_required
from atractivos_culturales.views import RegistrarAtractivoCultural, ListarAtractivoCultural,ActualizarAtractivoCultural,EliminarAtractivoCultural

urlpatterns = [
    path('listar_atractivos_cultural/',login_required(ListarAtractivoCultural.as_view()),name ='listado_atractivos'),
    path('registrar_atractivo/',login_required(RegistrarAtractivoCultural.as_view()),name ='registrar_atractivo'),
    path('editar_atractivo_cultural/<int:pk>/',login_required(ActualizarAtractivoCultural.as_view()), name = 'editar_atractivo'),
    path('eliminar_atractivo_cultural/<int:pk>/',login_required(EliminarAtractivoCultural.as_view()), name = 'eliminar_atractivo'),
]
