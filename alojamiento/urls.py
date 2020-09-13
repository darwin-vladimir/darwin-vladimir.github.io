from django.urls import path
from django.contrib.auth.decorators import login_required
from alojamiento.views import ListarAlojamiento, RegistrarAlojamiento,ActualizarAlojamiento,EliminarAlojamiento

urlpatterns = [
    path('listar_alojamientos/',login_required(ListarAlojamiento.as_view()),name ='listar_alojamientos'),
    path('registrar_alojamiento/',login_required(RegistrarAlojamiento.as_view()),name ='registrar_alojamiento'),
    path('editar_alojamiento/<int:pk>/',login_required(ActualizarAlojamiento.as_view()), name = 'editar_alojamiento'),
    path('eliminar_alojamiento/<int:pk>/',login_required(EliminarAlojamiento.as_view()), name = 'eliminar_alojamiento'),
]
