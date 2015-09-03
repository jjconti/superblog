<html><body><a title="Euler" href="http://projecteuler.net/" target="_blank">Project Euler</a> es un sitio web que reta a los programadores a resolver problemas matemáticos mediante código. Me parece entretenido. Voy a ir resolviendo problemas y posteando mi solución en Python acompañada de comentarios sobre el código que puedan servirles a quienes están empezando a aprender el lenguaje.

<h2>Enunciado 1</h2>

Si listamos todos los números menores a 10 que son múltiplos de 3 o 5, obtenemos 3, 5, 6 y 9. La suma de esos múltiplos es 23.



Encontrar la suma de todos los múltiplos de 3 o 5 menores a 1000.

<h2>Solución</h2>

La solución fue obtenida en el intérprete interactivo de Python 2.5.2:

<pre>&gt;&gt;&gt; def mults(n=10):

...     r = []

...     for i in range(1, n):

...             if i % 3 == 0:

...                     r.append(i)

...             elif i % 5 == 0:

...                     r.append(i)

...     return r

...

&gt;&gt;&gt; mults()

[3, 5, 6, 9]

&gt;&gt;&gt; sum(mults())

23

&gt;&gt;&gt; sum(mults(n=1000))

233168</pre>

<h2>Python tips</h2>

<ul>

	<li>En la definición de la función <code>mults</code> se incluye un argumento por defecto <code>n</code> con valor <code>10</code>. Cuando más adelante se llama a esta función sin parámetros, <code>n</code> toma el valor por defecto.</li>

	<li>La función <code>range</code>, incluida en el lenguaje devuelve una lista de números sobre la que se puede iterar. Muy útil para usar con la estructura <code>for</code>. Más información haciendo <code>help(range)</code> en el intérprete interactivo.</li>

</ul></body></html>