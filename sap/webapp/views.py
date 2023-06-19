from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


""" def bienvenido(request):
    return HttpResponse('Hola mundo desde django')
 """
def bienvenido(request):
    mensajes = {'msg1': 'valor mensaje 1', 'msg2': 'valor mensaje 2'}
    return render(request, 'bienvenido.html', mensajes)


def despedirse(request):
    return HttpResponse('Despedida desde django')