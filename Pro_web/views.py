from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, DetailView
from AppBlog.models import Articulo
from django.urls import reverse_lazy 



def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='AppBlog/index.html',
        context=contexto,
    )
    return http_response

class MiVista(View):
    def get(self, request):      
        mi_texto = "¡Hola, mundo!"
        context = {'texto': mi_texto}
        return render(request, 'AppBlog/acerca_de_mi.html', context)