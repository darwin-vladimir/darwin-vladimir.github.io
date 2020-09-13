from django.urls import path
from .views import DatosParroquiaView,FomentoProdutivo,Turismo,Actividades
urlpatterns = [
    path('datos_generales/',DatosParroquiaView.as_view(),name ='datos_generales'),
    path('fomento_productivo/',FomentoProdutivo.as_view(),name ='fomento_productivo'),
    path('turismo/',Turismo.as_view(),name ='turismo'),
    path('actividades/',Actividades.as_view(),name ='actividades'),

]
