<html><body><p>Este post se alinea con la serie Decoradores en Python (<a href="http://www.juanjoconti.com.ar/2008/07/11/decoradores-en-python-i/" target="_blank">I</a>, <a href="http://www.juanjoconti.com.ar/2009/07/16/decoradores-en-python-ii/" target="_blank">II</a>, <a href="http://www.juanjoconti.com.ar/2009/12/30/decoradores-en-python-iii/" target="_blank">III</a>) pero no es tan elaborado como para ser Decoradores en Python (IV) :)



Desde Python 2.5, al crear un decorador, se puede utilizar <a href="http://docs.python.org/library/functools.html" target="_blank">functools.update_wrapper</a> para quela versión decorada de la función, tenga los atributos  __name__, __doc__, __module__ y __dict__ de la función original.

</p><pre>&gt;&gt;&gt; import functools

&gt;&gt;&gt; def deco(f):

...     def inner(*a, **kw):

...             print "Este decorador no hace nada"

...             return f(*a, **kw)

...     return inner

...

&gt;&gt;&gt; def saludo():

...     print "hola"

...

&gt;&gt;&gt; saludo2 = deco(saludo)

&gt;&gt;&gt; saludo2()

Este decorador no hace nada

hola

&gt;&gt;&gt; saludo2.__name__

'inner'

&gt;&gt;&gt; def deco(f):

...     def inner(*a, **kw):

...             print "Este decorador no hace nada"

...             return f(*a, **kw)

...     return functools.update_wrapper(inner, f)

...

&gt;&gt;&gt; saludo3 = deco(saludo)

&gt;&gt;&gt; saludo3()

Este decorador no hace nada

hola

&gt;&gt;&gt; saludo3.__name__

'saludo'

&gt;&gt;&gt; saludo = saludo3

</pre></body></html>