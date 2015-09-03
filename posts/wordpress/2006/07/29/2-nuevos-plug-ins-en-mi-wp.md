<html><body><p>Hoy agregé dos plug-ins en mi instación de <a href="http://www.wordpress.org">WordPress</a> (el sistema que uso como blog).



</p><h3>Estadísticas de visitantes</h3>

Hace un tiempo tenía instalado un sistema de estadísticas llamado.. bueno no recuerdo como se llamaba, pero no importa por que era bastante malo. Hoy leyendo en el <a href="http://www.cesarsandrigo.com.ar/">blog de César M. Sandrigo</a> descubrí otro y tal vez mi búsqueda (casi abandonada) de una buena forma de conocer sobre mis visitantes haya llegado por fin a Ítaca. El plug-in se llama <a href="http://www.deltablog.com/2005/10/05/wordpress-plugin-popstats/">PopStats</a>.



<h3>Votar los artículos</h3>

Desde hoy, abajo de cada artículo, hay 5 estrellitas con las que los visitantes pueden rankear los <em>posts</em> publicados. La verdad, está muy lindo: <a href="http://blog.abusemagazine.com/index.php/2006/01/28/wordpress-plugin-post-star-rating/">Post Star Rating</a>.



Cuando dejé mi primer voto me pareció gracioso leer "1 votos" :) Luego pensé que no debería ser difícil de corregir, acá está la receta:



Hay que hacer un pequeño cambio en dos métodos de la clase PSR (<a href="http://dev.wp-plugins.org/file/post-star-rating/trunk/psr.class.php">psr.class.php</a>). Tanto en <code>_drawStars($votes, $points)</code> como en <code>_drawVotingStars($votes, $points)</code> cambiar <code>__('votos')</code> por <code>__($votes == 1 ? 'voto' : 'votos')</code>.



En la misma clase también se puede cambir el texto que se muestra.



Otro detallecito que encontré fué que el texto que acompaña a las estrellitas, por ejemplo "2 votos" se veía cortado abajo, revisando el código fuente de la clase anterior encontré el método <code>css()</code> que le da el estilo; en una parte decía:

               <code><pre> .PSR_stars {

                  height: 15px;

                  overflow: hidden;

                  padding: 0;

                  margin: 0;

                }</pre></code>



PSR_starts es la clase del div que contiene a las estrellitas y el texto. Simplemente comenté el límite impuesto a la altura:



               <code><pre> .PSR_stars {

                  /*height: 15px;*/

                  overflow: hidden;

                  padding: 0;

                  margin: 0;

                }</pre></code>

Seguro que a más de uno le sirve!



Saludos!</body></html>