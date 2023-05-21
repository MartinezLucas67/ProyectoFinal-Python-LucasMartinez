from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy 
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Articulo

class ArticuloListView(ListView):
    model = Articulo
    template_name = 'AppBlog/articulo_list.html'

class ArticuloCreateView(CreateView):
    model = Articulo
    fields = ('autor', 'titulo', 'sub_titulo', 'fecha', 'contenido')
    success_url = reverse_lazy('articulo_list')

class ArticuloDetailView(DetailView):
    model = Articulo
    success_url = reverse_lazy('articulo_list')

class ArticuloUpdateView(UpdateView):
    model = Articulo
    fields = ('titulo', 'sub_titulo', 'contenido')
    success_url = reverse_lazy('articulo_list')

class ArticuloDeleteView(DeleteView):
    model = Articulo
    success_url = reverse_lazy('articulo_list')

