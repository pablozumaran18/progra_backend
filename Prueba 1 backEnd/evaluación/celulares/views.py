from multiprocessing import context
from django.shortcuts import render

# Create your views here.


def inicio (request):

    context = {"saludo": "Bienvenido al listado de celulares :D"}

    return render(request,"inicio.html",context)

def lista_cel(request):
    context = {"celulares":[{"marca":"xiomi", "modelo":"mi 11 pro", "año":"2020", "fecha":"2021"},
    {"marca":"samsung", "modelo":"s21 fe", "año":"2021", "fecha":"2022"},
    {"marca":"apple", "modelo":"iphone 11 pro max", "año":"2021", "fecha":"2022"},
    {"filtro":2020}]}
    return render(request,"listaCelulares.html",context)