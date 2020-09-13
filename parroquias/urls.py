from django.urls import path
from . import views

urlpatterns = [
    path('',views.ParroquiasListView.as_view(), name='listado_parroquias'),
    path('search', views.ParroquiaSearchListView.as_view(), name='search'),
    path('<slug:slug>',views.ParroquiaDetailView.as_view(),name='parroquia'),


]
