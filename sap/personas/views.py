from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

# Create your views here.
from personas.models import Persona, Domicilio
from personas.forms import PersonaForm, DomicilioForm


def detallePersona(request, id):
    #persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id) # si se introduce un id no valido tira error 404
    return render(request, 'personas/detalle.html', {'persona': persona})


#PersonaForm = modelform_factory(Persona, exclude=[])
# esta linea se reemplaza por el archivo forms.py

def nuevaPersona(request):
    if request.method == 'POST':
        # request.POST -> # obtener info de todos los parametros que se envien en el formulario
        # formaPersona se llena con los valores enviados
        formaPersona = PersonaForm(request.POST) 
        if formaPersona.is_valid(): # validar los datos enviados
            formaPersona.save() # insert en la db
            return redirect('index') # de sap/urls
        """ else:
            return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona}) """
    else: 
        formaPersona = PersonaForm()
        # return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})

    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})



def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona) 
        if formaPersona.is_valid():
            formaPersona.save() # aqui funciona como update
            return redirect('index')
    else:
        
        formaPersona = PersonaForm(instance=persona)
    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})



def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)

    if persona:
        persona.delete()
    return redirect('index')










def detalleDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    return render(request, 'domicilios/detalle.html', {'domicilio': domicilio})



def nuevaDomicilio(request):
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST) 
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('domicilios')
    else: 
        formaDomicilio = DomicilioForm()

    return render(request, 'domicilios/nuevo.html', {'formaDomicilio': formaDomicilio})



def editarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST, instance=domicilio) 
        if formaDomicilio.is_valid():
            formaDomicilio.save() 
            return redirect('domicilios')
    else:
        formaDomicilio = DomicilioForm(instance=domicilio)
    return render(request, 'domicilios/editar.html', {'formaDomicilio': formaDomicilio})



def eliminarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)

    if domicilio:
        domicilio.delete()
    return redirect('domicilios')