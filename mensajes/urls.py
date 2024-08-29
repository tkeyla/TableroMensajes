from django.urls import path
from .import views

urlpatterns = [ 
    path('', views.buscar_remitente, name='home'),
    path('vermensajes', views.ver_mensajes, name='ver_mensajes')
]