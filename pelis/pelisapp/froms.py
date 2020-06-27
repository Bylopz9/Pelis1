from django import forms
from django.forms import ModelForm
from .models import Peliculas

#Se crea este archivo en la carpeta de la app para inportar un formulario de DJANGO y asi evitar la generacion del codigo en html

#Se crea una clase para importar los modelos de formulario
class peliForm(ModelForm):
#La clase meta es para importar los datos de la base de datos al formulario.
    class Meta:
        model = Peliculas
        fields = ['titulo','duracion','anio','genero']
