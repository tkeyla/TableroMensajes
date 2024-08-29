from django.urls import path
from .import views

urlpatterns = [ 
    path('', views.buscar_remitente, name='home'),
    path('mensajes/recibidos', views.ver_mensajes, name='ver_mensajes')
]