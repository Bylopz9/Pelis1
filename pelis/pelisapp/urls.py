"""pelis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import home,galeria,contacto,list_peli,nva_peli,actualiza,elimina


urlpatterns = [
    path('', home, name="home"),
    path('contacto', contacto, name="contacto"),
    path('galeria', galeria, name="galeria"),
    path('nva_peli', nva_peli, name="nva_peli"),
    path('list_peli', list_peli, name="list_peli"),
    path('actualiza/<id>/', actualiza, name="actualiza"),
    path('elimina/<id>/', elimina, name="elimina"),
]
