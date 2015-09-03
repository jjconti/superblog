<html><body><p>El módulo <code>random</code> de <a href="http://www.python.org">Python</a> tiene varias funciones muy útiles.

</p><pre>&gt;&gt;&gt; import random</pre>

Cómo <code>choice</code>, que permite elegir un elemento al asar de una secuencia:

<pre>&gt;&gt;&gt; lista = [1, 2, 3, "hola", 'q', '$', 0]

&gt;&gt;&gt; random.choice(lista)

1

&gt;&gt;&gt; random.choice(lista)

0

&gt;&gt;&gt; random.choice(lista)

3

&gt;&gt;&gt; random.choice(lista)

'q'

&gt;&gt;&gt; random.choice("Esta es una oración muy interesante")

'E'

&gt;&gt;&gt; random.choice((1,2,3,4))

3

</pre>

O <code>shuffle</code>, que desordena una lista (<em>in place</em>, es decir que no retorna una lista desordenada sino que la misma es desordenada):

<pre>&gt;&gt;&gt; random.shuffle(lista)

&gt;&gt;&gt; lista

[3, 1, 0, 'hola', '$', 'q', 2]

&gt;&gt;&gt; texto = "Esto es una pruba con SHUFFLE"

&gt;&gt;&gt; random.shuffle(texto)

Traceback (most recent call last):

File "&lt;stdin&gt;", line 1, in ?

File "/usr/lib/python2.4/random.py", line 262, in shuffle

x[i], x[j] = x[j], x[i]

TypeError: object does not support item assignment</pre>

Obviamente ni a tuplas ni a strings se puede aplicar esta función ya que esos dos tipos de datos son inmutables.

<!--more-->

Me encontraba yo programando y se me ocurrió que podría desordenar (shuffle) un diccionario para lograr cierto efecto. ¿Cual sería la semántica de esto? Seguro se entenderá mejor con un ejemplo, dado el diccionario:

<pre>{0 : "cero", 1 : "uno", 2 : "dos"}</pre>

que tiene números como claves y strings como valores, luego de que se le aplique la función shuffle

<pre>random.shuffle(dicc)</pre>

Se obtendría por ejemplo:

<pre>{0 : "uno", 1 : "dos", 2 : "cero"}</pre>

Bien, probémoslo en el REPL de Python:

<pre>&gt;&gt;&gt; from random import shuffle

&gt;&gt;&gt; lista = [1,2,3,4,5,6,7,8]

&gt;&gt;&gt; shuffle(lista)

&gt;&gt;&gt; lista

[4, 1, 7, 8, 6, 2, 5, 3]

&gt;&gt;&gt; dicc = {}

&gt;&gt;&gt; for a in range(8):

dicc[a] = a

&gt;&gt;&gt; dicc

{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}

&gt;&gt;&gt; shuffle(dicc)

&gt;&gt;&gt; dicc

{0: 1, 1: 4, 2: 7, 3: 6, 4: 2, 5: 5, 6: 3, 7: 0}

</pre>

Mmm, parece que funciona. ¿Qué dicen uds? El del último ejemplo no es en realidad el diccionario que uso en mi programa, sino que es más bien algo así:

<pre>&gt;&gt;&gt; dicc = {(1,1): "primero", (1,2): "segundo", (2,2): "otro"}</pre>

Intentamos mezclarlo y..

<pre>&gt;&gt;&gt; shuffle(dicc)

Traceback (most recent call last):

File "&lt;stdin&gt;", line 1, in ?

File "/usr/lib/python2.4/random.py", line 262, in shuffle

x[i], x[j] = x[j], x[i]

KeyError: 2</pre>

¿Qué pasó? La respuesta a este raro comportamiento está en el código mismo de Python, en el módulo <code>random</code>. En mi instalación de Python2.4 en Debian GNU/Linux lo encontramos en: <code>/usr/lib/python2.4/random.py</code>

<pre>def shuffle(self, x, random=None, int=int):

"""x, random=random.random -&gt; shuffle list x in place; return None.



Optional arg random is a 0-argument function returning a random

float in [0.0, 1.0); by default, the standard random.random.

"""



	if random is None:

		random = self.random

	for i in reversed(xrange(1, len(x))):

	# pick an element in x[:i+1] with which to exchange x[i]

		j = int(random() * (i+1))

		x[i], x[j] = x[j], x[i]</pre>

Sólo de ver la implementación se nota que solo funcionará con listas. La siguiente es mi alternativa, una función <code>shuffle_dict</code> que sirve para mezclar los elementos de un diccionario:

<pre>from random import choice



def shuffle_dict(d):

"""Shuffle the d dict."""

	for i in d.keys():

		k = d.keys()

		k.remove(i)

		j = choice(k)

		d[i], d[j] = d[j], d[i]

</pre></body></html>