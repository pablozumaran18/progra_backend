from cgitb import html
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def saludo (request):
    return render(request,"./gatos/templates/menu.html")


def agregar (request):
    return render(request,"./gatos/templates/index.html")

def lista (request):
    gato = {"gato1":[{"nombre":"juanito"},{"edad":"2años"},{"raza":"Abisinio"},{"genero":"macho"},{"color":"cafe"},{"peso":"18kg"}]}
    return render(request,"./gatos/templates/lista.html",gato)