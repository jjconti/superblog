<html><body><p>Otra cosa que leí es el apéndice A de <a href="http://gnosis.cx/TPiP">TPiP </a>: <a href="http://gnosis.cx/TPiP/appendix_a.txt">A Selective and Impressionistic Short Review of Python</a>. Encontré muchas cosas interesantes que no conocía y encontré algunas cosas sobre programación funcional que estaba buscando: funciones anónimas, lambda, map, filter y reduce... siga leyendo!



<!--more-->



<strong>Funciones anónimas:</strong>



Python toma de la programación funcional la posibilidad de definir funciones anónimas,

la desventaja de estas es que solo las podremos usar una vez, no podemos invocarlas por su nombre, no tienen :-)



Pero justamente esta es la idea, no tener que definir funciones (simples) que solo se usaran una vez, para usar por 

ejemplo (aquí es donde las estoy usando) en funciones que esperan funciones como algunos de sus argumentos (ej: map, filter)



Estas fucniones no pueden (de forma natural) ejecutar más de una sentencia.



Ejemplos para probar en el intérprete:



Ejemplo 1:

</p><pre>

&gt;&gt;&gt; lambda x: x+1 # x es el argumento de la función anónima

_function _lambda_ at 0x40219e2c_</pre>



Si bien la función fue definida, ya no podemos usarla, no tenemos como referenciarla.



Ejemplo 2:



<pre>&gt;&gt;&gt; map(lambda x: x+1, [0, 1, 2, 3])

[1, 2, 3, 4]</pre>



Ejemplo 3: una forma de darle un nombre a una función definida mediante 'lambda'



<pre>&gt;&gt;&gt; nombre = lambda x: x+1

&gt;&gt;&gt; nombre(5)

6

</pre>



<strong>map, filter y reduce:</strong>



Escribí un script con ejemplos sobre estas funciones: <a href="../../../../files/python/funcionesPF.py.html">funcionesPF.py</a></body></html>