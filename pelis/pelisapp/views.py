from django.shortcuts import render, redirect
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
        'form':peliForm()
        }
    if request.method == 'POST':
        formulario = peliForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Seguardaron los cambios correctamente"
    return render(request,"pelisapp/nva_peli.html",data)


def list_peli(request):
#solicita informacion de la base de datos para mostarla en los templates 
# la variable pelicula se genera para almacenar la informacion de la Base de datos 
    pelicula = Peliculas.objects.all()
    # Este diccionario se genera para solicitar la indormacion de la base de datos 
    dato = { 
        'Peliculas': pelicula
        }
    return render(request,"pelisapp/Lista_Pelis.html", dato)

def actualiza(request, id):

    pelicula = Peliculas.objects.get(id=id)
    data= {
        'form':peliForm(instance=pelicula)
        }
    
    if request.method == 'POST':
        formulario = peliForm(data=request.POST, instance=pelicula)

        if formulario.is_valid():
            formulario.save()
            data['mensaje']= "Peliacula actualizada correctamente"
            data['form'] = formulario

    return render(request,"pelisapp/actualiza.html",data)

def elimina(request,id):
    pelicula = Peliculas.objects.get(id=id)
    pelicula.delete()

    return redirect(to="list_peli")