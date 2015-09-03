<html><body><p>RadioFrecuencia es una herramienta que estoy haciendo para la <a href="http://capas1y2news.blogspot.com/">cátedra de Comunicaciones</a> la cual permite, dados los datos de una instalación de dos antenas calcular si existe línea de vista, si es factible la comunicación (sensibilidad de recepción) y realiza un diagrama de vano.

<!--more-->

El 7 de septiembre le mandé un mail a avarios amigos con la dirección web de la primera versión beta que la prueben y me avisen de errores que encuentraban (muchas gracias a todos los que la probaron!). Estuve haciendo algunas correcciones y dejé en <s>http://firebirds.com.ar/~juanjo/rf/</s> <strong>[UPDATE]</strong> <a href="http://comunicaciones.firebirds.com.ar/rf/">http://comunicaciones.firebirds.com.ar/rf/</a> una versión un poco más refinada. Sin enbargo todavía faltan algunas cosas como permitir seleccionar un tipo de antena y a partir de este seleccionar alguna característica particular del tipo como diámetro o sectorización y a partir de estos datos la herramienta solo obtendría la ganacia de la antena. Actualmente la ganancia es introducida directamente por el usuario (alumno).

</p><h2>Qué falta?</h2>

<ul>

	<li><strong>Una mejor forma de selección del tipo de antena</strong> (lo que mencioné antes)  <span style="color: rgb(255, 0, 0);"><strong>[REQUERIRÁ SU TIEMPO]</strong></span></li>

	<li><strong>Permitir poner obstáculos entre las antenas:</strong> esto ya es soportado por el módulo que se encarga de generar el diagrama de vano pero todavía tengo que hacer una buena interfaz que permite cargar fácilmente para cada obstáculo la distancia que lo separa de la primer antena y su alura. <span style="color: rgb(255, 0, 0);"><strong>[REQUERIRÁ SU TIEMPO]</strong></span></li>

	<li>Permitir la carga manual de algunos valores. <span style="color: rgb(255, 204, 51);"><strong>[MEDIO]</strong></span></li>

	<li>Brindar otros datos de interés en la salida. <span style="color: rgb(0, 153, 0);"><strong>[TRIVIAL]</strong></span></li>

</ul>

<h2>Ejemplos de salida</h2>

<center>

<a href="http://firebirds.com.ar/%7Ejuanjo/wordpress/wp-content/uploads/2006/09/rf3.png"><img id="image165" width="400" src="http://firebirds.com.ar/%7Ejuanjo/wordpress/wp-content/uploads/2006/09/rf3.png" alt="rf3"></a>

<a href="http://firebirds.com.ar/%7Ejuanjo/wordpress/wp-content/uploads/2006/09/rf1.png">

<img id="image163" width="400" src="http://firebirds.com.ar/%7Ejuanjo/wordpress/wp-content/uploads/2006/09/rf1.png" alt="rf1"></a>



<a href="http://firebirds.com.ar/%7Ejuanjo/wordpress/wp-content/uploads/2006/09/rf2.png"><img id="image164" width="400" src="http://firebirds.com.ar/%7Ejuanjo/wordpress/wp-content/uploads/2006/09/rf2.png" alt="rf2"></a>

</center>

<h2>Una nota de color (gris)</h2>

Cuando lo probé desde Internet Explorer, el navegador de Microsoft me di cuenta de que no se veía tan bien como yo lo venía en mi máquina (con Firefox de la fundación Mozilla), el problema es que IE no soporta imagenes en formato PNG con transparencia. Abajo unos ejemplos de las imágenes con las que tuve problemas:

<center>

<a href="http://firebirds.com.ar/%7Ejuanjo/wordpress/wp-content/uploads/2006/09/rf4.png"><img id="image166" width="400" src="http://firebirds.com.ar/%7Ejuanjo/wordpress/wp-content/uploads/2006/09/rf4.png" alt="rf4">

</a>

<a href="http://firebirds.com.ar/%7Ejuanjo/wordpress/wp-content/uploads/2006/09/rf5.png">

<img id="image167" width="400" src="http://firebirds.com.ar/%7Ejuanjo/wordpress/wp-content/uploads/2006/09/rf5.png" alt="rf5"></a>

</center>

Querés leer maś sobre esto? Hay mucho <a href="http://www.google.com.ar/search?hl=es&amp;hs=PP9&amp;client=firefox&amp;rls=org.mozilla:en-US:unofficial&amp;sa=X&amp;oi=spell&amp;resnum=0&amp;ct=result&amp;cd=1&amp;q=Internet+Explorer+png+transparency&amp;spell=1">allá afuera</a>. Realmente este tema (y las diferencias entre los navegadores en general) es una molestia para las personas que desarrollan para la web. La mentablemente los navegadores que no se preocupan por cumplir con los estándares no ayudan a resolver el problema. Por mi parte.. me uno al grito: <a href="http://www.spreadfirefox.com/">Spread FireFox!</a>

</body></html>