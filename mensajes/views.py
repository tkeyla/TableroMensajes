from django.shortcuts import render
from .models import Mensaje
from .templates import *
# Create your views here.

def ver_mensajes(request):
    mensajes = Mensaje.objects.all()
    return render(request, 'mensajes.html',{'mensajes': mensajes})