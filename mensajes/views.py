from django.shortcuts import render
from .models import Mensaje
from .templates import *
# Create your views here.

def buscar_remitente (request):
    return render (request, 'home.html')

def ver_mensajes(request):
    remitente = request.GET.get('remitente')
    mensajes = Mensaje.objects.filter(remitente = remitente)
    return render(request, 'mensajes.html',{'mensajes': mensajes})