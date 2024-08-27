from django.db import models

# Create your models here.
# Texto del mensaje: Contenido del mensaje.
# Remitente: Usuario que envía el mensaje.
# Destinatario: Usuario que recibe el mensaje.
#  Fecha y hora de envío: Timestamp del momento en que se envía el

class Mensaje(models.Model):
    texto = models.TextField()
    remitente = models.CharField(max_length=25)
    destinatario = models.CharField(max_length=25)
    fecha_y_hora = models.DateTimeField()

    def __str__(self):
        return self