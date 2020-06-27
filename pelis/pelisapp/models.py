from django.db import models

# Create your models here.
class generos(models.Model):

    genero=models.models.CharField(max_length=50)

class Peliculas(models.Model):
    titulo=models.CharField(max_length=200)
    duracion=models.TimeField()
    anio=models.IntegerField()
    genero=models.models.ForeignKey(generos, on_delete=models.CASCADE)
    