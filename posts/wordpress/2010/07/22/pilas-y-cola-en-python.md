<html><body><p>La forma más directa de tener pilas y colas en Python es usando listas, una de las poderosas estructuras de datos que vienen con el lenguaje.



Una pila es una estructura de datos secuencial en la que el último elemento insertado es el primero en retirarse (<a href="http://es.wikipedia.org/wiki/Pila_%28estructura_de_datos%29" target="_blank">LIFO</a>) y puede implementarse directamente con los métodos <code>append</code> y <code>pop</code>.



Una operación común en las pilas es top, que devuelve el elemento en el tope de la pila, pero sin quitarlo; esta operación se puede emular indexando por -1.



</p><pre>&gt;&gt;&gt; pila = [6,7,8]

&gt;&gt;&gt; pila.append(9)

&gt;&gt;&gt; pila

[6, 7, 8, 9]

&gt;&gt;&gt; pila.pop()

9

&gt;&gt;&gt; pila.pop()

8

&gt;&gt;&gt; pila[-1]

7</pre>



Implementar una cola requiere algo más. En las colas, a diferencia de las pilas, el primer valor insertado es el primero en quitarse (<a href="http://es.wikipedia.org/wiki/Cola_%28estructura_de_datos%29" target="_blank">FIFO</a>).



Un primer intento es implementarla con <code>append</code> y <code>pop(0)</code> que obtiene el primer elemento (o con <code>insert</code> insertando al principio y <code>pop</code>). Pero las listas de Python, si bien están optimizadas para insertar al final y quitar del final, no lo están para insertar al principio o quitar del principio. La solución es utilizar <a href="http://docs.python.org/library/collections.html#collections.deque" target="_blank"><code>collections.deque</code></a> que si está implementada con estas operaciones optimizadas.



<pre>&gt;&gt;&gt; from collections import deque

&gt;&gt;&gt; cola = deque([1,2,3])

&gt;&gt;&gt; cola.append(4)

&gt;&gt;&gt; cola

deque([1, 2, 3, 4])

&gt;&gt;&gt; cola.popleft()

1

&gt;&gt;&gt; cola.popleft()

2

&gt;&gt;&gt; cola

deque([3, 4])

</pre></body></html>