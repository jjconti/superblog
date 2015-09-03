<html><body><p>En la lista de PyAr <a href="http://www.grulic.org.ar/lurker/message/20100204.020622.c24e333b.en.html" target="_blank">preguntaron</a> si había alguna forma de aplicar un decorador a todos las funciones de un módulo. Envié una solución sin probarla, que al verla unos días más tarde parece bastante buena :)



La comento aquí con un ejemplo. modulo.py contiene definiciones de funciones:

</p><pre>def a():

    pass



def b():

    print 42



def c():

    a()

    b()</pre>

y decoradores.py un decorador que imprime el nombre de la función llamada:

<pre>def nombrador(f):

    def inner(*a, **kw):

        print "Ejecutando %s" % f.__name__

        return f(*a, **kw)

    return inner</pre>

(Si no sabés lo que es un decorador, podés leer mi post <a href="http://www.juanjoconti.com.ar/2008/07/11/decoradores-en-python-i/" target="_blank">Decoradores en Python I: Introducción</a>)



En lugar de modificar las definiciones de funciones en modulo.py para aplicar el decorador a cada una de las funciones, ya sea usando el azúcar sintáctica de Python:

<pre>@nombrador

def a():

    ...</pre>

o mediante una llamada a la función:

<pre>a = nombrador(a)</pre>

podemos agregar el siguiente código al final de modulo.py:

<pre>for n,v in locals().items():

   if inspect.isfunction(v) and n != 'nombrador':

       locals()[n] = nombrador(v)</pre>

Vamos a explicarlo:



la llamada a la función built-in locals retorna un diccionario representando el espacio de nombres local: cada clave es un string representando el nombre de un objeto y cada valor es el objeto en si. Iteramos sobre la lista de pares (key, value) del mencionado dict y por cada uno verificamos si:



a) es una función (inspect.isfunction es apropiado para esto)

b) el nombre no es el del decorador que queremos aplicar (para no aplicar el decorador sobre si mismo!)



Si las condiciones a y b se cumplen, podemos guardar en el diccionario del espacio de nombres, bajo el nombre de la función que cumplió las condiciones, una versión decorada de la misma.



Agregamos algo más de código a modulo.py para que se llame a las funciones cuando lo ejecutemos:

<pre>if __name__ == '__main__':

    a()

    b()

    c()</pre>

Esta es la salida obtenida:

<pre lang="bash">juanjo@fenix:~/python/muchosdecos$ python modulo.py

Ejecutando a

Ejecutando b

42

Ejecutando c

Ejecutando a

Ejecutando b

42</pre>

¿Querés probarlo? Bajá <a href="/wp-content/uploads/2010/02/muchos.zip">muchos.zip</a>



<strong>Nota:</strong> para acceder a locals() no se puede utilizar iteritems por que el diccionario cambia durante la ejecución.</body></html>