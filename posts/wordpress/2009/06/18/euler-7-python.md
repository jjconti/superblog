<html><body><h2>Enunciado 7</h2>

Listando los primeros seis números primos: 2, 3, 5, 7, 11,y 13, podemos ver que el 6° primo es el 13.



¿Cuál es el 10001° primo?

<h2>Solución</h2>

La solución fue obtenida en el intérprete interactivo de Python 2.5.2:

<pre>&gt;&gt;&gt; from math import sqrt

&gt;&gt;&gt; def primo(n):

...     for i in xrange(2,int(sqrt(n))+1):

...         if n % i == 0:

...             return False

...     return True

&gt;&gt;&gt; a = 2

&gt;&gt;&gt; i = 1

&gt;&gt;&gt; while i &lt; 10002:

...     if primo(a):

...             i +=1

...     a += 1

...

&gt;&gt;&gt; i

10002

&gt;&gt;&gt; a

104744

&gt;&gt;&gt; a-1

104743</pre></body></html>