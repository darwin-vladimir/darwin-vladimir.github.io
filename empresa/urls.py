from django.urls import path
from django.contrib.auth.decorators import login_required
from empresa.views import RegistrarEmpresa,ListarEmpresa,ActualizarEmpresa,EliminarEmpresa,RegistrarProducto,ListarProducto,ActualizarProducto,EliminarProducto
urlpatterns = [
    path('listar_empresa/',login_required(ListarEmpresa.as_view()),name ='listado_empresa'),
    path('registrar_empresa/',login_required(RegistrarEmpresa.as_view()),name ='registrar_empresa'),
    path('editar_empresa/<int:pk>/',login_required(ActualizarEmpresa.as_view()), name = 'editar_empresa'),
    path('eliminar_empresa/<int:pk>/',login_required(EliminarEmpresa.as_view()), name = 'eliminar_empresa'),
    #**************************productos*******************************************
    path('listar_producto/',login_required(ListarProducto.as_view()),name ='listado_producto'),
    path('registrar_producto/',login_required(RegistrarProducto.as_view()),name ='registrar_producto'),
    path('editar_producto/<int:pk>/',login_required(ActualizarProducto.as_view()), name = 'editar_producto'),
    path('eliminar_producto/<int:pk>/',login_required(EliminarProducto.as_view()), name = 'eliminar_producto'),
]
