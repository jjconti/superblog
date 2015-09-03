<html><body><p>Un año después del primer artículo, llega el segundo. ¿Por qué tardó tanto? Por lo general mis artículos técnicos surgen de algún problema que se me presenta y para el cual necesito investigar antes de poder solucionarlo. El artículo anterior cubría todo lo que necesité hacer con decoradores en Python hasta el mes pasado, cuando necesité decoradores con parámetros.



Si no leíste el artículo anterior, te recomiendo que lo hagas antes de seguir: <a href="http://www.juanjoconti.com.ar/2008/07/11/decoradores-en-python-i/" target="_blank">Decoradores en Python (I)</a>.

<!--more-->

</p><h2>Decoradores con Parámetros</h2>

Cuando quise escribir un decorador con un parámetro me encontré con errores que ni siquiera entendía. No solo que los estaba escribiendo mal, sino que también los estaba usando mal. Te voy a evitar el sufrimiento.



Un decorador con parámetro se aplica así (siendo deco un decorador y 1 el argumento utilizado):

<pre>@deco(1)

def funcion_a_decorar(a, b, c):

    pass</pre>

Creo que la raíz de mi confusión fue el azúcar sintáctica (si, el @). Así que vamos a sacarlo y ver cómo se usaría este decorador en una versión de Python más vieja:

<pre>def funcion_a_decorar(a, b, c):

    pass</pre>

<pre>funcion_a_decorar = deco(1)(funcion_a_decorar)</pre>

Esto luce más claro para mi: deco es llamado con un argumento y el resultado tiene que ser algún objeto que pueda ser llamado con una función como parámetro para... decorarla. ¿Se entiende la idea? Vamos a definir deco, va a recibir un parámetro y utilizarlo para crear un decorador como los del artículo anterior. Finalmente retorna este decorador interno.



Agreguemos semántica al ejemplo. Mi decorador con parámetro recibirá un número, este número se usará para indicar cuantas veces queremos ejecutar la función decorada.

<pre>def deco(i):

    def _deco(f):

        def inner(*args, **kwargs):

            for n in range(i):

                r = f(*args, **kwargs)

            return r

        return inner

    return _deco</pre>

Como una convención personal, uso para el nombre de la segunda función _{nombre de la primer funcion}. Notemos entonces que _deco es un decorador dinámico, dependiendo del parámetro i, la función inner se compilará de una forma o de otra. Apliquemos el decorador:

<pre>@deco(2)

def saluda(nombre):

    print "hola", nombre</pre>

<pre>&gt;&gt;&gt; saluda("juanjo")

hola juanjo

hola juanjo</pre>

<pre>@deco(3)

def suma1():

    global n

    n += 1</pre>

<pre>&gt;&gt;&gt; n = 0

&gt;&gt;&gt; suma1()

&gt;&gt;&gt; n

3</pre>

Cuando aplicamos deco, se ejecuta deco, se compila _deco, se aplica _deco a la función que definimos y se compila inner utilizando un valor dado para i. Cuando llamamos a nuestra función (saluda, o suma1, en los ejemplos) se ejecuta inner.



¡Espero que se haya entendido!

<h2>Si no...</h2>

Si en lo anterior no fui lo suficientemente claro (por favor quejate en un comentario), no todo está perdido. Te puedo entregar un decorador para decoradores que convierte a tu decorador en un decorador con parámetros. ¿Qué tal?

<pre>def decorador_con_parametros(d):

    def decorador(*args, **kwargs):

        def inner(func):

            return d(func, *args, **kwargs)

        return inner

    return decorador</pre>

Original usando lambda en <a href="http://pre.activestate.com/recipes/465427/" target="_blank">http://pre.activestate.com/recipes/465427/</a>



Se usa así:

<pre>@decorador_con_parametros

def deco(func, i):

    def inner(*args, **kwargs):

        for n in range(i):

           r = func(*args, **kwargs)

        return r

    return inner</pre>

<pre>@deco(2)

def saludar(nombre):

    print "chau", nombre</pre>

<pre>&gt;&gt;&gt; saludar("juanjo")

chau juanjo

chau juanjo</pre>

<h2>Para la próxima</h2>

Para el próximo artículo voy a explorar utilizar clases decoradoras en lugar de funciones decoradoras. Si bien todavía no lo terminé de investigar, me parece un enfoque que permite escribir código más organizado. Veremos! <strong>update:</strong> <a href="http://www.juanjoconti.com.ar/2009/12/30/decoradores-en-python-iii/" target="_blank">aquí está</a>.</body></html>