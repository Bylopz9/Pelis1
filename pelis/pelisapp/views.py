from django.shortcuts import render
from .models import Peliculas
from .froms import peliForm

# Create your views here.
def home(request):
    return render(request,"pelisapp/home.html")

def contacto(request):
    return render(request,"pelisapp/contacto.html")

def galeria(request):
    return render(request,"pelisapp/galeria.html")

def nva_peli(request):

    data= {
        'from':peliForm()
    }

    if request.method == 'POST':
        formulario = peliForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Se guardaron los cambios correctamente"

    return render(request,"pelisapp/nva_peli.html",data)

def list_peli(request):

    pelicula = Peliculas.objects.all()
    dato = {
        'peliculas': pelicula
    }

    return render(request,"pelisapp/Lista_Pelis.html", dato)

