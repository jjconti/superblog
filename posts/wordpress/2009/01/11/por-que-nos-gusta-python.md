<html><body><em>El siguiente texto era parte del informe del proyecto final de carrera de Juan José Conti y Cecilia Lorena Puccinelli, titulado <strong>Desarrollo Ágil de un Sistema de Gestión de Negocios Inmobiliarios con Software Libre</strong>. Finalmente no fue incluido en la versión definitiva del mismo por lo que lo rescatamos en este blog.</em>

<!--more-->

<h2>Python</h2>

Python es un lenguaje de programación de propósito general de alto nivel. Su filosofía de diseño hace énfasis en lograr productividad para los programadores y legibilidad del código.



Fue creado en el año 1990 por Guido Van Rossum y desde entonces ha sido desarrollado como un proyecto del Software Libre por desarrolladores alrededor del mundo.



A menudo es comparado con lenguajes como C, Java, Perl y Lisp, pero tiene muchas características distintivas que marcan su identidad propia:

<h3>Intérprete interactivo</h3>

Python viene acompañado de un intérprete interactivo o read-eval-print-loop que permite agilizar el desarrollo de programas ya que se pueden probar ideas y rápidamete ver como resultan sin necesidad de escribir un programa entero en el cual envolverla. Otros lenguajes como Smalltalk, Haskell o Scheme también tienen esta herramienta.



El siguiente es un ejemplo sencillo de uso del intérprete interactivo, los comandos ingresados por el usuario están precedidos por &gt;&gt;&gt;:



<code>&gt;&gt;&gt; 1 + 2</code>

<code>3</code>

<code>&gt;&gt;&gt; "hola"</code>

<code>'hola'</code>

<code>&gt;&gt;&gt; nombre = "fabio"</code>

<code>&gt;&gt;&gt; "hola " + nombre</code>

<code>'hola fabio'</code>

<h3>Tipos de datos poderosos</h3>

Python incluye de forma nativa tipos de datos poderosos muy útiles a la hora de programar. Las listas y tuplas son secuencias de objetos:



<code>lista = [1,2,3, “cuatro”, Cliente()]</code>

<code>tupla = ('u', 1, 3)</code>



Ambos tipos de datos pueden almacenar cualquier tipo de objetos en orden. La principal diferencia entre estos dos tipos de datos es que las listas pueden cambiar en forma dinámica su tamaño mientras que las tuplas son de tamaño fijo (se dice que es un objeto inmutable, como los números o cadenas de texto).



Los diccionarios son una estructura de datos sin orden que permite almacenar valores asociados a una clave para luego poder recuperarlos a partir de esta. Solo objetos inmutables pueden ser clave de un diccionario.



<code>dicc = {'a': 1, 'b': 10}</code>

<code>dicc['a']</code> obtiene el objeto 1

<code>dicc[3] = ‘tres’</code> agrega al diccionario el objeto ‘tres’ asociado a la clave 3 .

<h3>Espacios en blanco con significado</h3>

En Python los bloques se delimitan mediante el uso de indentación en lugar de utilizar llaves:



<pre class="code">if carteles == 0:

    print “No hay carteles disponibles.”

else:

    print “Hay %d carteles disponibles.” % carteles</pre>



Esto tiene como objetivo forzar una correcta indentación que redunde en una mayor legibilidad del código escrito.



<pre>i = 20

while i &gt; 0:

    print i

    i -= 1

</pre>

<h3>Tipado de pato</h3>

El nombre <a href="http://en.wikipedia.org/wiki/Duck_typing" target="_blank">tipado de pato</a> surge de la idea: “si un objeto camina como pato y come como pato, entonces debe ser un pato”.



Las restricciones de tipo no son checkeadas en tiempo de compilación, sino que las operaciones sobre los objetos siempre se intentan llevar a cabo y fallan en tiempo de ejecución si el objeto no puede responder al mensaje que se le envió.



Supongamos que definimos la función saludar como sigue:



<pre>def saludar(o):

    print “hola %s“ % o.nombre</pre>



A esta función no lo interesa el tipo del objeto o, recibido como parámetro, lo único que le importa es que tenga el atributo nombre.



Así, si la variable m referencia un objeto de la clase Mujer y la variable h referencia un objeto de la clase Hombre y ambas clases tienen un atributo llamado nombre, entonces las siguientes llamadas se ejecutarán sin problemas:



<code>saludar(m)</code>

<code>saludar(h)</code>



Si la variable ‘a’ referencia a un objeto de la clase Anonimo y ésta no tiene un atributo llamado nombre, la llamada a:



<code>saludar(a)</code> lanzará una excepción.

<h3>Librería estándar amplia</h3>

<img class="size-medium wp-image-1117" title="python_batteries_included" src="/wp-content/uploads/2009/01/python_batteries_included-300x128.jpg" alt="Python viene con las baerías incluidas!" width="300" height="128">



Al igual que Java, Python cuenta con una amplia librería estándar que acompaña al lenguaje. Ésta incluye módulos para manejar expresiones regulares, crear interfaces gráficas, conectarse a bases de datos entre muchos otros.



Ésta es una de sus mayores ventajas y a esto se debe la popular expresión “Python viene con las baterías incluidas”.

<h3>Librerías externas</h3>

Además de los muchos componentes incluidos en la librería estándar de Python, hemos utilizando algunas librerías externas:

<ul>

	<li>PIL: librería 	para manejo de imágenes.</li>

	<li>Pysicopg: conector 	para el motor de bases de datos PostgreSQL.</li>

	<li>ReportLab: librería 	para generar documentos PDF.</li>

	<li>BeautifulSoap: librería para procesar documentos HTML. Su uso es descrito en la sección 1.1.37.</li>

	<li>Pynum2word: módulo 	que convierte números en palabras.</li>

</ul></body></html>