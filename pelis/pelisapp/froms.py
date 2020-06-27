from django import forms
from django.forms import ModelForm
from .models import Peliculas

class peliForm(ModelForm):

    class Meta:
        model = Peliculas
        fields = ['titulo','duracion','anio','genero']
