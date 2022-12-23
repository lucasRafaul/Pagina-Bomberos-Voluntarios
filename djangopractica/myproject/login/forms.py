from django import forms
from django.forms import ModelForm
from .models import *


# class CrearNoticia(forms.Form):
#titulo = forms.CharField(label='titulo noticia', max_length=50)
# contenido = forms.CharField(
# label='contenido noticia', widget=forms.Textarea)
#imagen = forms.ImageField()

class crearNoticia(forms.ModelForm):
    class Meta:
        model = Noticia
        fields = ['titulo', 'contenido', 'categoria',
                  'imagen', ]
