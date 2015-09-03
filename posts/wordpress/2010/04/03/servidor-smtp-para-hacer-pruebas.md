<html><body><p>Cuando estamos programando, muchas veces necesitamos de un servidor de mails para que nuestro programa envíe todo tipo de mensajes: reportes de error, avisos, passowords luego de una gesistración, "contact us", etc...



Muchas veces no se tiene un servidor SMTP instalado en la computadora de desarrollo, pero si tenemos <a href="http://www.python.org/" target="_blank">Python</a> instalado, podemos ejecutar el siguiente comando y tener un servidor de prueba en el que en lugar de enviar los mails porla red, se imprimen por la salida standar:



</p><pre lang="bash">python -m smtpd -n -c DebuggingServer localhost:25</pre></body></html>