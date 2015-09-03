<html><body><h2>Enunciado 3</h2>

Los factores primos de 13195 son 5, 7, 13 y 29.



¿Cual es el mayor factor primo del número 600851475143?

<h2>Solución</h2>

La solución fue obtenida en el intérprete interactivo de Python 2.5.2:

<pre>&gt;&gt;&gt; from math import sqrt

&gt;&gt;&gt; the_number = 600851475143

&gt;&gt;&gt; my_number = sqrt(the_number)

&gt;&gt;&gt; my_number

775146.09922452678

&gt;&gt;&gt; my_number = int(my_number)

&gt;&gt;&gt; my_number

775146

&gt;&gt;&gt; def esprimo(n):

...     for i in xrange(2,int(sqrt(n))+1):

...             if n % i == 0:

...                     return False

...     return True

...

&gt;&gt;&gt; esprimo(8)

False

&gt;&gt;&gt; esprimo(3)

True

&gt;&gt;&gt; esprimo(6823)

True

&gt;&gt;&gt; esprimo(100109)

True

&gt;&gt;&gt; esprimo(100110)

False

&gt;&gt;&gt; for i in xrange(1, my_number+1):

...      if the_number % i == 0 and esprimo(i):

...             print i

...

1

71

839

1471

6857</pre>

<h2>Python tips</h2>

<ul>

	<li><code>xrange</code>, en lugar de crear una lista entera de números como hace <code>range</code> devuelve un generador que va entregando números a medida que los necesitamos.</li>

	<li>La clase <code>int</code> se instancia para obtener enteros. Si la llamamos con un float como parámetro, podemos usarla para forzar un entero.</li>

</ul></body></html>