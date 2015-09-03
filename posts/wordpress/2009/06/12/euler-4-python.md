<html><body><h2>Enunciado 4</h2>

Un número palíndromo se lee igual en ambos sentidos. El mayor palíndromo construido a partir del producto de dos números de dos dígitos es 9009 = 91 × 99.



Encontrar el mayor palíndromo que se puede construir como el producto de dos números de tres dígitos.

<h2>Solución</h2>

La solución fue obtenida en el intérprete interactivo de Python 3.0rc1+. Necesitaba Python 3 para utilizar itertools.combinations:

<pre>

juanjo@fenix:~$ python3

Python 3.0rc1+ (py3k, Oct 28 2008, 09:23:29) 

[GCC 4.3.2] on linux2

Type "help", "copyright", "credits" or "license" for more information.

&gt;&gt;&gt; from itertools import combinations

&gt;&gt;&gt; tri = range(999, 99, -1)

&gt;&gt;&gt; mults = []

&gt;&gt;&gt; for a,b in combinations(tri, 2):

...     s = str(a*b)

...     if s == s[::-1]:

...             mults.append(int(s))

... 

&gt;&gt;&gt; max(mults)

906609

</pre>

<h2>Python tips</h2>

<ul>

	<li><code>combinations</code> genera la combinación con los elementos de la lista argumento tomados de a n, si se especifica el parámetro n.</li>

	<li>En Python 3 <code>print</code> deja de ser una sentencia para convertirse en una función, por lo que siempre debe ser llamado con parámetros.</li>

	<li><code>unString[::-1]</code> es un <em>idiom</em> usado para invertir una cadena de texto (en el ejemplo, <code>unString</code>). Se lee: los elementos de unString, desde el principio al final, con paso -1.</li>

</ul></body></html>