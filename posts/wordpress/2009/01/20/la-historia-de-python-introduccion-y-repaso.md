<html><body><em>El siguiente texto es una traducción del artículo <a href="http://python-history.blogspot.com/2009/01/introduction-and-overview.html" target="_blank">Introduction and Overview</a> de Guido  van Rossum publicado en <a href="http://python-history.blogspot.com/" target="_blank">http://python-history.blogspot.com/</a>. Mi objetivo es traducir todos los artículos que se publiquen en ese blog.</em><!--more-->

<h2>Introducción</h2>

Python es en la actualidad uno de los lenguajes de programación dinámicos más populares, junto con Perl, Tcl, PHP y ahora Ruby. A pesar de ser a menudo visto como un lenguaje de "scripting", es en realidad un lenguaje de programación de propósito general como Lisp o Smalltalk. Hoy, Python es usado para todo, desde scripts que luego se tiran hasta servidores web de alta escalabilidad que proveen servicio ininterrumpido 24x7. Permite crear interfaces de usuario, programar con bases de datos, realizar programación web tanto del lado del servidor como del cliente y testear aplicaciones. Es usado por científicos que escriben aplicaciones para las más rápidas supercomputadoras del mundo y por niños que están aprendiendo a programar.



En este blog, voy a concentrarme en la historia de Python. En particular, cómo Python fue desarrollado, las principales influencias en su diseño, errores cometidos, lecciones aprendidas y futuras direcciones para el lenguaje.



<strong>Reconocimiento:</strong> Estoy en deuda con <a href="http://www.dabeaz.com/">Dave Beazley</a> por muchas de las mejores oraciones en este blog. (Para saber más sobre los orígenes de este blog, vea <a href="http://neopythonic.blogspot.com/2009/01/history-of-python-introduction.html">mi otro blog</a>.)

<h2>Un repaso rápido a Python</h2>

Cuando uno se encuentra con Python por primera vez, a menudo se sorprende de que el código Python se vea, por lo menos superficialmente, similar a código escrito en otros lenguajes de programación convencionales como C o Pascal. Esto no es un accidente; la sintaxis de Python toma mucho prestado de C. Por ejemplo, muchas de las palabras claves de Python (if, else, while, for, etc.) son las mismas que en C, los identificadores en Python tienen las mismas reglas que los de C, y muchos de los operadores estándares tienen el mismo significado que en C. Por supuesto, Python no es C y una de las principales áreas dónde difiere es que en lugar de usar llaves para agrupar sentencias, usa indentación. Por ejemplo, en lugar de escribir sentencias en C como:

<pre lang="c" escaped="true">if (a &lt; B) {

    max = b:

} else {

    max = a;

}</pre>

Python simplemente se deshace de todas las llaves (y de los punto y coma finales) y usa la siguiente estructura

<pre>if a &lt; b:

    max = b

else:

    max = a</pre>

Otra área importante en la que Python se diferencia de los lenguajes del estilo de C es en su uso de tipado dinámico. En C, las variables siempre deben ser declaradas explícitamente y se les debe dar un tipo específico como int o double. Esta información es luego usada para hacer verificaciones estáticas en tiempo de compilación del programa y para reservar memoria para almacenar el valor de las variables. En Python, las variables son simplemente nombres que hacen referencia a objetos. No se necesita declarar las variables antes de que sean asignadas e incluso pueden cambiar de tipo en el medio de un programa. Como otros lenguajes de programación dinámicos, todas las verificaciones de tipo se hacen en tiempo de ejecución por un intérprete en lugar de en un paso de compilación separado.



Los tipos de datos primitivos que vienen con Python incluyen booleanos, números (enteros de máquina, enteros de precisión arbitraria, y números de coma flotante reales y complejos), y cadenas de texto (de 8 bits y Unicode). Estos son todos tipos de datos inmutables, esto significa que los valores son representados por objetos que no pueden ser modificados después de su creación. Los tipos de datos compuestos que viene con el lenguaje incluyen tuplas (arrays inmutables), listas (arrays que pueden cambiar de tamaño) y diccionarios (tablas hash).



Para organizar los programas, Python soporta paquetes (grupos de módulos y/o paquetes), módulos (código relacionado agrupado en un solo archivo fuente), clases, métodos o funciones. Para control de flujo, provee if/else, while y una sentencia for de alto nivel que itera sobre cualquier objeto "iterable". Para el manejo de errores, Python usa excepciones. Una sentencia raise lanza una excepción, y las sentencias try/except/finally especifican manejadores para las excepciones. Las operaciones que vienen con el lenguaje lanzan excepciones cuando se encuentran condiciones de error.



En Python, todos los objetos que pueden ser nombrados son llamados "de primera clase". Esto significa que funciones, clases, métodos, módulos y todos los otros objetos nombrados pueden ser libremente pasados como parámetros, inspeccionados y almacenados en distintas estructuras de datos (por ejemplo, listas o diccionarios) en tiempo de ejecución. Y hablando de objetos, Python también tiene soporte completo para programación orientada a objetos; incluyendo clases definidas por el usuario, herencia y asociación de métodos en tiempo de ejecución.



Python tiene una extensa librería estándar, la cual es una de las razones de su popularidad. La librería estándar tiene más de 100 módulos y siempre está evolucionando. Alguno de estos módulos incluyen expresiones regulares, funciones matemáticas típicas, hilos, interfaces con sistemas operativos, redes, protocolos estándares de Internet (HTTP, FTP, SMTP, etc.), manejo de email, procesamiento de XML, procesamiento de HTML y toolkits para GUI (Tcl/Tk).



Además, hay una gran cantidad de módulos y paquetes provistos por terceros, muchos de los cuales también son open source. Aquí uno puede encontrar frameworks web (¡muchos como para listarlos!), más toolkits para GUI, librerías numéricas eficientes (incluyendo wrappers para muchos paquetes populares escritos en Fortran), interfaces con bases de datos relacionales (Oracle, MySQL y otras), SWIG (una herramienta para hacer que librerías C++ estén disponibles como módulos Python), y mucho más.



Un atractivo principal de Python (y de otros lenguajes de programación dinámicos en ese aspecto) es que tareas que parecen complicadas a menudo pueden ser expresadas con muy poco código. Por ejemplo, aquí hay un script en Python simple que obtiene una página web, la revisa buscando referencias a URLs, e imprime las primeras 10.

<pre># Scan the web looking for references



import re

import urllib



regex = re.compile(r'href="([^"]+)"')



def matcher(url, max=10):

    "Print the first several URL references in a given url."

    data = urllib.urlopen(url).read()

    hits = regex.findall(data)

    for hit in hits[:max]:

        print urllib.basejoin(url, hit)



matcher("http://python.org")</pre>

Este programa puede ser modificado fácilmente para hacer un web crawler, y en efecto Scott Hassan me ha dicho que escribió el primer web crawler de Google en Python. Hoy, Google emplea millones de líneas de código Python para manejar muchos aspectos de sus operaciones, desde automatización a manejo de avisos (Descargo: en la actualidad soy un empleado de Google.)



Por debajo, Python es implementado como una combinación de intérprete y compilador a bytecode. La compilación es llevada a cabo implícitamente cuando los módulos son cargados, y muchas primitivas del lenguaje necesitan que el compilador esté disponible en tiempo de ejecución. A pesar de que la implementación de referencia de Python está escrita en C, y está disponible para cada plataforma de hardware/software existente, muchas otras implementaciones se han vuelto populares. Jython es una versión que corre sobre la JVM y tiene integración con Java. IronPython es una versión para la plataforma .NET de Microsoft que tiene una integración similar con otros lenguajes que corren sobre la plataforma .NET. PyPy es un compilador/intérprete de Python escrito en Python (aún un proyecto de investigación, financiado con fondos de la UE). También está Stackless Python, una variante de la implementación en C que reduce la dependencia del stack de C para llamadas a funciones/métodos, para permitir co-rutinas, continuations y micro hilos.



<em>Traducido por Juan José Conti.

Revisado por César Portela.

Si encontrás errores en esta traducción, por favor reportalos en un comentario y los corregiremos a la brevedad.</em>

Todas las traducciones de esta serie pueden encontrarse en <a href="/categoria/aprendiendo-python/historia/" target="_self">La historia de Python</a>.</body></html>