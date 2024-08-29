from django.shortcuts import render
from .models import Mensaje
from .templates import *
# Create your views here.

def buscar_remitente (request):
    return render (request, 'home.html')

def ver_mensajes(request):
    filtro = request.GET.get('filtro')
    
    if filtro == 'todos':
        mensajes = Mensaje.objects.all()
    else: 
        nombre = request.GET.get('nombre')
        filtro = {filtro: nombre}
        mensajes = Mensaje.objects.filter(**filtro)
    return render(request, 'mensajes.html',{'mensajes': mensajes})