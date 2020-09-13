from .import views
from django.urls import path
from django.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from parroquias.views import ParroquiasListView
from usuario.views import Login,logoutUsuario
from django.contrib.auth.decorators import login_required

urlpatterns = [

    #administrador de django
    path('admin/', admin.site.urls),
    #sitio-administrador
    path('administrador/index', views.home_view, name='home'),
    #************************ dedicadas al usuario ******************
    path('usuarios/',include(('usuario.urls','usuarios'))),
    path('accounts/login/', Login.as_view(), name= 'login'),
    path('logout/',login_required(logoutUsuario), name= 'logout'),
    #********************** ruta de la app parroquias****************
    path('parroquias/',include(('parroquias.urls','parroquias'))),
    #********************** ruta de atarctivos Naturales*************
    path('atractivos_naturales/',include(('atractivos_naturales.urls','atractivos_naturales'))),
    #********************** ruta de atarctivos Culturales*************
    path('atractivos_culturales/',include(('atractivos_culturales.urls','atractivos_culturales'))),
    #********************** ruta de alojamiento*************
    path('alojamiento/',include(('alojamiento.urls','alojamiento'))),
    #********************** ruta de transporte*************
    path('transporte/',include(('transporte.urls','transporte'))),
    #********************** ruta de empresa*************
    path('empresa/',include(('empresa.urls','empresa'))),
    #************************ Index Turista **********************
    path('', views.index_view, name='index'),
    path('turista/',include(('interfaz_turista.urls','turista'))),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
