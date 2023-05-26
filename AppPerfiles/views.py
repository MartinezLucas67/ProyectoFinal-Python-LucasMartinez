from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy 
from AppPerfiles.forms import UserRegisterForm, UserUpdateForm, AvatarFormulario
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, View
from .models import Avatar

def registro(request):
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
        
    else: 
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='AppPerfiles/registro.html',
        context={'form': formulario},
    )

def login_view(request):
   next_url = request.GET.get('next')
   if request.method == "POST":
       form = AuthenticationForm(request, data=request.POST)

       if form.is_valid():
           data = form.cleaned_data
           usuario = data.get('username')
           password = data.get('password')
           user = authenticate(username=usuario, password=password)
           
           if user:
               login(request=request, user=user)
               if next_url:
                   return redirect(next_url)
               url_exitosa = reverse('inicio')
               return redirect(url_exitosa)
   else:  
       form = AuthenticationForm()
   return render(
       request=request,
       template_name='AppPerfiles/login.html',
       context={'form': form},
   )

class CustomLogoutView(LogoutView):
   template_name = 'AppPerfiles/logout.html'

class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
   form_class = UserUpdateForm
   success_url = reverse_lazy('inicio')
   template_name = 'AppPerfiles/perfiles_form.html'

   def get_object(self, queryset=None):
       return self.request.user


class AgregarAvatarView(View):
    def get(self, request):
        avatar = Avatar.objects.filter(user=request.user).first()
        formulario = AvatarFormulario()
        context = {
            'form': formulario,
            'avatar': avatar,
        }
        return render(
            request=request,
            template_name="AppPerfiles/avatar_form.html",
            context=context,
        )

    def post(self, request):
        avatar = Avatar.objects.filter(user=request.user).first()
        formulario = AvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            if avatar:
                avatar.delete()
            avatar = formulario.save(commit=False)
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('ver_avatar')
            return redirect(url_exitosa)
        else:
            context = {
                'form': formulario,
                'avat': avatar,
            }
            return render(
                request=request,
                template_name="AppPerfiles/avatar_form.html",
                context=context,
            )

class EliminarAvatarView(View):
    def get(self, request):
        avatar = Avatar.objects.filter(user=request.user).first()
        context = {
            'avatar': avatar
        }
        return render(request, 'AppPerfiles/avatar_confirm_delete.html', context)

    def post(self, request):
        avatar = Avatar.objects.filter(user=request.user).first()
        if avatar:
            avatar.delete()
        url_exitosa = reverse('inicio')
        return redirect(url_exitosa)

def MiAvatar(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='AppBlog/avatar.html',
        context=contexto,
    )
    return http_response