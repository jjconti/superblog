<html><body><p>Hoy se llevó a cabo el octavo <a href="http://wiki.python.org/moin/PythonBugDay" title="PBD" target="_blank">Python Bug Day</a>. Sabía que era en estos días pero no lo tenía presente ni se me había ocurrido participar. Al mediodía <a href="http://www.taniquetil.com.ar/plog/" title="Facu" target="_blank">Facundo Batista</a> me lo recuerda por chat y me pregunto... ¿Por qué no? Puedo probar unas horas, ver que pasa, nunca compilé Python tal vez tenga que hacerlo para probar una solución.



Me dieron una lista de <a href="http://www.taniquetil.com.ar/cgi-bin/pytickets.py?nropag=0&amp;priority=0&amp;severity=0&amp;component=0&amp;version=0&amp;keyword=6" title="easy bugs" target="_blank">bugs fáciles</a>.  Y elejí este: <a href="http://bugs.python.org/issue1779" title="1779" target="_blank">1779</a>. El bug en particular podría haber sido resuelto en pocos minutos por un desaarrollador de Python. Es más, el mismo había sido reportado por el creador del lenguaje :D Pero como bien dice en uno de los comentarios, es un buen bug para el Python Bug Day. A un experto, resolverlo no le habría costado nada, pero tampoco le habría aportado nada. A un novato como a mi me sirvió para conocer algo del nucleo del lenguaje y el proceso que hay que seguir para resolver un bug:

</p><ol>

	<li>Bajar la última versión del código fuente</li>

	<li>Compilar</li>

	<li>Correr los tests para ver que todo ande bien</li>

	<li> Encontrar el bug y arreglarlo</li>

	<li>Correr los tests nuevamente</li>

	<li>Arreglar los tests que fallan</li>

	<li>Agregar tests que prueben el arreglo</li>

	<li>Correr los tests nuevamente</li>

	<li>Armar un parche</li>

	<li>Envair el parche</li>

</ol>

<!--more-->



El bug, que continuará en las versiones previas de Python pero ya está corregido en Python 3000, es el siguiente:

<code>

&gt;&gt;&gt; int("- 1")

-1

&gt;&gt;&gt; float("- 1")

Traceback (most recent call last):

File "&lt;stdin&gt;", line 1, in &lt;module&gt;

ValueError: invalid literal for float(): - 1

</code>

Cuando se quiere crear un número a partir de un string, no pueden haber espacios en blanco entre el signo (+ o -) y el número. El comportamiento correcto es el de la función <code>float</code>. El de <code>int</code> es errorneo. Necesita ser arreglado.



<strong>Obtener el código fuente</strong>



Bajé del servidor svn la última versión de Python 3000, la nueva versión del lenguaje, para el cual el bug estaba abierto:



<code>svn co http://svn.python.org/projects/python/branches/py3k/</code>



(Esto llevó bastante tiempo. Mientras tanto cociné y almorcé.)



<strong>Compilar</strong>



<code>cd py3k/</code>



./configure &amp;&amp; make



<strong>Correr el intérprete compilado</strong>



<code>./python</code>



<strong>Correr los tests</strong>



<code>make test</code>



o



<code>./python Lib/test/regrtest.py</code>



<strong>Arreglar el bug</strong>



En los comentarios sel bug se decía que era simple de resolver y que no consistía más que en comentar 2 líneas en un archivo en C.



Revisé el archivo <code>Objects/longobject.c</code> y luego de entender como funcionaba la función <code>PyLong_FromString(char *str, char **pend, int base)</code>, comenté las líneas 1688 y 1689. Problema resuelto!



Compilé para que mis cambios se vean reflejados.



<code>make</code>



Y probé en el intérprete.



<code>&gt;&gt;&gt; int("- 1")

Traceback (most recent call last):

File "&lt;stdin&gt;", line 1, in &lt;module&gt;

ValueError: invalid literal for int() with base 10: '- 1'</code>



Perfecto!



Luego corrí las pruebas afectadas por mi cambio y fallaron.



<code>./python Lib/test/test_builtin.py</code>



La función en particular era <code>test_int(self)</code>. Luego de una mirada rápida, comenté los valores de una lista que hacían fallar la prueba y pensé que con eso era suficiente. Consulté y me dijeron que también agregue mi cambio en Misc/NEWS. Lo hice. Lo siguiente era generar el parche.



<code>svn diff | tee bug_fix_for_1779.diff</code>



El mismo está en <a href="http://bugs.python.org/file9220" title="first patch" target="_blank">http://bugs.python.org/file9220</a>.



Luego lo vio Facundo y me dijo que tenía que tenía que agregar pruebas para mi parche. Me llevó bastante tiempo entender como funcionaba la prueba. Finalmente, luego de preguntar bastante conseguí el resultado deseado. Volví a generar un parche y a subirlo.



<code>svn diff | tee bug_fix_for_1779-plustests.diff</code>



<a href="http://bugs.python.org/file9228" title="patch2" target="_blank">http://bugs.python.org/file9228</a>



<strong>La experiencia</strong>



La verdad es que la experiencia fue muy buena. En unas 5 horas aprendí mucho sobre Python en si y sobre su ciclo de desarrollo, interactué con una comunidad despuesta a darte una mano cuando la necesitás y arreglé un error en el lenguaje que más uso. <em>Voilá!</em> Muchas gracias Comunidad de Python por organizar este Python Bug Day.</body></html>