<html><body><p>Me llegó un mail consultando sobre <code>*args</code> y <code>**kwargs</code> en Python. ¿Qué es eso? Vamos por partes.



En Python existen varias formas de llamar a una función. Por ejemplo, en su definición <a href="http://docs.python.org.ar/tutorial/controlflow.html#argumentos-con-valores-por-omision" target="_blank">puede tener valores por defecto</a>, entonces no es necesario utilizarlos todos al llamarla:

</p><pre>&gt;&gt;&gt; def f(a, b, c=3):

...     print a, b, c

...

&gt;&gt;&gt; f(1,2)

1 2 3</pre>

<a href="http://docs.python.org.ar/tutorial/controlflow.html#palabras-claves-como-argumentos" target="_blank">Se pueden utilizar palabras claves como argumento</a>, por supuesto, respetando algunas reglas:

<pre>&gt;&gt;&gt; def f(a, b, c):

...     print a, b, c

...

&gt;&gt;&gt; f(a=1, b=2, c=3)

1 2 3

&gt;&gt;&gt; f(a=1, 2, 3)

  File "", line 1

SyntaxError: non-keyword arg after keyword arg

&gt;&gt;&gt; f(1, 2, b=3)

Traceback (most recent call last):

  File "", line 1, in

TypeError: f() got multiple values for keyword argument 'b'

&gt;&gt;&gt; f(1, b=2, c=3)

1 2 3</pre>

Y finalmente, <a href="http://docs.python.org.ar/tutorial/controlflow.html#listas-de-argumentos-arbitrarios" target="_blank">se puede llamar con listas arbitrarias de argumentos</a>. Como en los casos anteriores, poder hacerlo depende de cómo hayamos definido la función:

<pre>&gt;&gt;&gt; def f(*args, **kwargs):

...     print "args:", args

...     print "kwargs:", kwargs

...</pre>

Con <code>*args</code> se indica, mapear todos los argumentos posicionales a una tupla llamada <code>args</code>. Y con <code>**kwargs</code> se indica, mapear todos los argumentos de palabra clave a un diccionario llamado <code>kwargs</code>.

<pre>&gt;&gt;&gt; f(1,2,3)

args: (1, 2, 3)

kwargs: {}

&gt;&gt;&gt; f(1,2,3, cuatro=4)

args: (1, 2, 3)

kwargs: {'cuatro': 4}

&gt;&gt;&gt; f(cuatro=4)

args: ()

kwargs: {'cuatro': 4}</pre>

Notemos que se pueden definir argumentos con nombre propio antes de los argumentos <em>agrupados</em> y que no es necesario usar exactamente los nombres <code>args</code> y <code>kwargs</code>. También puede usarse solo uno de los dos:

<pre>&gt;&gt;&gt; def f(p, *a, **kw):

...     print "p:", p

...     print "a:", a

...     print "kw:", kw

...

&gt;&gt;&gt; f(1,2,3)

p: 1

a: (2, 3)

kw: {}

&gt;&gt;&gt; f(1,2,3, cuatro=4)

p: 1

a: (2, 3)

kw: {'cuatro': 4}

&gt;&gt;&gt; f(cuatro=4)

Traceback (most recent call last):

  File "", line 1, in

TypeError: f() takes at least 1 non-keyword argument (0 given)</pre>

Espero que los ejemplos sirvan. Para más detalle, se pueden consultar las secciones del <a href="http://tutorial.python.org.ar/" target="_blank">Tutorial de Python</a> que enlacé.</body></html>