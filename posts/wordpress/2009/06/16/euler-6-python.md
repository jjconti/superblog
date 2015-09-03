<html><body><h2>Enunciado 6</h2>

La suma de los cuadrados de los primeros diez números naturales es:

<div style="text-align: center;">1<sup>2</sup> + 2<sup>2</sup> + ... + 10<sup>2</sup> = 385</div>

El cuadrado de la suma de los primeros diez números naturales es:

<div style="text-align: center;">(1 + 2 + ... + 10)<sup>2</sup> = 55<sup>2</sup> = 3025</div>

Así que la diferencia entre la suma de los cuadrados de los diez primeros números naturales y el cuadrado de la suma es 3025 − 385 = 2640.



Encontrar la diferencia entre la suma de los cuadrados de los primeros cien números naturales y el cuadrado de la suma.

<h2>Solución</h2>

La solución fue obtenida utilizando el intérprete interactivo de Python 2.5.2:

<pre>&gt;&gt;&gt; def a(n):

...     s = sum(xrange(1,n+1))

...     a1 = s ** 2

...     a2 = sum([x**2 for x in xrange(1,n+1)])

...     return a1, a2, a1-a2

...

&gt;&gt;&gt; a(10)

(3025, 385, 2640)

&gt;&gt;&gt; a(100)

(25502500, 338350, 25164150)</pre>

<h2>Python tips</h2>

<ul>

	<li>Con ** podemos elevar un número a cualquier potencia sin necesidad de importar ningún módulo.</li>

	<li>Para denotar una tupla solo hacen falta las comas (,), no los paréntesis al principio y al final.</li>

</ul></body></html>