<html><body><h2>Enunciado 2</h2>

Cada nuevo item en la secuencia de Fibonacci es generado sumando los dos términos previos. Empezando con 1 y 2, los primeros 10 términos serían:



1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...



Encontrar la suma de todos los términos pares en la secuencia que no supera los 4 millones.

<h2>Solución</h2>

La solución fue obtenida en el intérprete interactivo de Python 2.5.2:

<pre>&gt;&gt;&gt; MAX = 4000000

&gt;&gt;&gt; def evsum(n):

...     s = 0

...     a,b = 1,2

...     while True:

...         if a &gt;= n:

...             break

...         if a % 2 ==0:

...             print a, " ",

...             s += a

...         a,b = b,a+b

...     return s

...

&gt;&gt;&gt; evsum(MAX)

2   8   34   144   610   2584   10946   46368   196418   832040   3524578

4613732</pre>

<h2>Python tips</h2>

<ul>

	<li>La asignación múltiple es un idom muy cómodo: <code>a,b = 1,2</code></li>

	<li>Si agregamos una coma final a la enumeración de objetos a ser impresos con <code>print</code>, se logra el efecto de que no se imprima el salto de línea (<code>\n</code>) final.</li>

</ul></body></html>