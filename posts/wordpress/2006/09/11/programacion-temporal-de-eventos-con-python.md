<html><body><p>Este artículo estuvo en mi lista de borradores (<em>draft posts</em>) por mucho tiempo ya. Evidente mente no cumplí con la consigna <em><a href="http://www.catb.org/~esr/writings/cathedral-bazaar/cathedral-bazaar/ar01s04.html">release early</a></em> del desarrollo tipo bazar. <em>Enough!</em>



Este artículo va a hablar un poco de simulación de sistemas discretos, va a presentar un módulo que escribí como prueba de que se podía hacer y me va a servir para contarles algunas cosas uq e aprendí en el camino.



Sigo <a href="http://firebirds.com.ar/~juanjo/wordpress/category/aprendiendo-python/">Aprendiendo Python</a> y esta es una clase más.

<!--more-->



</p><h2>Programación temporal de eventos</h2>



En el primer cuatrimestre de este año cursé una materia llamada <a href="http://www.frsf.utn.edu.ar/matero/visitante/index.php?id_catedra=150">Simulación</a>. Estudiamos principalmente como simular sistemas discretos (como un grupo de pasajeros subiendo a un avión. Suben de a uno, en un momento hay 7 pasajeros a bordo y en otro momento hay 8, nunca hay 7.5) en contraposición a los sistemas continuos (como el tanque de nafta del avión dónde su nivel baja instante a instante cuando el avión está volando).



Básicamente existen dos tipos de técnicas que se pueden utilizar para simular sistemas discretos, las de orientación al intervalo y las de orientación al evento. En las del primer tipo, cada cierto tiempo t se verifica de alguna forma si ha ocurrido un evento y se realiza el procesamiento asociado a este. Esto lleva a impresiciones y en ocasiones a un gasto innecesesario de cpu. En las técnicas de orientación al evento estos problemas no existen. 



Una de las técnicas más primitivas de orientación al intervalo (no se si se usa en la actualidad) es la de Programación Temporal de Eventos. Básicamente se tiene un reloj que cuenta el tiempo de simulación y una lista de eventos ordenada en el tiempo. Uno debe escribir una función o procedimiento por cada uno de los eventos principales del sistema (por ejemplo la llegada de una pieza a una máquina) y una función principal que contenga el <em>main loop</em> de la simulación. Esta irá tomando eventos de la lista, avanzará el tiempo de simulación según corresponda y los ejecutará. Siempre se toma el primero y se lo ejecuta, si no hay más elementos en la lista termina la siumulación.



Los eventos son agregados a la lista con una primitiva llamada por ejemplo <strong>PPE</strong> (programar próximo evento), dónde además de indicar <em>cual</em> será el próximo evento, se debe indicar dentro de cuanto tiempo a partir del actual se debe ejecutar.



Mientras cursaba, estudiaba y rendía pensaba que sería muy fácil implementar en Python un módulo que provea las primitivas necesarias para realizar una simulción por programación temporal de eventos. Poner y sacar funciones de una lista seguro sería sencillo en un lenguaje muy dinámico y donde todo (incluidas las funciones) son objetos. La semana siguiente a rendir estuve escribiendo un poco de código Python. El resultado es un módulo llamado <strong>pte</strong> que cubre las funcionalidades mínimas que yo pretendía.



<h2>Resultado</h2>

No pretendía realizar un imponente desarrollo ni pienso que alguien use esto alguna vez en serío. Es más bien una prueba de concepto (<em><a href="http://en.wikipedia.org/wiki/Proof_of_concept">Proof of concept</a></em>). Lo había avandonado y ni siquiera funcionaba sin tirar errores. Objetivo: que funcione.



Este es el módulo: <a href="http://firebirds.com.ar/~juanjo/wordpress/files/python/pte.py.html">pte.py</a> (versión orginal)

Una versión con el consejo de Daniel: <a href="http://firebirds.com.ar/~juanjo/wordpress/files/python/pte-d.py.html">pte-d.py</a> (gracias Daniel!)

Y este un ejemplo en el que lo uso: <a href="http://firebirds.com.ar/~juanjo/wordpress/files/python/pte_ej2.py.html">pte_ej2.py</a>



Ejemplo de ejecución:

<pre lang="bash">

juanjo@sarge:~/python$ ./pte_ej2.py



500 piezas fueron aceptadas en 1247.55 unidades de tiempo.



Máximo tamaño de la cola para procesamiento 5.

</pre>



<h2>Qué aprendí</h2>

<h3>Módulos</h3>

Más de lo que pueda decir sobre módulos: <a href="http://docs.python.org/tut/node8.html">http://docs.python.org/tut/node8.html</a>

<h3>reload(modulo)

<blockquote>

Reload a previously imported module. The argument must be a module object, so it must have been successfully imported before. This is useful if you have edited the module source file using an external editor and want to try out the new version without leaving the Python interpreter. The return value is the module object (the same as the module argument).

</blockquote>



Entonces lo que hay que hacer cuando se está trabajando en la consola de Python[1] es, primer importar el módulo que se quiere probar:

<pre>

&gt;&gt;&gt; import modulo

</pre>

Hacer algunas pruebas:

<pre>

&gt;&gt;&gt; modulo.var1

1

&gt;&gt;&gt; modulo.cuad(3)

9

</pre>

Si luego editamos el texto de <em>modulo</em> y queremos probar la función que agregarmos:

<pre>

&gt;&gt;&gt; modulo = reload(modulo)

</pre>

<h3>Funciones como objetos</h3>

En Python todo es un objeto, incluso las funciones. Sabiendo esto y teniendo en mente lo que quería hacer (en la definición de una función, explicitar que esta se llame en el futuro, es decir almacenarla en una <em>lista de eventos</em>) hice una pequeña prueba en el intérprete:

<pre>

&gt;&gt;&gt; l = []

&gt;&gt;&gt; def f():

	l.append(f)



	

&gt;&gt;&gt; l

[]

&gt;&gt;&gt; f()

&gt;&gt;&gt; l

[&lt;function f at 0x418bce9c&gt;]

&gt;&gt;&gt; l[0]

&lt;function f at 0x418bce9c&gt;

&gt;&gt;&gt; l

[&lt;function f at 0x418bce9c&gt;]

&gt;&gt;&gt; l[0]()

&gt;&gt;&gt; l

[&lt;function f at 0x418bce9c&gt;, &lt;function f at 0x418bce9c&gt;]

</pre>



Esto es posible justamente gracias a que en Python las funciones son objetos. En ciencias de la computación esto se conoce como Funciones de Primera Clase, es decir que las funciones sean Objetos de Primera Clase, es decir que puedan ser creadas durante la ejecución de un programa, almacenadas en estructuras de datos, recuperadas más tarde para usarlas, pasadas como argumentos y retornadas en otras funciones. <a href="http://en.wikipedia.org/wiki/First-class_function">Más al respecto en wikipedia</a>.

<h3>Ordenar según un criterio propio</h3>

Una lista puede ser ordenada según un criterio propio pasándole al método sort de una lista ese criterio en forma de función:

<pre>

def _comparar_tiempos(a,b):

    """ Función auxiliar usada para ordenar los pares eventos,tiempos

    en la lista de eventos.

    """

    t1 = a[1]

    t2 = b[1]

    if (t1 &gt; t2): return 1

    elif (t1 &lt; t2): return -1

    else: return 0

</pre>

y luego..

<pre>

eventos.sort(_comparar_tiempos)

</pre>



Espero les haya resultado interesante!



[1] También conocida como <a href="http://en.wikipedia.org/wiki/Read-eval-print_loop">REPL</a>, algo muy piola cuando uno esta desarrollando.





</h3></body></html>