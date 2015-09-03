<html><body><p>Extendí <a title="Un ejemplo de A*" href="http://www.juanjoconti.com.ar/2008/10/07/un-ejemplo-de-busqueda-a/" target="_blank">mi ejercicio de A*</a> para que además busque la solución utilizando Avara y las compare gráficamente.

Avara es otro algoritmo de búsqueda, pero a diferencia de A* no es ni óptimo ni completo. Ambos utilizan una heurística para estimar el costo de un estado n al estado objetivo y por esto se dice que son <strong>métodos informados</strong>.



La diferencia  radica en cómo seleccionan nodos para su expansión: mientras que A* siempre elije  el nodo que minimice la función <strong>camino recorrido + estimación al objetivo</strong>, Avara simplemente elije el nodo con menor <strong>estimación al objetivo</strong> (no tiene en cuenta el camino previo).<!--more-->



Hay escenarios en los que ambas estrategias encontrarán el mismo camino:



<a href="/wp-content/uploads/2008/10/avsavara-iguales.png"><img class="aligncenter size-full wp-image-679" title="avsavara-iguales" src="/wp-content/uploads/2008/10/avsavara-iguales.png" alt="" width="500" height="388"></a>

Pero hay otros en los que no:



<a href="/wp-content/uploads/2008/10/avsavara5.png"><img class="aligncenter size-full wp-image-678" title="avsavara5" src="/wp-content/uploads/2008/10/avsavara5.png" alt="" width="500" height="388"></a>



<a href="/wp-content/uploads/2008/10/avsavara4.png"><img class="aligncenter size-full wp-image-677" title="avsavara4" src="/wp-content/uploads/2008/10/avsavara4.png" alt="" width="500" height="388"></a>



<a href="/wp-content/uploads/2008/10/avsavara3.png"><img class="aligncenter size-full wp-image-676" title="avsavara3" src="/wp-content/uploads/2008/10/avsavara3.png" alt="" width="500" height="388"></a>



<a href="/wp-content/uploads/2008/10/avsavara2.png"><img class="aligncenter size-full wp-image-675" title="avsavara2" src="/wp-content/uploads/2008/10/avsavara2.png" alt="" width="500" height="388"></a>



<a href="/wp-content/uploads/2008/10/avsavara.png"><img class="aligncenter size-full wp-image-674" title="avsavara" src="/wp-content/uploads/2008/10/avsavara.png" alt="" width="500" height="388"></a>

</p><h2>Instalación y uso</h2>

Similar al ejemplo anterior. Teniendo Python y <a title="PyGame" href="http://www.pygame.org/" target="_blank">PyGame</a> instalados, obtener el código fuente:



<code>svn co http://svn.juanjoconti.com.ar/astar/tags/astar-vs-avara/ astar-vs-avara</code>



y dentro de la carpeta <code>astar</code>-vs-avara ejecutar gui.py:



<code>cd astar-vs-avara

python gui.py</code></body></html>