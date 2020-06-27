from django.contrib import admin
from .models import generos, Peliculas



class PeliculasAdmin(admin.ModelAdmin):
    list_display = ['titulo','duracion','anio','genero']
    search_fields = ['titulo','anio']
    list_filter = ['genero']
    list_per_page = 100



admin.site.register(generos)
admin.site.register(Peliculas, PeliculasAdmin)

