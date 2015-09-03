<html><body><p>Cuando estaba preparando mi <a href="http://www.juanjoconti.com.ar/2009/10/21/charla-bienvenido-a-python-en-instituto-libre-09" target="_blank">charla introductoria a Python</a>, le pasé mis slides a un amigo para que me diga su opinión y una de las cosas que me dijo fue

</p><blockquote>Nunca senti que set sea algo nativo de python, le daria mas importancia a los diccionarios, aunque tal vez tu publico este mas interesado en sets, no lo se.</blockquote>

Me sorprendió el comentario. Para mi, set es un tipo de dato muy útil y poderoso. En este post voy a intentar hacer una apología de set, el tipo de dato que incorpora Python para representar la noción matemática de conjunto.

<!--more-->

<h2>Presentación</h2>

Un objeto set es una colección sin orden de objetos <a href="http://docs.python.org/glossary.html#term-hashable" target="_blank"><em>hasheables</em></a>. Puede contener objetos de todos los tipos inmutables de Python, pero no los contenedores mutables como listas. También puede contener objetos de clases definidas por el usuario (Los objetos instancias de clases definidas por el usuario son por defecto hasheables.).

Los conjuntos se pueden crear, por ejemplo, a partir de una lista. Podemos quitar elementos (al azar o uno en concreto) o agregarlos:

<pre>&gt;&gt;&gt; heladera = ['huevo', 'huevo', 'queso', 'leche', 'pera', 'pera', 'pera']

&gt;&gt;&gt; alimentos = set(heladera)

&gt;&gt;&gt; alimentos

set(['queso', 'leche', 'huevo', 'pera'])

&gt;&gt;&gt; alimentos.pop()

'queso'

&gt;&gt;&gt; alimentos.remove('leche')

&gt;&gt;&gt; alimentos

set(['huevo', 'pera'])

&gt;&gt;&gt; alimentos.add('empanada')

&gt;&gt;&gt; alimentos

set(['empanada', 'huevo', 'pera'])</pre>

<h2>Prueba de pertenencia</h2>

Otra función muy común y útil es probar la pertenencia de objetos al conjunto:

<pre>&gt;&gt;&gt; 'empanada' in alimentos

True

&gt;&gt;&gt; 'leche' in alimentos

False

&gt;&gt;&gt; 'leche' not in alimentos

True

</pre>

<h2>Iterar sobre conjuntos</h2>

Podemos interar sobre conjuntos de la misma forma que lo hacemos sobre listas:

<pre>&gt;&gt;&gt; for a in alimentos:

...     "Debo comer " + a

...

'Debo comer empanada'

'Debo comer huevo'

'Debo comer pera'

</pre>

<h2>Operaciones sobre conjuntos</h2>

Los conjuntos en Python soportan las operaciones típicas de conjuntos: restas, intersección, unión y diferencia simétrica (los elementos que están en uno de los conjuntos, pero no en ambos). <a href="http://es.wikipedia.org/wiki/Teor%C3%ADa_de_conjuntos#Operaciones_con_conjuntos">Repasar operaciones con conjuntos.</a>

<pre>&gt;&gt;&gt; frutas = set(['banana', 'naranja', 'pera'])

&gt;&gt;&gt; frutas - alimentos

set(['banana', 'naranja'])

&gt;&gt;&gt; alimentos - frutas

set(['huevo', 'empanada'])

&gt;&gt;&gt; frutas &amp; alimentos

set(['pera'])

&gt;&gt;&gt; frutas | alimentos

set(['huevo', 'empanada', 'pera', 'banana', 'naranja'])

&gt;&gt;&gt; frutas ^ alimentos

set(['huevo', 'empanada', 'banana', 'naranja'])</pre>

También podemos preguntar sin un conjunto es subconjunto de otro. En los ejemplos se utiliza <code>set()</code>, el conjunto vacío:

<pre>&gt;&gt;&gt; alimentos &lt; set()

False

&gt;&gt;&gt; set() &lt; alimentos

True

&gt;&gt;&gt; set() &gt; alimentos

False

&gt;&gt;&gt; alimentos &lt;= alimentos

True

</pre>

<h2>El problema de las dos comisiones</h2>

Este problema está basado en un caso real y lo escuché en la charla <a href="http://ar.pycon.org/2009/conference/proposals/24/" target="_blank">Escribí menos código, pensá como un (buen) matemático</a> de Gustavo Carmona (FCEYN - UBA) <sup><a title="bio" href="http://ar.pycon.org/2009/profile/1d73/">bio</a></sup> y Matías A Graña (FCEyN - UBA) <sup><a title="bio" href="http://ar.pycon.org/2009/profile/015c/">bio</a></sup>.



Se tienen dos archivos de textos con una lista de e-mails en cada uno. Cada archivo tiene los mails de los funcionarios de una comisión; los archivos no están bien depurados, por lo que pueden contener direcciones repetidas; hay funcionarios trabajando en las dos comisiones. Luego de una reunión en la que trabajaron ambas comisiones, se generó un material que se necesita enviar a todos los participantes. ¿Cómo obtener la lista de destinatarios?

<pre>archivo1

dir1@mail.com

dir2@mail.com

dir3@mail.com

dir1@mail.com</pre>

<pre>archivo2

dir21@mail.com

dir23@mail.com

dir3@mail.com

dir1@mail.com</pre>

Queremos una tercera lista que tenga la primera más la segunda, pero que no estén repetidos.



El enfoque tradicional que utilizaría un programador para resolver este problema mediante bucles es:

<pre>def unionlarga(l1, l2):

    l3 = []

    for x in l1:

        if not x in l3:

            l3.append(x)

    for x in l2:

        if not x in l3:

            l3.append(x)

    return l3</pre>

Supongamos que ya tenemos los archivos leídos y almacenamos el contenidos en listas:

<pre>&gt;&gt;&gt; unionlarga(archivo1, archivo2)

['dir1@mail.com', 'dir2@mail.com', 'dir3@mail.com',

'dir21@mail.com', 'dir23@mail.com']</pre>

La solución es genérica para cualquier lenguaje. Sin embargo, puede lograr una mejor solución utilizando sets en Python:

<pre>&gt;&gt;&gt; list(set(archivo1) | set(archivo2))

['dir21@mail.com', 'dir3@mail.com', 'dir2@mail.com',

'dir1@mail.com', 'dir23@mail.com']</pre>

Convertimos ambas listas a conjuntos (con lo que se eliminan los repetidos dentro de las listas), realizamos la unión de ambos conjuntos (con lo que se eliminan los repetidos entre listas y finalmente se convierte el resultado en una nueva lista.



<a href="http://docs.python.org/library/stdtypes.html#set-types-set-frozenset" target="_blank">Más sobre conjuntos en la referencia del lenguaje.</a></body></html>