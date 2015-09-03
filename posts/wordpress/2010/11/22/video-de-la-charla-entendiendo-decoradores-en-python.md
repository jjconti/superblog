<html><body><a href="http://twitter.com/Orfx" target="_blank">Orfi</a> se tomó el trabajo de editar una filmación de mi charla en el <a href="http://www.juanjoconti.com.ar/2010/05/09/charla-entendiendo-decoradores-en-python/" target="_blank">PyDay de Rafaela</a> con mis slides para armar este video. Muchas gracias!



<center>

<iframe src="http://player.vimeo.com/video/16976108" width="400" height="300" frameborder="0"></iframe><p><a href="http://vimeo.com/16976108">entendiendo decoradores</a> from <a href="http://vimeo.com/user5262473">Orfx Sch</a> on <a href="http://vimeo.com">Vimeo</a>.</p>

</center>

Al final, durante las preguntas, escribo algo de código Python en la terminal. Lo siguiente es una reproducción:

<pre>&gt;&gt;&gt; def f(a, b):

...     print a, b

...

&gt;&gt;&gt; f(1, 2)

1 2

&gt;&gt;&gt; def f(*a, **kw):

...     print a

...     print kw

...

&gt;&gt;&gt; f(1)

(1,)

{}

&gt;&gt;&gt; f(1, parametro=2)

(1,)

{'parametro': 2}

</pre>

<pre>&gt;&gt;&gt; def f(p1, *a, **kw):

...     print kw['param']

...

&gt;&gt;&gt; f()

Traceback (most recent call last):

  File "", line 1, in

TypeError: f() takes at least 1 argument (0 given)

&gt;&gt;&gt; f(1, 2, 3, param=0)

0

</pre>

<pre>&gt;&gt;&gt; def deco(f):

...     def _deco(*a, **kw):

...             if kw.get('p'):

...                     return f(*a, **kw)

...             else:

...                     print "No ejecuto."

...     return _deco

...

&gt;&gt;&gt; @deco

... def saludo(*a, **kw):

...     print "hola"

...

&gt;&gt;&gt; saludo()

No ejecuto.

&gt;&gt;&gt; saludo(p=0)

No ejecuto.

&gt;&gt;&gt; saludo(p=1)

hola

</pre></body></html>