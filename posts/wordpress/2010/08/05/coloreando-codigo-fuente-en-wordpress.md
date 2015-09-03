<html><body><p>Tengo este blog hace unos 5 años y en él tengo muchos posts con código fuente, pero nunca usé un plug-in para hacer <strong>syntax highlight</strong> o resaltado de sintáxis, es decir que las distintas partes del código fuente se pinten de distintos colores según su significado. Mi idea es solucionarlo.



El escenario es bastante complicado. Hay bloques de código en los que uso la etiqueta HTML &lt;pre&gt; y otros en los que uso la etiqueda &lt;code&gt;. También tengo código in-line (es decir líeas de código que forman parte de una oración) arcadas con la etiqueta &lt;code&gt;.

<!--more-->

</p><h2>¿Qué busco?</h2>

<ul>

	<li>No quiero posts con código coloreado de ahora en adelante y que los anteriores

sigan en blanco y negro.</li>

	<li>No quiero tener que editar cada posts para agregar algún atributo en las

etiquetas pre o code. Por ejemplo, muchos plug-ins te piden que marques el código

con algo como &lt;pre lang="python"&gt; o similar.</li>

	<li>Quiero que los bloques de código &lt;pre&gt; y &lt;code&gt; se vean igual.</li>

</ul>

Luego de buscar un poco, decidí instalar y probar estos plug-ins:

<ul>

	<li><a href="http://wordpress.org/extend/plugins/wp-synhighlight/" target="_blank">WP-SynHighlight</a> (lo descarté enseguida, tiene una GUI pesada con muchas opciones y las marcas que introduce en el post son bastante poco estándar e intrusivas)</li>

	<li><a href="http://wordpress.org/extend/plugins/wp-syntax/" target="_self">WP-Syntax</a> (usa <a href="http://qbnz.com/highlighter/" target="_blank">GeSHI</a>, por lo que el coloreado se realiza en el lado del servidor)</li>

	<li><a href="http://wordpress.org/extend/plugins/jquery-syntax/" target="_blank">JQuery.Syntax</a> (hecho con la popular librería de JavaScript)</li>

	<li><a href="http://wordpress.org/extend/plugins/google-code-prettify-for-wordpress/" target="_self">Google Code Prettify</a> (está basado en tecnología de Google y posiblemente lo hayan visto en acción en <a href="http://stackoverflow.com/" target="_blank">StackOverflow</a>. Su principal ventaja es que <strong>no requiere decirle en qué lenguaje está escrita la porción de código</strong>, sino que este lo adivina)</li>

</ul>

Intentar empezar a usar uno de estos plug-ins ahora, me genera un gran problema

de compatibilidad hacia atrás :)



Veamos... <strong>WP-SynHighlight</strong> no me gustó de arranque. Modifica la GUI del editor WYSIWYG the WordPress, uno selecciona una porción de código, aprieta el botón y te da unas 10 opciones para elegir (desde lenguaje hasta el número de espacios para los tabs). Puede funcionar para algún tipo de usuario, pero no para un programador. Además agrega bastante código sucio al HTML del post. Paso.



El segundo que probé fue <strong>WP-Syntax</strong>. Me gustó mucho, entre otras cosas:

<ul>

	<li> Usa CSS in-line para que el código coloreado se mantenga incluso si el posts no es leído en el blog; por ejemplo en un planeta o por RSS.</li>

	<li>Si el texto es más ancho que la página, agrega una barra de desplazamiento en la cajita de código.<a href="/wp-content/uploads/2010/08/wpsyntax.jpg"><img class="aligncenter size-full wp-image-2581" title="wpsyntax" src="/wp-content/uploads/2010/08/wpsyntax.jpg" alt="" width="235" height="250"></a></li>

</ul>

Luego probé JQuery.Syntax y Google Code Prettify. Estos funcionan de la siguiente forma: luego de que se carga el HTML del sitio, corre código JavaScript que se encarga del coloreado. Esto hace que la carga de la página sea más lenta.



<a href="/wp-content/uploads/2010/08/jquery.jpg"><img class="aligncenter size-full wp-image-2582" title="jquery" src="/wp-content/uploads/2010/08/jquery.jpg" alt="" width="244" height="230"></a>

<h2>¿Qué hice?</h2>

Me decidí a usar WP-Syntax y para no editar todos los bloques de código, creé un pequeño plug-in para WordPress que cambia todos los &lt;pre&gt; por &lt;pre lang="python" escaped="true"&gt;, cambié a mano los pocos bloques code que tenía por bloques pre y agregué a mano la especificación para los bloques de código que no son Python (no eran muchos).



Tampoco tengo coloreado del código in-line. De las opciones que probé solo el plug-in que usa tecnología de Google, tenía esta característica.



Si ven algún post en el que algo no quedó del todo bien, avisen!</body></html>