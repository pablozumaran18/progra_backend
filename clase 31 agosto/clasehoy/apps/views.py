from cgitb import html
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound

# Create your views here.


def bienvenidos(request):
    return HttpResponse ("hola mundo")

def index (request):
    html = "<h1> hola mundo -index  </h1>"

    return HttpResponse(html)

def notfoundjeje (request):
    if True :
        return HttpResponseNotFound("<h1> page not found </h1>")
    else:
        html = "<h3> todo ok </h3>"
        return HttpResponse (html)