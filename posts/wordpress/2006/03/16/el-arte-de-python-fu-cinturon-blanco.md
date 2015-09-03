<html><body><p>Como parte de mi aprendizaje del lenguaje de programación <a title="Aprendiendo Python" href="http://firebirds.com.ar/~juanjo/wordpress/?cat=7">Python</a> y por la necesidad de generar automáticamente algunos dibujos, incurcioné en el milenario arte del Python-Fu.



Si querés conocer más sobre este acestral arte, seguí leyendo..



<!--more--> Script-Fu (un dialecto de Scheme) es el lenguaje original (además de C) utilizado para escribir plug-ins para <a target="_blank" title="Gimp web site" href="http://www.gimp.org">Gimp</a> (The GNU Image Manipulation Program). Actualmente se pueden escribir plug-ins en otros lenguajes como Perl, Tcl y.. Python



<strong>¿qué hay que tener instalado?</strong>

</p><ul>

	<li>python (<code>apt-get install python</code> en Debian GNU/Linux)</li>

	<li>gimp (<code>apt-get install gimp</code>)</li>

	<li>pygimp (<code>apt-get install gimp-python</code>)</li>

</ul>

Los dos primeros programas suelen estar instalados en la mayoría de las instalaciones de GNU/Linux, el último no. Una verificación rápida puede hacerse ejecutando gimp y buscando la opción Python-Fu en el menú Exts.



<strong>Script-Fu</strong>



En <a title="Estructura de un python-fu (en)" target="_blank" href="http://www.jamesh.id.au/software/pygimp/structure-of-plugin.html">http://www.jamesh.id.au/software/pygimp/structure-of-plugin.html</a> se puede ver la estructura de un Script-Fu.



Cuando gimp es ejecutado, busca los archivos ejecutables que se encuentran en <code>$HOME/.gimp-x-y/plug-ins/</code>. En el caso de los scripts en python, la función register() es ejecutada y cuando se acceda al plug-in mediante el menú especificado se ejecutará su función principal. Antención a esto: los archivos deben ser tener encendido el bit de ejecución (<code>chmod +x hello-world.py</code>).



Otro tip: si algo no funciona como se espera, una forma de enterarse que pasó es ejecutar gimp desde una terminal (<code>gimp --verbose</code>) y leer en esta las distintas salidas que produce el programa (allí se van a escribir los errores que se produzcan en tiempo de ejecución).



<strong>Links útiles</strong>

<ul>

	<li><a href="http://www.jamesh.id.au/software/pygimp/">http://www.jamesh.id.au/software/pygimp/</a>: documentación sobre gimp-python.</li>

	<li><a href="http://carol.gimp.org">Carol at Gimp.org</a>: muchos scripts que pueden servir de ejemplo, a mi me sirvió leer algunos antes de lanzarme a escribir el mío.</li>

</ul>

<em><strong>[update: a pedido del público: hello-world.py]</strong></em>



Pueden bajar <a title="Hello-World.py" href="../../../../files/python/hello-world.py.html">hello-world.py</a> para ver un ejemplo sencillo. Debería generar una imagen como esta:<img align="top" alt="Hello World" id="image46" title="Hello World" src="http://firebirds.com.ar/%7Ejuanjo/wordpress/wp-content/uploads/2006/03/hello.jpg">salvo que cambien los parámetros ;-)</body></html>