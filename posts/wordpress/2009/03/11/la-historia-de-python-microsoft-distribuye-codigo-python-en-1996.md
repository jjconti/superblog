<html><body><em>El siguiente texto es una traducción del artículo Microsoft Ships Python Code... in 1996 de Greg Stein publicado en <a href="http://python-history.blogspot.com/" target="_blank">http://python-history.blogspot.com/</a>.</em>

<!--more-->

<h2>Microsoft distribuye código Python... en 1996</h2>

¡Muchas gracias a Guido por permitirme compartir mi propia historia de Python!



Me guardo mi iniciación en Python para otro post, pero el resultado final fue su introducción en un emprendimiento que co-fundé en 1991 con otras personas. Estábamos trabajando en un gran sistema cliente/servidor de comercio electrónico entre empresas y consumidores. Protocolos TCP propios operando sobre la vieja red X.25 y todo eso. Vieja escuela.



En 1995 nos dimos cuenta, contrariamente a nuestra primera impresión, que la mayoría de los consumidores no estaban en Internet, y que necesitábamos un sistema para nuestros clientes (los vendedores) para que lleguen a sus clientes basados en Internet. Tuve la tarea de definir nuestro enfoque y elegí Python como mi herramienta de prototipado.



Nuestro primer problema fue cambiar a una solución basada totalmente en el navegador. Nuestro cliente a medida ya no era viable, necesitamos una experiencia de compra nueva para los clientes e infraestructura de servidores para soportarla. En ese entonces, hablarle a un navegador significaba escribir scripts de CGI para los servidoes Apache o Netscape HTTP. Usando CGI, me conectaba a nuestro servidor existente para procesar las ordenes, mantener el carrito de compras y obtener información de los productos. Estos scripts producían HTML plano (¡no había AJAX en 1995!).



Este enfoque era menos que ideal ya que cada petición tomaba tiempo y creaba un nuevo proceso CGI. La velocidad de respuesta era muy pobre. Luego, en diciembre de 1995, mientras asistía al Python Workshop en Washington DC, me introdujeron a algunos módulos para Apache y Netscape (de Digital Creations, mejor conocidos como Zope) que corrían en forma persistente en el proceso del servidor. Estos módulos usaban un sistema RPC llamado ILU para comunicarse contra otros procesos por detrás. Con este sistema funcionando, la sobrecarga del CGI desapareció y la experiencia de compra ¡se podía disfrutar bastante! Empezamos a convertir el prototipo en código real. Mientras más lejos íbamos, mejor lucía y más personas se unían al proyecto. El desarrollo se movió <b>muy</b> rápido durante los siguientes meses (¡gracias Python!).



En enero de 1996 Microsoft llamó a nuestra puerta. Su esfuerzo interno por crear un sistema de comercio electrónico no tenía éxito y necesitaban personas que conocieran la industria (nosotros habíamos estado haciendo comercio electrónico ya por varios años en ese momento) y que fueran ágiles. Continuamos desarrollando el software durante la primavera mientras las negociaciones se llevaban a cabo y luego la adquisición finalizó en junio de 1996.



Una vez que llegamos a Microsoft con nuestra pequeña pila de código Pyhon, tuvimos que resolver como distribuir el producto en Windows NT. El equipo al que nos unimos tenía mucha experiencia y creó un plug-in para IIS que permitía comunicarse mediante tuberías nombradas al servidor que estaba por detrás, un servicio de NT con el código de nuestro servidor Python embebido. Con una primavera loca empezando en julio, distribuimos Microsoft Merchant Server 1.0 en octubre de 1996.



Y si... si mirabas bajo la alfombra, en algún lugar escondido, había un intérprete de Python, algunas DLLs y un montón de archivos .pyc. Ciertamente Microsoft no se dio cuenta de este hecho, pero estaba ahí si sabías dónde mirar.

<em>Traducido por Juan José Conti.

Revisado por César Portela.

Si encontrás errores en esta traducción, por favor reportalos en un comentario y los corregiremos a la brevedad.</em>

Todas las traducciones de esta serie pueden encontrarse en <a href="/categoria/aprendiendo-python/historia/" target="_self">La historia de Python</a>.</body></html>