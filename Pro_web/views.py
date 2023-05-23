from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, ListView
from AppBlog.models import Articulo
from django.urls import reverse_lazy 

class ArticuloIndexListView(ListView):
    model = Articulo
    template_name = 'AppBlog/index.html'
    context_object_name = 'articulos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cantidad_articulos'] = self.get_queryset().count()
        return context


class MiVista(View):
    def get(self, request):      
        mi_texto = "¡Hola, mundo!"
        context = {'texto': mi_texto}
        return render(request, 'AppBlog/acerca_de_mi.html', context)