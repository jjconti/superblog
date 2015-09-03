<html><body><p>Esta es una traducción de la última sección del <a href="http://www.python.org/dev/peps/pep-0008/" target="_blank">PEP 8 de Python</a>,<strong> Recomendaciones al programar</strong>:



<!--more-->

</p><h2>Programming Recommendations</h2>

<strong>El código</strong> debe ser escrito de forma que no tenga desventajas en otras implementaciones de Python aparte de CPython (PyPy, Jython, IronPython, Pyrex, Psyco).



Por ejemplo, no te bases en la implementación eficiente que tiene CPython de concatenación <em>in-place</em> de strings en sentencias de la forma <code>a+=b</code> o <code>a=a+b</code>. Esas sentencias corren más despacio en Jython. En su lugar la forma <code>''.join()</code> debe ser usada en bibliotecas, en las partes dónde la performance sea importante. Esto asegura que la concatenación ocurra en tiempo lineal en todas las implementaciones.



<strong>La comparación con <em>singletons</em></strong> como <code>None</code> siempre debe hacerse con <code>is</code> o <code>is not</code>, nunca con los operadores de igualdad.



También tené cuidado al escribir <code>if x</code> cuando realmente querés decir <code>if x is not None</code>, por ejemplo al testear si a una variable o argumento que por defecto es <code>None</code> le fue asignado a otro valor. El otro valor puede tener un tipo (por ejemplo, un contenedor) que puede ser falso en un contexto booleado! (NdT: por ejemplo [] o {}).



<strong>Usá excepciones basadas en clases</strong>



Las excepciones basadas en strings en código nuevo deben desaparecer ya que esta característica del lenguaje fue eliminada en Python 2.6.



Los módulos o paquetes deben definir su propia clase base para exepciones específica de su dominio, la cual debe extender la clase <em>built-in</em> <code>Exception</code>. Siempre incluí un <em>docstring</em> a la clase, por ejemplo:

<pre>

class MessageError(Exception):

"""Clase base para errores en el paquete mail."""

</pre>

La convención para el nombramiento de clases se aplica aquí, aunque deberías agregar el sufijo 'Error' a tus clases de excepciones, si la excepción es un error. Las excepciones que no sean errores no necesitan un sufijo especial.



<strong>Al lanzar una excepción</strong>, usá <code>raise ValueError('mensaje')</code> en lugar de <code>raise ValueError, 'message'</code>.



La forma usando paréntesis es preferida porque cuando los argumentos de la excepción son largos o incluyen formateo de strings, no necesitás usar el carácter de continuación de línea (\) gracias al paréntesis. La forma vieja será quitada en Python 3000.



Al atrapar excepciones, mencioná la excepción específica cuando puedas, en lugar de usar la clausula <code>except:</code>.



Por ejemplo, usá:

<pre>

try:

    import platform_specific_module

except ImportError:

    platform_specific_module = None

</pre>



Una clausula <code>except:</code> atrapará las excepciones <code>SystemExit</code> y <code>KeyboardInterrupt</code>, haciendo que sea más difícil interrumpir al programa con Control-C, y puede traer otros problemas.  Si querés atrapar todas las excepciones que señalan errores en el programa, usar <code>except Exception:</code>.



Una buena regla es limitar el uso de la clausula <code>except:</code> a dos casos:

<ol>

	<li>Si el manejador de excepción estará imprimiendo o logeando el <em>traceback</em>; al menos el usuario se dará cuenta de que ocurrió un error.</li>

	<li>Si el código necesita hacer algún trabajo de limpieza, pero después deja que la excepción se propague hacia arriba con <code>raise</code>.

<code>try...finally</code> es la mejor forma de manejar este caso.</li>

</ol>

<strong>Adicionalmente</strong>, para todas las clausulas try/except, limitá la clausula <code>try</code> a la absolutamente mínima cantidad de código necesario. De nuevo, esto evita esconder bugs.



Si:

<pre>

try:

    value = collection[key]

except KeyError:

    return key_not_found(key)

else:

    return handle_value(value)

</pre>



No:



<pre>

try:

    # Too broad!

    return handle_value(collection[key])

except KeyError:

    # Will also catch KeyError raised by handle_value()

    return key_not_found(key)

</pre>

<strong>Usar los métodos de string</strong> en lugar del módulo string.



Los métodos de string son siempre más rápidos y comparten la misma API con los strings unicode. Sobreescribí esta regla si necesitás compatibilidad hacia atrás con versiones de Python menores a 2.0.



<strong>Usá <code>''.startswith()</code> y <code>''.endswith()</code></strong> en lugar de rebanamiento de strings (<em>string slicing</em>) para checkear prefijos y sufijos.



<code>startswith()</code> y <code>endswith()</code> son más limpios y menos propensos a errores. Por ejemplo:



Si: <code>if foo.startswith('bar'):</code>



No:  <code>if foo[:3] == 'bar':</code>



La excepción es sin tu código debe funcionar con Python 1.5.2 (pero esperemos que no!).



<strong>La comparación entre tipos</strong> de objetos debe usar siempre isinstance() en lugar de comparar tipos directamente.



Si: <code>if isinstance(obj, int):</code>



No:  <code>if type(obj) is type(1):</code>



Al chequear si un objeto es un string, recordá que hay strings Unicode también! En Python 2.3, str y unicode tienen una clase base común, basestring, así que podés hacer:



<code>if isinstance(obj, basestring):</code>



En Python 2.2, el módulo types tiene el tipo StringTypes definido para ese propósito, por ejemplo:



<pre>

from types import StringTypes

if isinstance(obj, StringTypes):

</pre>



En Python 2.0 y 2.1, tenés que hcaer:



<pre>from types import StringType, UnicodeType

if isinstance(obj, StringType)

</pre>

o

<pre>

isinstance(obj, UnicodeType) :

</pre>



<strong>Para secuencias</strong>, (strings, listas, tuplas), hacé uso del hecho de que las secuencias vacías tienen valor de verdad falso:



Si:

<pre>

if not seq:

if seq:

</pre>

No:

<pre>

if len(seq):

if not len(seq):

</pre>



<strong>No escribas</strong> strings literales que hagan uso de espacios en blanco al final de una línea. Esos espacios en blanco son visualmente indistingibles y algunos editores (o más recientemente, <a href="http://svn.python.org/projects/python/trunk/Tools/scripts/reindent.py">reindent.py</a>) los eliminan.



<strong>No compares</strong> valores booleanso con <code>True</code> o <code>False</code> usando <code>==</code>.



Si: <pre>if greeting:</pre>



No: <pre>if greeting == True:</pre>



Peor: <pre>if greeting is True:</pre></body></html>