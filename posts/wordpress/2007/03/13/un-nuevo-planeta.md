<html><body><p>No, no. No se trata de atronomía. En la <a href="http://es.wikipedia.org/wiki/Blogosfera">blogósfera</a> un planeta a una agregación de blogs que tratan sobre un tema en común. Por ejemplo, es muy común en los proyectos grandes de Software Libre que exista una planeta del mismo. En este se pueden encontrar las entradas más recientes los los blogs de los desarrolladores del mismo.



Todos los planetas que visite usan un software escrito en <a href="http://www.python.org">Python</a> llamado <a href="http://www.planetplanet.org">Planet</a>. Tenía ganas de probarlo así que ayer a la tarde bajé la versión 2.0 (primer <em>release</em> oficial) y lo instalé en <a href="http://blogs.firebirds.com.ar">blogs.firebirds.com.ar</a> (a falta de un mejor dominio).



<!--more-->Tiene un archivo de configuración en el qeu se deben agregar las direcciones de los feeds que se quiere reunir en el planeta y ejecutando unprograma (.py) se crea una página index.html estática a partir de un  template llamado index.html.tmpl y varios archivos xml también a partir de sus propios templates (archivos .xml.tmpl).



Queremos que esta ejecución de lleve a cabo cada cierto tiempo, para que index.html se vaya actualizando. Para esto se agrega una entrada en el <code>crontab</code>.

<code>

[squirt]$ crontab -l

*/15    *       *       *       *       /home/jjconti/blogs.firebirds.com.ar/planet.sh &gt; /dev/null 2&gt;&amp;1

</code>



Esa línea ejecuta cada 15 minutos el script planet.sh y redirije tanto su salida estándar como su error estándar a /dev/null para que no la veamos (recibamos por mail dentro del sistema). [1]



Fácil y rápido el sitio quedó andando. Le cambié el logo por defecto por uno qeu hice en 5' en el <a href="http://www.gimp.org" target="_blank">GIMP</a> (a falta de uno mejor) y le cargué los feeds de algunos amigos en Santa Fe.



Ahora que? Bueno, vamos a dejar el sitio en línea. A falta de un mejor nombre (e imaginación) bauticé el planeta como Computadoras en Santa Fe, un nombre que ciertamente es bastante malo. Se aceptan sugerencias para un nombre mejor (y para todo lo señalado como <em>a falta de uno mejor</em>). Gracias.

Por último: si sos de Santa Fe, tenés un blog, en el escribís sobre software, computadoras y la vida misma (no es necesario que exclusivamente) y tenés ganas de ser un habitante más de este nuevo planeta, <a href="mailto:jjconti@gnu.org">mandame un mail</a> con la dirección de feed (rss o atom) de tu blog y te agrago! Esto último define el <em>target</em> del planeta.



[1] El paquete viene con buena documentación + la documentación embebida en el archivo de confuración que nos explica para que es cada variable que tenemos que llenar. <strong>BonusTrack</strong>: si tu hosting está en <a href="http://www.DreamHost.com">DreamHost</a> no dejés de leer: <a href="http://wiki.dreamhost.com/index.php/Planet">http://wiki.dreamhost.com/index.php/Planet</a>



Esto es para mi caso en particular pero también puede servirle a alguien:

</p><ul>

	<li><a href="http://blogs.firebirds.com.ar/planet.sh" target="_blank">planet.sh</a></li>

	<li><a href="http://blogs.firebirds.com.ar/fancy/config.ini">config.ini</a></li>

</ul></body></html>