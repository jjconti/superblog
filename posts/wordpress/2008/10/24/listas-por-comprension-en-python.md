<html><body><p>Las listas por comprensión o <a href="http://en.wikipedia.org/wiki/List_comprehension" target="_blank">list comprehension</a> es una característica muy práctica de Python (también incluida en <a href="http://en.wikipedia.org/wiki/Comparison_of_programming_languages_(list_comprehension)#JavaScript" target="_blank">otros lenguajes de programación</a>). Es una herramiente de mucha utilidad y fácil de usar, muchas veces desconocida por quienes vienen de lenguajes como PHP o Java.

Este artículo tiene como objetivo explorar su uso y plantear ejemplos para que los nuevos usuarios puedan incorporarlas rápidamente a su cajita de herramientas.



<!--more-->



Cómo lo indica el <a title="202" href="http://www.python.org/dev/peps/pep-0202/" target="_blank">PEP 202</a>, es una construcción sintáctica que permite crear listas en situaciones en las que se usaría map, filter o for anidados; pero de forma mas concisa.

</p><h2>map</h2>

Al llamar a la función map con argumentos f y l ,dónde f es una función y l una lista, retorna una lista con los resultados de aplicar f a cada elemento de l.

En el primer ejemplo usamos la función len, que dado un string retorna su longitud:

<pre>

&gt;&gt;&gt; len('hola')

4

</pre>

Esto es lo que sucede al aplicar map a todos los elementos de una lista de palabras:

<pre>

&gt;&gt;&gt; palabras = ['uno', 'dos', 'Santa Fe', 'Python', '...', 'Soleado']

&gt;&gt;&gt; map(len, palabras)

[3, 3, 8, 6, 3, 7]

</pre>

La versión equivalente es:

<pre>

&gt;&gt;&gt; [len(p) for p in palabras]

[3, 3, 8, 6, 3, 7]

</pre>

La sintaxis de la listas por comprensión es más flexible. Si queremos la lista de palabras, pero en mayúsculas hacemos:

<pre>

&gt;&gt;&gt; [p.upper() for p in palabras]

['UNO', 'DOS', 'SANTA FE', 'PYTHON', '...', 'SOLEADO']

</pre>

Para hacer lo anterior utilizando la función map, antes tendríamos que definir una función que llame al método upper de la clase string:

<pre>

&gt;&gt;&gt; def upper(s):

    return s.upper()

&gt;&gt;&gt; map(upper, palabras)

['UNO', 'DOS', 'SANTA FE', 'PYTHON', '...', 'SOLEADO']

</pre>

<h2>filter</h2>

La función filter recibe como argumento una función f y una lista l. Al igual que map, aplica f a todos los elementos de l pero retorna una lista con los elementos de l para los cuales la función f retornó True o un objeto con valor de verdad True.

<pre>

&gt;&gt;&gt; def incluye_n(s):

    return 'N' in s.upper()

&gt;&gt;&gt; incluye_n('Python')

True

&gt;&gt;&gt; incluye_n('Soleado')

False

&gt;&gt;&gt; filter(incluye_n, palabras)

['uno', 'Santa Fe', 'Python']

</pre>

La forma de hacer lo anterior con listas por comprensión es:

<pre>

&gt;&gt;&gt; [p for p in palabras if incluye_n(p)]

['uno', 'Santa Fe', 'Python']

</pre>

Incluso muchas veces podemos hacerlo sin necesitar de definir una función auxiliar:

<pre>

&gt;&gt;&gt; [p for p in palabras if 'N' in p.upper()]

['uno', 'Santa Fe', 'Python']

</pre>

<h2>for</h2>

También podemos anidar fors de forma similar a cómo lo haríamos en:

<pre>

&gt;&gt;&gt; range(6)

[0, 1, 2, 3, 4, 5]

&gt;&gt;&gt; for n in range(6):

for p in palabras:

    if len(p) == n:

        print p,n

uno 3

dos 3

... 3

</pre>

Pero con una sintaxis más cómoda:

<pre>

&gt;&gt;&gt; [(p,n) for n in range(6) for p in palabras]

[('uno', 0), ('dos', 0), ('Santa Fe', 0), ('Python', 0), ('...', 0), ('Soleado', 0), ('uno', 1), ('dos', 1), ('Santa Fe', 1), ('Python', 1), ('...', 1), ('Soleado', 1), ('uno', 2), ('dos', 2), ('Santa Fe', 2), ('Python', 2), ('...', 2), ('Soleado', 2), ('uno', 3), ('dos', 3), ('Santa Fe', 3), ('Python', 3), ('...', 3), ('Soleado', 3), ('uno', 4), ('dos', 4), ('Santa Fe', 4), ('Python', 4), ('...', 4), ('Soleado', 4), ('uno', 5), ('dos', 5), ('Santa Fe', 5), ('Python', 5), ('...', 5), ('Soleado', 5)]

&gt;&gt;&gt; [(p,n) for n in range(6) for p in palabras if len(p) == n]

[('uno', 3), ('dos', 3), ('...', 3)]

</pre></body></html>