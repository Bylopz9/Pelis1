from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"pelisapp/home.html")

def contacto(request):
    return render(request,"pelisapp/contacto.html")

def galeria(request):
    return render(request,"pelisapp/galeria.html")

def galeria(request):
    return render(request,"pelisapp/pelicula.html")