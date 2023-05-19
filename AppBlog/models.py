from django.db import models

class Articulo(models.Model):
    autor = models.CharField(max_length=256)
    titulo = models.CharField(max_length=256)
    sub_titulo = models.CharField(max_length=256)
    fecha = models.DateField(auto_now_add=True)
    contenido = models.TextField()
    
    def __str__(self):
        return f"{self.autor} {self.titulo}"
