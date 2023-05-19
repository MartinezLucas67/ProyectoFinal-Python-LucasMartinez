from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy 
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Articulo

class ArticuloListView(ListView):
    model = Articulo
    template_name = 'control_code/lista_articulos.html'

class ArticuloCreateView(CreateView):
    model = Articulo
    fields = ('autor', 'titulo', 'sub_titulo', 'fecha', 'contenido')
    success_url = reverse_lazy('lista_articulos')

class ArticuloDetailView(DetailView):
    model = Articulo
    success_url = reverse_lazy('lista_articulos')

class ArticuloUpdateView(UpdateView):
    model = Articulo
    fields = ('titulo', 'sub_titulo', 'contenido')
    success_url = reverse_lazy('lista_articulos')

class ArticuloDeleteView(DeleteView):
    model = Articulo
    success_url = reverse_lazy('lista_articulos')

