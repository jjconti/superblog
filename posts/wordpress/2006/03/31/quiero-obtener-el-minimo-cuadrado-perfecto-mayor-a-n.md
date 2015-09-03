<html><body><p>Programando mi generador de constelaciones llegué a este problema:



<em>Obtener el mínimo cuadrado perfecto mayor a n (con n 



¿Cómo hubiese sido la forma iterativa de hacerlo?

<pre>

&gt;&gt;&gt; def min_perf_sqrt(n):

...    i = s = 1

...    while (s 

Este es mi one-liner hecho en python con un toque de programación funcional:

<pre>

min(filter(lambda i: i &gt; n, map(lambda j: j*j, range(13))))

</pre>



Mmm probablemente la versión iterativa sea más eficiente.. programadores? comentarios?</pre></em></p></body></html>