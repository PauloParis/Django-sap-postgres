from django.shortcuts import render
from django.http import HttpResponse
from personas.models import Persona, Domicilio
# Create your views here.

def bienvenido(request):
    # Persona.objects -> se conecta a la db 
    num_personas = Persona.objects.count()
    #personas = Persona.objects.all()
    personas = Persona.objects.order_by('id', 'nombre') # '-id -> ordena alrevez
    return render(request, 'bienvenido.html', {
        'num_personas': num_personas,
        'personas': personas
        })


def domicilios(request):
    num_domicilios = Domicilio.objects.count()
    domicilios = Domicilio.objects.all()
    return render(request, 'domicilios.html', {
        'num_domicilios': num_domicilios,
        'domicilios': domicilios
    })
