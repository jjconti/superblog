<html><body><em>El siguiente texto es una traducción del artículo Origins of Python's "Functional" Features de Guido van Rossum publicado en <a href="http://python-history.blogspot.com/" target="_blank">http://python-history.blogspot.com/</a>.</em>



<!--more-->

<h2>Los orígenes de las características "Funcionales" de Python</h2>

Yo nunca considere que Python esté fuertemente influenciado por lenguajes funcionales, no importa lo que la gente diga o piense. Estoy  mucho mas familiarizado con lenguajes imperativos, como C y Algol 68, y aunque hice a las funciones objetos de primera clase, nunca vi a Python como un lenguaje de programación funcional. Sin embargo, tiempo atrás, tenia claro que los usuarios querían hacer mucho mas con las  listas y las funciones



Una operación común en las listas fue la de mapear una función a cada elemento de una lista, creando una nueva lista. Por ejemplo:

<pre>def square(x):

    return x*x

vals = [1, 2, 3, 4]

newvals = []

for v in vals:

    newvals.append(square(v))</pre>

En los lenguajes funcionales como Lisp y Sheme, operaciones como esa son provistas como funciones incorporadas al lenguaje. Por lo tanto, los nuevos usuarios, familiarizados con este tipo de lenguajes se encontraron a si mismos implementando funcionalidades similares en Python. Por Ejemplo

<pre>def map(f, s):

    result = []

    for x in s:

        result.append(f(x))

    return result</pre>

<pre>def square(x):

    return x*x

vals = [1, 2, 3, 4]

newvals = map(square,vals)</pre>

Un detalle sutil del código de arriba es que a mucha gente no le gusto la idea de tener que definir una función separada para la operación  que estaban aplicando a cada elemento de la lista. Lenguajes como Lisp permitían funciones simplemente definidas "al vuelo", al hacer la llamada a la función map. Por ejemplo en Scheme, se pueden crear funciones anónimas y hacer operaciones de asignación en una expresión simple usando lambda, de esta forma:

<pre>(map (lambda (x) (* x x)) '(1 2 3 4))</pre>

Aunque en Python las funciones son objetos de primera clase, no tenia un mecanismo similar para para crear funciones anónimas.



A finales de 1993, los usuarios estaban proponiendo varias ideas para crear funciones anónimas y funciones para manipular listas como: map(), filter() y reduce().  Por ejemplo, Mark Lutz (autor de "Programming Python") envió este código, para una función que  crea funciones usando exec:

<pre>def genfunc(args, expr):

    exec('def f(' + args + '): return ' + expr)

    return eval('f')</pre>

<pre># Sample usage

vals = [1, 2, 3, 4]

newvals = map(genfunc('x', 'x*x'), vals)</pre>

Entonces Tim Peters lo siguió con una solución que simplificaba un poco mas la sintaxis, permitiendo que los usuarios escriban:

<pre>vals = [1, 2, 3, 4]

newvals = map(func('x: x*x'), vals)</pre>

Estaba claro que había una demanda de esas funcionalidades. Sin embargo, al mismo tiempo,  me parecía demasiado "hacky" que se creen funciones anónimas como strings, que tenías que procesar usando "exec". Así que en enero de 1994, las funciones map(), filter(), y reduce() fueron agregadas a la biblioteca estándar. Ademas se creo el operador lambda para crear funciones anónimas (como expresión) con una sintaxis mas sencilla. Por Ejemplo:

<pre>vals = [1, 2, 3, 4]

newvals = map(lambda x:x*x, vals)</pre>

Esas incorporaciones representan una significativa  contribución de código fuente. Desafortunadamente no recuerdo el autor, y  no esta registrado en el SVN. Si es tuyo, ¡dejá un comentario!



Nunca estuve del todo conforme con el uso de la termino "lambda", pero a falta de una mejor y mas obvia alternativa, fue lo adoptado para Python. Después de todo, fue la elección del contribuyente anónimo, y en ese momento los grandes cambios requerían menos discusión que actualmente, <a href="http://www.python.org/dev/peps/pep-0001/" target="_blank">para bien</a> o <a href="http://yellow.bikeshed.com/" target="_blank">para mal</a>.



Lambda solo pretendía ser una herramienta sintáctica para definir funciones anónimas. Sin embargo, la elección de esa terminología tuvo muchas consecuencias inesperadas. Los usuarios acostumbrados a los lenguajes funcionales esperaban que la semántica fuese igual que en estos. Como resultado, encontraban que la implementación de Python no tenia demasiadas características avanzadas. Un detalle de lambda es que la expresión no puede referirse a variables en el ámbito circundante. Por  ejemplo, si tenes el siguiente código, la función map() se rompería, porque la función lambda se ejecutaría con una referencia indefinida a la variable "a".

<pre>def spam(s):

    a = 4

    r = map(lambda x: a*x, s)</pre>

Había formas de solucionar este problema, pero involucraban prácticas ilógicas como setear argumentos por defecto y pasar argumentos escondidos en la expresión lambda. Por ejemplo:

<pre>def spam(s):

    a = 4

    r = map(lambda x, a=a: a*x, s)</pre>

La solución "correcta" a este problema fue que las funciones interiores llevaran, implícitamente, referencias a todas las variables locales del entorno circundante referenciadas por la función. Esto es conocido como "closure", y es un aspecto esencial de los lenguajes funcionales. Sin embargo esa capacidad no se introdujo hasta la versión 2.2 (pero podia ser importada "desde el futuro" en Python 2.1).



Curiosamente, map, filter y reduce, que motivaron originalmente la introducción de lambda y otras características funcionales, fueron, en gran medida reemplazadas por las listas por comprensión y las expresiones generadoras. De hecho, la función reduce fue removida de las funciones incorporadas en Python 3.0 (Sin embargo no es necesario que me manden quejas por la quita de lambda, map o filter: se quedarán en su sitio :-)



Hay que tener en cuenta que, aunque yo no preveía a Python como un lenguaje funcional, la introducción de closures ha sido útil en el desarrollo de muchas otras características avanzadas de programación. Por ejemplo, ciertos aspectos de los nuevos estilos de clases, decoradores y otras funcionalidades dependen de esta característica.



Finalmente, aunque a lo largo de los años se introdujeron varias características de programación funcional, Python no tiene ciertas capacidades que se encuentran en los verdaderos lenguajes de programación funcional. Por ejemplo, Python no realiza ciertos tipos de optimizaciones (como recursión por la cola). En general, por la naturaleza extremadamente dinámica de Python, es imposible de hacer optimizaciones en tiempo de compilación como las de lenguajes como Haskell o ML. Y eso <a href="http://hugunin.net/story_of_jython.html" target="_blank">es bueno</a>.



<em>Traducido por <a href="http://www.joaclandia.com.ar/" target="_blank">Joaquín Sorianello</a>.

Revisado por Juan José Conti.

Si encontrás errores en esta traducción, por favor reportalos en un comentario y los corregiremos a la brevedad.</em>

Todas las traducciones de esta serie pueden encontrarse en <a href="/categoria/aprendiendo-python/historia/" target="_self">La historia de Python</a>.</body></html>