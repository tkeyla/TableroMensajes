from django.urls import path
from .import views

urlpatterns = [ 
    path('', views.filtrar, name='home'),
    path('mensajes/recibidos', views.ver_mensajes, name='ver_mensajes')
]