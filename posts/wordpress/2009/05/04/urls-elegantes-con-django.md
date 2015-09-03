<html><body><em>Este texto es parte del informe de nuestro  proyecto final de carrera, lo publico en forma separada aquí por que tiene valor propio y puede convencer a más de un programador PHP de probar Django. Las URLs elegantes son la forma natural de las URL en Django.</em>

<h3>Manejo de URLs</h3>

<p>Tener URLs elegantes y limpias es un requisito común para aplicaciones web modernas. Django provee un mecanismo de manejo de URLs basado en expresiones regulares que asocia una expresión regular a una vista.</p>

<p>Para diseñar las URLs de una aplicación Django, se construye una especie de tabla que mapea patrones de URL a funciones Python a ejecutar (vistas). Con esto se logra que las URLs estén desacopladas del resto de la aplicación.</p>

<p>El siguiente es un ejemplo de una entrada de esa tabla:</p>

<p><code>(r'^index/$', index)</code></p>

<p>Suponiendo que la aplicación web está corriendo en el servidor con nombre localhost, cuando alguien acceda a http://localhost/index/ se ejecutará la vista ‘index’.</p>

<p>El siguiente es un ejemplo un poco más complejo:</p>

<p><code>(r'^cliente/datos/(\d+)/$', cliente_datos)</code></p>

<p>En el patrón de la URL se utilizan paréntesis para capturar una parte de la misma y poder accederla luego como parámetros en la vista. La expresión encerrada entre paréntesis se denomina grupo y son propias de las expresiones regulares en Python. Así, siempre que se acceda a, por ejemplo, http://localhost/cliente/datos/1/ o http://localhost/cliente/datos/100/ se ejecutará la vista cliente_datos y recibirá como parámetro el número correspondiente.</p>

<p>Algo similar sucede en el siguiente ejemplo:</p>

<p><code>(r'^inmueble/fotos/(\d+)/eliminar/(\d+)/$', eliminar_foto)</code></p>

<p>Con la diferencia de que ahora la vista recibe dos parámetros, en este caso particular el primero corresponde a un identificador de inmueble y el segundo a un identificador de foto.</p>

<p>Las expresiones regulares en Python soportan también lo que se denomina grupos nombrados. Esto permite obtener un grupo por su nombre. Si escribimos una especificación de URL como la siguiente:</p>

<p><code>(r'^inmueble/fotos/(?P&lt;inmueble&gt;\d+)/eliminar/(?P&lt;foto&gt;\d+)/$', eliminar_foto)</code></p>

<p>la vista será llamada utilizando parámetros nombrados. Esto tiene la ventaja de que si cambia el orden de los parámetros en la URL, la vista seguirá funcionando sin que se necesite redefinirla.</p></body></html>