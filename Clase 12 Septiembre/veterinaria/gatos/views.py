from cgitb import html
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def saludo (request):
    context ={
        "mensaje":"bienvenidos"
    }

    return render(request,"./gatos/templates/menu.html",context)


def agregar (request):
    return render(request,"./gatos/templates/index.html")

def lista (request):
    context = {
        "gatos" : [{"nombre":"juan","edad":"3 años","raza":"albino","genero":"macho","color":"negro","peso":"12kg"},
    {"nombre":"femina","edad":"1 año","raza":"Callejero","genero":"Hembra","color":"Blanca","peso":"2kg"},
    {"nombre":"Maria","edad":"5 años","raza":"nulo","genero":"Hembra","color":"blanca","peso":"4kg"},
    {"nombre":"pedrito","edad":"6","raza":"n","genero":"m","color":"gris","peso":"8kg"}]
    }
    
    return render(request,"./gatos/templates/lista.html",context)