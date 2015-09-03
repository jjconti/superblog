<html><body><p>Este año en una de las clases de Comunicaciones expliqué cómo instalar Savi. <a title="Savi Home" href="http://savi.sourceforge.net/" target="_self">Savi</a> es un visualizador de <a title="Wikipedia en inglés" href="http://en.wikipedia.org/wiki/Satellite_constellation" target="_self">constelaciones de satélites</a>. Permite simular las órbitas y coberturas de satélites en 2 y 3 dimensiones. Puede simular constelaciones como <a title="Iridium" href="http://www.ee.surrey.ac.uk/Personal/L.Wood/constellations/iridium.html" target="_blank">Iridium</a> o <a title="Globalstar" href="http://www.ee.surrey.ac.uk/Personal/L.Wood/constellations/globalstar.html" target="_blank">Globalstar</a> entre muchas otras.<!--more-->



Los pasos que seguí para realizar la instalación en GNU/Linux (Ubuntu) fueron:

</p><ol>

	<li>Descargar el paquete de la <a title="Savi Home" href="http://savi.sourceforge.net/" target="_blank">página principal</a> (1.3.2 en su momento).</li>

	<li>Instalar los paquetes tcl8.4-dev y tk8.4-dev (contienen los <em>headers</em> necesarios para la compilación).</li>

	<li>Revisar el archivo <code>src/Makefile</code> (para saber cómo se realizará la compilación).</li>

	<li>Instalar el paquete motif-client o lesstif (usados en la GUI).</li>

	<li>Instalar geomview (software utilizando para la visualización 3D de la simulación, Ubuntu tenía un paquete para el mismo).</li>

	<li>Ejecutar el comando <code>make ARCH=debian</code></li>

</ol>

Eso es todo, luego del proceso (si no hay errores) se obtiene el ejecutable <code>savi</code>.



En Windows los pasos son similares (también se requiere compilar el software), las principales diferencias en el proceso son:

<ol>

	<li>Se necesita tener instalado Cygwin (un entorno Unix sobre Windows): <a title="Cygwin" href="http://info.ee.surrey.ac.uk/Personal/L.Wood/software/SaVi/building-under-Windows/" target="_blank">instrucciones</a>.</li>

	<li>El comando make a ejecutar será <code>make ARCH=cygwin</code></li>

</ol>

En ambos casos para ejecutar Savi con Geomview hay que pasarle al ejecutable geomview el ejecutable savi como argumento, por ejemplo:



<code>$ geomview savi </code>desde la línea de comandos.



Algunos ejemplos visuales:



<a href="/wp-content/uploads/2008/08/iridium.png"><img class="size-medium wp-image-533" title="iridium" src="/wp-content/uploads/2008/08/iridium-300x187.png" alt="Iridium" width="300" height="187"></a>



<a href="/wp-content/uploads/2008/08/sirius.png"><img class="size-medium wp-image-534" title="sirius" src="/wp-content/uploads/2008/08/sirius-300x187.png" alt="Sirius" width="300" height="187"></a></body></html>