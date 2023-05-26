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
        mi_texto = "¡Hola buenas, mi nombre es Lucas Martinez. Soy el creador de la pagina, tengo 24 años recien cumplidos ya que fue el 26/05. Trabajo y soy estudiante de ingenieria aunque estoy mas dedicado al curso de Python por el momento, ya que mi interes es cambiar de trabjo y trabajar en algo relacionado a la programacion y de algo que de verdad me gusta. Espero que les haya gustado mi pagina!"
        context = {'texto': mi_texto}
        return render(request, 'AppBlog/acerca_de_mi.html', context)
    
class Historia_del_cafe(View):
    def get(self, request):      
        mi_texto = "¡Aca iria toda la info sobre el cafe, como tipos, localidades donde se hacen y el proceso.!"
        context = {'texto': mi_texto}
        return render(request, 'AppBlog/historia_del_cafe.html', context)