<html><body><p>El ejemplo consiste en un plano de 800x600 puntos con el punto (0,0)  en la esquina superior izquierda. En el plano hay puntos y figuras (formadas por puntos). Uno de los puntos es el origen y otro el destino. El problema a resolver es encontrar el camino más corto desde el origen al destino moviéndose de punto a punto y sin pasar sobre una figura.



La heurística utilizada es la distancia en línea recta desde la posición actual a la posición del objetivo. <!--more-->

</p><h2>Instalación y uso</h2>

Teniendo Python y <a title="PyGame" href="http://www.pygame.org" target="_blank">PyGame</a> instalados, obtener el código fuente:



<code>svn co http://svn.juanjoconti.com.ar/astar/tags/astar-only/ astar</code>



y dentro de la carpeta <code>astar</code> ejecutar gui.py:



<code>cd astar

python gui.py</code>



El primer click que se haga marcará el punto origen (verde) y el segundo el punto destino (rojo).

<p style="text-align: center;"><a href="/wp-content/uploads/2008/10/apasp1.png"><img class="aligncenter size-medium wp-image-617" title="paso 1" src="/wp-content/uploads/2008/10/apasp1-300x232.png" alt="" width="300" height="232"></a></p>



Luego se pueden agregar tantos puntos sueltos o figuras como se quieran. Si se hace uno o dos clicks y luego se aprieta la barra espaciado, uno o dos puntos son añadidos al planto. Si se hacen más de dos clicks antes de apretar la barra espaciadora, entonces una figura formada por los puntos marcados es añadida.



<a href="/wp-content/uploads/2008/10/apaso2.png"><img class="aligncenter size-medium wp-image-620" title="paso2" src="/wp-content/uploads/2008/10/apaso2-300x232.png" alt="" width="300" height="232"></a>



<a href="/wp-content/uploads/2008/10/apaso3.png"><img class="aligncenter size-medium wp-image-619" title="paso3" src="/wp-content/uploads/2008/10/apaso3-300x232.png" alt="" width="300" height="232"></a>



Se siguen cargando tantos puntos y figuras como se quiera. Finalmente, al aprender Enter se ejecuta el algoritmo de búsqueda y si se encuentra un camino-solución, este es graficado.



<a href="/wp-content/uploads/2008/10/apaso5.png"><img class="aligncenter size-medium wp-image-618" title="resultado1" src="/wp-content/uploads/2008/10/apaso5-300x232.png" alt="" width="300" height="232"></a>

<p align="center"></p>



Otros casos de prueba:



<a href="/wp-content/uploads/2008/10/a2.png"><img class="aligncenter size-medium wp-image-614" title="resultado2" src="/wp-content/uploads/2008/10/a2-300x232.png" alt="" width="300" height="232"></a>



<a href="/wp-content/uploads/2008/10/a3.png"><img class="aligncenter size-medium wp-image-615" title="resultado3" src="/wp-content/uploads/2008/10/a3-300x232.png" alt="" width="300" height="232"></a>



<a href="/wp-content/uploads/2008/10/a6.png"><img class="aligncenter size-medium wp-image-616" title="resultado4" src="/wp-content/uploads/2008/10/a6-300x232.png" alt="" width="300" height="232"></a>



<a href="/wp-content/uploads/2008/10/a1.png"><img class="aligncenter size-medium wp-image-613" title="resultado5" src="/wp-content/uploads/2008/10/a1-300x232.png" alt="" width="300" height="232"></a>

<h2>Teoría relacionada</h2>

<ul>

	<li><a href="http://es.wikipedia.org/wiki/Algoritmo_de_b%C3%BAsqueda_A*" target="_self">Estrategia de búsqueda A*</a></li>

	<li><a title="AIMA" href="http://aima.cs.berkeley.edu/" target="_self">Inteligencia artificial, un enfoque moderno</a></li>

</ul></body></html>