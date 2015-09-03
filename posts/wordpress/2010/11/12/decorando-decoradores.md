<html><body><p>Una de las preguntas que aveces me hacen luego de hablar sobre <a href="http://www.juanjoconti.com.ar/taint/" target="_blank">Taint Mode</a> es: una vez que la aplicación pasa de desarrollo a producción, <strong>¿hay alguna forma de deshabilitar los decoradores?</strong>



La biblioteca usa decoradores para marcar entradas no confiables, sumideros sensibles y funciones limpiadoras con la idea de encontrar posibles vulnerabilidades en tiempo de desarrollo. Si en producción no los requerimos más, esos decoradores producen overhead.



Entonces... qué se puede hacer? <strong>Editar el código comentando los decoradores no escala</strong>[0]. Una alternativa es utilizar un nuevo decorador: llamemoslo @apply_decorator y vamos a utilizarlo para controlar mediante alguna condición (por ejemplo una variable en el archivo de configuración) si se debe usar o no el decorador.

</p><pre>

COND = True



def apply_decorator(d):

    if COND:

        return d

    else:

        return lambda f: f

</pre>

Si la condición es verdadera, se retorna el decorador original, sino una función <em>fake</em> (implementada utilizando <code>lambda</code>) que recibe una función y retorna la misma función: un decorador que no hace nada.



Un ejemplo de su uso en el REPL de Python:

<pre>

&gt;&gt;&gt; @apply_decorator

... def mydeco(f):

...     def inner(*a, **kw):

...             print "decorado"

...             return f(*a, **kw)

...     return inner

... 

&gt;&gt;&gt; mydeco

<function mydeco at>

&gt;&gt;&gt; COND = False

&gt;&gt;&gt; @apply_decorator

... def mydeco(f):

...     def inner(*a, **kw):

...             print "decorado"

...             return f(*a, **kw)

...     return inner

... 

&gt;&gt;&gt; mydeco

<function> at 0xb7753dbc&gt;

</function></function></pre>

Podemos aplicarlo directamente a la definición de nuestros decoradores 

<pre>

@apply_decorator

def mi_decorador(f):

    ...

</pre>



o al principio de nuestro programa.

<pre>

mi_decorador = apply_decorator(mi_decorador)

</pre>

[0] nessita trademark.</body></html>