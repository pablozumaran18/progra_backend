from django.shortcuts import render
from urllib import request
from django.http import HttpResponse



# Create your views here.


def listado (request):

    dic = {
        "personas" :[{"nombre":"juanito","edad":"18","vocacion":"estudiante"},
        {"nombre":"pedro","edad":"29","vocacion":"informatico"}
        ],
    }

    return render(request,"./apli_nueva/templates/persona.html",dic)

def home (request):

    saludo = {
        "mensaje":"hola mundo"
    }
    return render(request, "./apli_nueva/templates/index.html",saludo)
