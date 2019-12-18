"""
Definition of views.
"""
# -*- coding: utf-8 -*-
from django.shortcuts import render
from app.services.preparacion import lee_kml
from app.services.visualizacion import grafica_cluster
from app.services.clasificacion import agrupa
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    #coordenadas_df = lee_kml('app\services\doc-checkpoint.kml')
    #cluster, centros = agrupa(coordenadas_df, 10)
    #grafica_cluster(cluster, centros)
    #with open('app\services\col3.txt', 'r', encoding="utf-8") as archivo:
        #print(archivo.read().decode('utf8'), end="")
        #head = [next(archivo) for x in range(2)]
    #print(head)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def login(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/login.html',
        {
            'title':'Login',
        }
    )
