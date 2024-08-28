#este script no es parte de programa sino que se uso unicamente para cargar datos de prueba

from mensajes.models import Mensaje

m1 = Mensaje(texto='hola', remitente='dario', destinatario='keyla', fecha_y_hora='2024-08-27')
m2 = Mensaje(texto='la verdad no se si usar DateTime está bien', remitente='keyla', destinatario='julio', fecha_y_hora='2024-08-28 12:21')
m3 = Mensaje(texto='quiero cocinar galletitas con chips de chocolate', remitente='keyla', destinatario='valeria', fecha_y_hora='2024-08-28 12:22')
m4 = Mensaje(texto='no metas a tu abuela muerta que nadie la falto el respeto', remitente='moria', destinatario='silvina', fecha_y_hora='2011-11-09 23:24')
m5 = Mensaje(texto='ya no se que poneeer', remitente='keyla', destinatario='julio', fecha_y_hora='2024-08-28 12:36')
mensajes = [m1, m2, m3, m4, m5]
for m in mensajes:
    m.save()
