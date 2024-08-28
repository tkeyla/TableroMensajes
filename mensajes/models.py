from django.db import models

class Mensaje(models.Model):
    texto = models.TextField(default='hola')
    remitente = models.CharField(max_length=25)
    destinatario = models.CharField(max_length=25)
    fecha_y_hora = models.DateTimeField()

    def __str__(self):
        return self.texto