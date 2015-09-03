<html><body><p>Si en una terminal tipeamos:

</p><pre>ssh user@domain.com</pre>

el cliente ssh intentará contactarse al puerto 22 de domain.com. Cómo cambiamos ese puerto?

<pre>ssh -p 2222 user@domain.com</pre>

Pero qué pasa si no tenemos acceso a cambiar ese parámetro? Puede pasarnos esto? Sí, por ejemplo si accedemos a un repositorio cvs por ssh; cuando ejecutamos uno de los comandos cvs, el tunel ssh se hace sin que nos demos cuenta. Si el servidor al que nos queremos conectar escucha en un puerto distinto al por defecto, tenemos un problema.



<strong>Hoy no me acordaba cómo se configuraba esto y resultó bastante tedioso buscarlo en Internet </strong>(todas las respuestas a la búsqueda era sobre como cambiar el puerto en el que un servidor ssh <em>escucha</em>). Lo dejo aquí para futuras referencias.



La forma de configurar un puerto por defecto para un cliente ssh en GNU/Linux es editando el archivo <code>.ssh/config</code> y añadiendo la línea:

<pre>Port NNNN</pre>

dónde NNNN es el número de puerto.</body></html>