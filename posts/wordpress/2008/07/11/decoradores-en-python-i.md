<html><body><p>Este artículo es el primero de un plan de 3 artículos. Empezamos con una introducción a los decoradores en Python.

<!--more-->

</p><h2>Funciones</h2>

Cómo todo en Python, las funciones son objetos. La forma más común de crear un objeto de tipo &lt;function&gt;  es mediante el keyword def:

<pre>def saludo():

    print "Hola"</pre>

Al realizar esta definición, el cuerpo de la función es compilado pero no ejecutado y el objeto de tipo &lt;function&gt;  es asociado al nombre 'saludo'. Mediante este nombre podemos referirnos al objeto:

<pre>&gt;&gt;&gt; saludo

&lt;function saludo at 0xb7d82fb4&gt;</pre>

y utilizando la notación de paréntesis podemos llamar a (ejecutar) la función.

<pre>&gt;&gt;&gt; saludo()

Hola</pre>

Una función puede tener parámetros (los parámetros son nombres a los que podemos referirnos en el cuerpo de la función):

<pre>def saludo2(nombre):

    print "Hola %s" % nombre</pre>

<pre>def saludo3(nombre, apellido):

    print "Hola %s %s" % (nombre, apellido)</pre>

Cuando llamamos a la función con argumentos (los argumentos son valores que en principio se asocian uno a uno a los parámetros de la función):

<pre>&gt;&gt;&gt; saludo2("Ceci")

Hola Ceci</pre>

<pre>&gt;&gt;&gt; saludo3("Ceci", "Pucci")

Hola Ceci Pucci</pre>

Los últimos n parámetros pueden tener valores por defecto, entonces estas definiciones y sus consiguientes ejecuciones son válidas:

<pre>def saludo4(nombre, apellido="Conti"):

    print "Hola %s %s" % (nombre, apellido)</pre>

<pre>&gt;&gt;&gt; saludo4("Juanjo")

Hola Juanjo Conti</pre>

<pre>&gt;&gt;&gt; saludo4("Juanjo", "Garau")

Hola Juanjo Garau</pre>

<pre>def saludo5(nombre="Juanjo", apellido="Conti"):

    print "Hola %s %s" % (nombre, apellido)</pre>

<pre>&gt;&gt;&gt; saludo5()

Hola Juanjo Conti</pre>

<pre>&gt;&gt;&gt; saludo5("Mary")

Hola Mary Conti</pre>

Los últimos n argumentos pueden ser argumentos nombrados, es decir utilizando el nombre de los parámetros con los que el argumento se debe asociar. En las siguientes ejecuciones se pueden ver ejemplos de esto:

<pre>def saludo6(tratamiento, nombre, apellido):

    print "Hola %s %s %s" % (tratamiento, nombre, apellido)</pre>

<pre>&gt;&gt;&gt; saludo6("Sr.", apellido="Conti", nombre="Juanjo")

Hola Sr. Juanjo Conti</pre>

<pre>&gt;&gt;&gt; saludo6("Sr.", "Juanjo", apellido="Conti")

Hola Sr. Juanjo Conti</pre>

Los parámetros de una función pueden terminar con *&lt;nombre&gt;  (una tupla con los últimos argumentos posicionales) y/o **&lt;nombre&gt;  (un diccionario con los últimos argumentos nombrados).

<pre>def saludo7(tratamiento, *args):

    print "Hola %s %s" % (tratamiento, " ".join(args))</pre>

<pre>&gt;&gt;&gt; saludo7("Sr.", "Juanjo", "Conti")

Hola Sr. Juanjo Conti</pre>

<pre>&gt;&gt;&gt; saludo7("Sr.", "Juanjo", "Conti", "Garau")

Hola Sr. Juanjo Conti Garau</pre>

Notemos que esta forma de definir una función es bastante útil cuando no sabemos el número de argumentos que se recibirán.

La siguiente es la forma más genérica de definir una función:

<pre>def saludo8(*args, **kwargs):

    pass</pre>

<h2>Decoradores</h2>

Un decorador es una función 'd' que recibe como argumento otra función 'a' y retorna una nueva función 'b'. La nueva función 'b' es la función 'a' decorada con 'd'.



Supongamos que queremos avisarle a un sistema de seguridad cada vez que se ejecutan las funciones abrir_puerta y cerrar_puerta. Para hacer una simplificación, el aviso simplemente será imprimir por un mensaje en la pantalla. Podemos escribir el siguiente 'decorador':

<pre>def avisar(f):

    def inner(*args, **kwargs):

        f(*args, **kwargs)

        print "Se ha ejecutado %s" % f.__name__

    return inner</pre>

Las siguientes son las funciones a decorar:

<pre>def abrir_puerta():

    print "Abrir puerta"



def cerrar_puerta():

    print "Cerrar puerta"</pre>

<pre>&gt;&gt;&gt; abrir_puerta()

Abrir puerta

&gt;&gt;&gt; cerrar_puerta()

Cerrar puerta</pre>

Y ahora solo nos limitamos a seguir la definción que di al principio de un decorador:

<pre>abrir_puerta = avisar(abrir_puerta)

cerrar_puerta = avisar(cerrar_puerta)</pre>

Listo!, ambas funciones han sido decoradas:

<pre>&gt;&gt;&gt; abrir_puerta()

Abrir puerta

Se ha ejecutado abrir_puerta

&gt;&gt;&gt; cerrar_puerta()

Cerrar puerta

Se ha ejecutado cerrar_puerta</pre>

<h2>Azúca sintáctica</h2>

En Python 2.3, la anterior era la forma de decorar una función. A partir de Python 2.4 se a añadido azúcar sintáctica al lenguaje que nos permite hacer lo mismo de esta forma:

<pre>@avisar

def abrir_puerta():

    print "Abrir puerta"



@avisar

def cerrar_puerta():

    print "Cerrar puerta"</pre>

Esta es una forma mucho más visual de hacerlo.

<h2>Encadenando decoradores</h2>

La decoración de funciones puede encadenarse. Para ejemplificarlo vamos a suponer ahora que solo usuarios autenticados en el sistema pueden ejecutar las funciones abrir_puerta y cerrar puerta.



Nuevamente hacemos una simplificación. Existe la variable AUTHENTICATED que indica el estado del usuario actual. Si el usuario no está autenticado y se intente ejecutar alguna de las funciones, una excepción es lanzada.

<pre>def autenticado(f):

    def inner(*args, **kwargs):

        if AUTHENTICATED:

            f(*args, **kwargs)

       else:

           raise Exception

    return inner</pre>

Luego, la definición de abrir_puerta y cerrar_puerta debería ser:

<pre>@autenticado

@avisar

def abrir_puerta():

    print "Abrir puerta"



@autenticado

@avisar

def cerrar_puerta():

    print "Cerrar puerta"</pre>

Con AUTHENTICATED = True:

<pre>&gt;&gt;&gt; cerrar_puerta()

Cerrar puerta</pre>

Se ha ejecutado cerrar_puerta



Pero si AUTHENTICATED = False:

<pre>&gt;&gt;&gt; cerrar_puerta()

Traceback (most recent call last):

File "&lt;stdin&gt; ", line 1, in &lt;module&gt;

File "&lt;stdin&gt; ", line 6, in inner

Exception</pre>

<strong>update:</strong> <a href="http://www.juanjoconti.com.ar/2009/07/16/decoradores-en-python-ii/" target="_blank">2° entrega</a>.</body></html>