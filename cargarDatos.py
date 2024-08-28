#este script no es parte de programa sino que se uso unicamente para cargar datos de prueba

from mensajes.models import Mensaje

m1 = Mensaje(texto='hola', remitente='dario barassi', destinatario='keyla', fecha_y_hora='2024-08-27')
m1.save()