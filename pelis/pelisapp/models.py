from django.db import models


class generos(models.Model):

    genero=models.CharField(max_length=80,verbose_name="GENERO")

    def __str__(self):
        return self.genero

class Peliculas(models.Model):
    titulo = models.CharField(max_length=200,verbose_name="NOMBRE DE LA PELICULA")
    duracion = models.TimeField(verbose_name="DURACIÓN")
    anio = models.IntegerField(verbose_name="AÑO")
    genero = models.ForeignKey(generos, on_delete=models.CASCADE,verbose_name="GENERO")

    def __str__(self):
        return self.titulo
