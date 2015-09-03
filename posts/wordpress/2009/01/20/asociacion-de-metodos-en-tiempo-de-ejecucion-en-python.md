<html><body><p>En el <a href="http://python-history.blogspot.com/2009/01/introduction-and-overview.html" target="_blank">primer artículo de La Historia de Python (en)</a> se menciona, entre las cualidades que hacen a Python un lenguaje que permite la programación orientada a objetos, la posibilidad de "asociación de métodos en tiempo de ejecución" ("run-time binding of methods"). Hoy en <a href="http://neopythonic.blogspot.com/2008/10/why-explicit-self-has-to-stay.html" target="_blank">otro artículo del autor</a>, vuelvo a leer sobre el tema:

</p><blockquote>Now instances of C have a method with one argument named 'meth' that works exactly as before. It even works for instances of C that were created before the method was poked into the class.</blockquote>

Vamos a ver un ejemplo de esto:

<pre>&gt;&gt;&gt; class C:

...     pass

...

&gt;&gt;&gt; c1 = C()

&gt;&gt;&gt; c1.hello()

Traceback (most recent call last):

  File "", line 1, in 

AttributeError: C instance has no attribute 'hello'

&gt;&gt;&gt; def hello(myself, name):

...     myself.lasthello = name

...     print "Hello %s" % name

...

&gt;&gt;&gt; C.hello = hello

&gt;&gt;&gt; c2 = C()

&gt;&gt;&gt; c2.hello("mary")

Hello mary

&gt;&gt;&gt; c1.hello("juanjo")

Hello juanjo</pre></body></html>