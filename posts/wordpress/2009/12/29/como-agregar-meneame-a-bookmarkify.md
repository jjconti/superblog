<html><body><a href="http://www.gara.com/projects/bookmarkify/" target="_blank">Bookmarkify</a> es un popular plugin para Wordpress y script PHP que permite agregar a un sitio web una botonera que posibilite a un visitánte rápidamente compartir el contenido que está leyendo mediante las redes sociales más pupulares (Twitter, Facebook, Digg, Reddit, ...).



Lamentablemente no posee la posibilidad de incluir a <a href="http://meneame.net" target="_blank">Menéame</a>, el sitio web para compartir contenidos más popular en español.



Para añadirlo, se debe editar la función get getBookmarkifyLinks en el archivo bookmarkify.php de la distribución del plugin para añadir, en algún lugar entre <code>$i=0;</code> y return $links; la siguiente línea:



<code>$links[$i++] = array("Meneame!", "Publicar en Meneame!", "http://meneame.net/submit.php?url=$u&amp;title=$t", "meneame.ico", 0, 0);</code>



y guardar el archivo http://meneame.net/favicon.ico como meneame.ico en la carpeta del plugin.</body></html>