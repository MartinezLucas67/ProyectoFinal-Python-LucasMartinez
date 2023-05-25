from django import forms
from .models import Articulo

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ('autor', 'titulo', 'sub_titulo', 'fecha', 'contenido', 'imagen')
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={'multiple': True}),
        }
        labels = {
            'imagen': 'Imagen',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].required = False

