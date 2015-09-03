<html><body><p>Siguiendo con la serie de posts sobre decoradores en Python, y fiel al espíritu que los originó (ir mostrando lo que voy aprendido a medida que necesito resolver problemas específicos o descubro aplicaciones concretas) hoy les traigo un nuevo uso para los decoradores en Python: <strong>funciones caché</strong>.

<!--more-->

Anteriormente: <a href="http://www.juanjoconti.com.ar/2008/07/11/decoradores-en-python-i/" target="_blank">Decoradores I</a>, <a href="http://www.juanjoconti.com.ar/2009/07/16/decoradores-en-python-ii/" target="_blank">Decoradores II</a>.

</p><h2>Funciones caché</h2>

Una función caché[0], es aquella que siempre que se le pide que compute un resultado para un grupo de parámetros dado, primero se fija en una memoria interna si no realizó ya el cálculo. Si ya lo hizo, retorna el valor computado anteriormente. Si aún no lo hizo, computa el valor, lo guarda en una memoria interna y luego lo retorna.

Esta técnica es muy útil en funciones que requieren un cómputo intensivo y obtener un resultado lleva mucho tiempo. Permita acelerar sustancialmente los tiempos de ejecución a cambio de utilizar más memoria.



La siguiente es una forma de implementarlo en Python para un computo en particular:

<pre>cache = {}

def fmem(arg):

    if arg in cache:

        print "Recuperando valor de la memoria"

        return cache[arg]

    else:

        r = (arg ** 10) * (arg ** -5)

        cache[arg] = r

        return r</pre>

Como memoria se utiliza un diccionario y el argumento de la función fmem es la clave del diccionario[1].



Este es el resultado de utilizarla en el intérprete interactivo:

<pre>&gt;&gt;&gt; fmem(1)

1.0

&gt;&gt;&gt; fmem(2)

32.0

&gt;&gt;&gt; fmem(2)

Recuperando valor de la memoria

32.0</pre>

<h2>Decoradores con estado</h2>

En esta implementación, la técnica de memorización se mezcla con el cálculo que era el objetivo original de la función. Si queremos aplicar la técnica sobre distintas funciones vamos a tener que entrometer la implementación de la caché en todas las funciones. Peor aún, si en el futuro se quiere realizar un cambio en la forma de almacenar y recuperar los valores almacenados, ¡tendríamos que modificar todas las funciones! La forma de resolver estos problemas es implementando un decorador que agregue esta funcionalidad a las funciones decoradas: resolvemos ambos problemas, el de intrución y el de mantenibilidad. Todo el código que provee esta funcionalidad extra es encapsulado en el decorador.



Las funciones decoradoras, como las que vimos en los anteriores artículos, no nos sirven para esta tarea. Necesitamos un decorador que pueda almacenar un estado. Ya que cualquier <em>callable</em> puede ser un decorador, <strong>implementaremos el decorador mediante una clase</strong>.

<h2>Funciones caché con clases decoradoras</h2>

La definición de la clase decoradora consiste en dos métodos:

<ul>

	<li> un método de inicialización, dónde se inicializa el atributo cache con un diccionario vacío y se guarda una referencia a la función decorada.</li>

	<li>un método __call__ que será ejecutado cuando se llame a la función decorada.</li>

</ul>

<pre>class mem(object):



    def __init__(self, g):

        self.cache = {}

        self.g = g



    def __call__(self, arg):

        if arg in self.cache:

            print "Recuperando valor de la memoria"

            return self.cache[arg]

        else:

            r = self.g(arg)

            self.cache[arg] = r

            return r</pre>

Luego, lo único que resta es decorar todas las funciones que querramos "dotar de memoria" para obtener mejoras de performance en su ejecución:

<pre>@mem

def f(arg):

    return (arg ** 10) * (arg ** -5)</pre>

La salida obtenida al ejecutar la función decorada en el intérprete interactivo es la misma qué en el ejemplo anterior:

<pre>&gt;&gt;&gt; fmem(1)

1.0

&gt;&gt;&gt; fmem(2)

32.0

&gt;&gt;&gt; fmem(2)

Recuperando valor de la memoria

32.0</pre>

<h2>Más</h2>

La implementación del decorador mem solo sirve para decorar funciones que reciben un único argumento. Podemos mejorar su definición para que pueda decorar funciones con cualquier número de argumentos:

<pre>class mem2(object):



    def __init__(self, g):

        self.cache = {}

        self.g = g



    def __call__(self, *args):

        if args in self.cache:

            print "Recuperando valor de la memoria"

            return self.cache[args]

        else:

            r = self.g(*args)

            self.cache[args] = r

            return r</pre>

<pre>@mem2

def f2(arg1, arg2):

    return (arg1 ** 10) * (arg2 ** -5)</pre>

<h2>Notas</h2>

[0] Se puede leer más sobre este concepto en Caching Function Results:Faster Arithmetic by Avoiding Unnecessary Computation de Stephen E. Richardson [SMLI TR-92-1]

[1] Esta implementación tiene la limitación de que si el argumento de la función es un objeto mutable, no podrá ser usado como clave de un diccionario y se lanzará una excepción.</body></html>