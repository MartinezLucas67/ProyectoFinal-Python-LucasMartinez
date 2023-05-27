from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy 
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

from .models import Articulo


class ArticuloListView(ListView):
    model = Articulo
    template_name = 'AppBlog/articulo_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cantidad_articulos'] = self.get_queryset().count()
        return context

@method_decorator(login_required, name='dispatch')
class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ('titulo', 'sub_titulo', 'fecha', 'contenido', 'imagen')
    success_url = reverse_lazy('articulo_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.imagen = self.request.FILES.get('imagen')
        return super().form_valid(form)


class ArticuloDetailView(DetailView):
    model = Articulo
    success_url = reverse_lazy('articulo_list')
    
@method_decorator(login_required, name='dispatch')
class ArticuloUpdateView(UpdateView):
    model = Articulo
    fields = ('titulo', 'sub_titulo', 'contenido')
    success_url = reverse_lazy('articulo_list')

@method_decorator(login_required, name='dispatch')
class ArticuloDeleteView(DeleteView):
    model = Articulo
    success_url = reverse_lazy('articulo_list')

