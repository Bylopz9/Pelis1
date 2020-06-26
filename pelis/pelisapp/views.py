from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"pelisapp/home.html")

def contacto(request):
    return render(request,"pelisapp/contacto.html")

def capitulos(request):
    return render(request,"pelisapp/cap.html")