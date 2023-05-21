from django.db import models
from django.contrib.auth.models import User

class Articulo(models.Model):
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    titulo = models.CharField(max_length=256)
    sub_titulo = models.CharField(max_length=256)
    fecha = models.DateField()
    contenido = models.TextField()
    
    def __str__(self):
        return f"{self.autor} {self.titulo}"
