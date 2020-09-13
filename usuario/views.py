from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,TemplateView
from usuario.models import Usuario
from usuario.forms import FormularioLogin, FormularioUsuario

#iniciar secion
class Login(FormView):
    template_name = 'usuario/login.html'
    form_class = FormularioLogin
    success_url = reverse_lazy('index')
    # medidas de seguridad
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs): #verifica la peticion
        #si hay un usuario q hace una peticion y esta logeado.
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url()) #redireccina
        else:
            return super(Login, self).dispatch(request, *args, **kwargs) #si o esta logeado
    #valida el formulario de esta vista
    def form_valid(self, form):
        login(self.request, form.get_user()) #indico qe cree una iinstancia e inicie una secion
        return super(Login, self).form_valid(form)

#cerrar secion
def logoutUsuario(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/')

#listar usuarios registrados
class ListadoUsuario(ListView):
    model = Usuario
    template_name = 'usuario/listar_usuario.html'
    #para listar puedo usar esta forma o
    #queryset = Usuario.objects.filter(usuario_activo = True)  #listar los usuarios activos
    #o definiendo los get_queryset
    def get_queryset(self):
        return self.model.objects.filter(usuario_activo=True)

#registrar usuarios
class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'usuario/crear_usuario.html'
    success_url = reverse_lazy('usuarios:listar_usuarios')

#esta es otra forma en la que se puede validar y registrar la informacion
#no se valida con el request.post porq django ya sabe q es de ese metodo
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            #creo una nusva isntancia de usuario
            nuevo_usuario = Usuario(
                email=form.cleaned_data.get('email'), #valor que me llega del formulario
                username=form.cleaned_data.get('username'),
                nombres=form.cleaned_data.get('nombres'),
                apellidos=form.cleaned_data.get('apellidos')
            )
            nuevo_usuario.set_password(form.cleaned_data.get('password1')) #encripto la constraseña
            nuevo_usuario.save() #metodo save del modelo
            return redirect('usuarios:listar_usuarios')
        else:
            return render(request,self.template_name,{'form':form})
#ActualizarUsuario
class ActualizarUsuario(UpdateView):
    model = Usuario
    template_name = 'usuario/crear_usuario.html'
    form_class = FormularioUsuario
    success_url = reverse_lazy('usuarios:listar_usuarios')
#eliminar usuarios
class EliminarUsuario(DeleteView):
    model = Usuario
    success_url = reverse_lazy('usuarios:listar_usuarios')
