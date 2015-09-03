<html><body><p>Cuando empecé a cursar Ingeniería en Sistemas en el año 2003, tuvimos una materia llamada Algoritmos y Estructuras de Datos. La semana del curso estaba compuesta por una clase teórica, una clase práctica y una clase "especial" dictada por un docente de apellido Marina que tenía como objetivo hacernos pensar resolviendo problemas; en las primeras clases ni siquiera programábamos.

El lenguaje de programación de la materia era C y en una de las clases, este docente recordaba risueño que un alumno había querido intercambiar el valor de dos variables

</p><pre lang="c">int a = 1;

int b = 2;</pre>

haciendo:

<pre lang="c">a = b;

b = a;</pre>

El error es evidente; en a se copia el valor contenido en b (2) pisando el valor original (1) y al ejecutarse la segunda sentencia, el nuevo valor de a (2) es copiado en b.

<p style="text-align: left;">La siguiente tabla muestra los valores que van tomando las variables a y b:

<img class="aligncenter size-full wp-image-1547" title="ej1f" src="/wp-content/uploads/2009/05/ej1f.jpg" alt="" width="389" height="185">

La forma correcta de intercambiar los valores habría sido utilizando una variable auxiliar en la cual mantener uno de los valores:

</p><pre lang="c">int aux;

int a = 1;

int b = 2;

aux = a;

a = b;

b = aux;</pre>

La siguiente tabla muestra los valores que van tomando las variables aux, a y b:

<img class="aligncenter size-full wp-image-1552" title="ej2ff" src="/wp-content/uploads/2009/05/ej2ff.jpg" alt="" width="500" height="233">

Lo gracioso del asunto es que unos años más tarde conocí otro lenguaje de programación, <a href="http://www.python.org/" target="_blank">Python</a>.



<!--more-->



En Python un tipo de dato que viene con el lenguaje es la tupla. Una tupla es una secuencia (sus elementos tienen orden) inmutable (no se puede cambiar su tamaño o contenido) que puede tener dentro objetos de distinto tipo. Un ejemplo de tupla en Python (contiene tres números y dos cadenas de texto):



<pre>(1, 2, "tres", 4, "Juan")</pre>



La forma de apuntar a ese objeto desde una variable es simplemente:



<pre>a = (1, 2, "tres", 4, "Juan")</pre>



Aunque podemos obviar los paréntesis y de todas formas funcionará. Decimos que la tupla es <em>empaquetada</em>:



<pre>a = 1, 2, "tres", 4, "Juan"</pre>



De forma similar, podemos <em>desempaquetar</em> la tupla en nuevas variables:



<pre>b, c, d, e, f = a</pre>



La condición es que el número de variables en el lado izquierdo del operador = coincida con el número de elementos en la tupla.



La siguiente sentencia, empaqueta y desempaqueta:

<pre>x, y, z = "Juan", 100, 1</pre>



Y es equivalente a:

<pre>x = "Juan"

y = 100

z = 1</pre>



Finalmente, esta propiedad del lenguaje nos permite intercambiar rápidamente los valores de 2 (o n) variables:

<pre>a = 1

b = 2

a, b = b, a</pre>

<a href="/wp-content/uploads/2009/05/ej31.jpg"><img class="aligncenter size-full wp-image-1544" title="ej31" src="/wp-content/uploads/2009/05/ej31.jpg" alt="" width="389" height="159"></a>

Así, lo que un alumno despistado quiso hacer en 2 sentencias y Marina mostró que se hacía correctamente en 3, yo lo hago en 1 :)</body></html>