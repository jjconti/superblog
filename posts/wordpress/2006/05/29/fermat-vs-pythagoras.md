<html><body><p>Esta es mi solución al problema número 6 de una <a title="problemset" href="http://acm.uva.es/problemset/" target="_blank">larga lista de problemas de programación</a>. A pesar de que, como estudiante de Ingeniería, pasé los últimos 3 años y medio estudiando distintas formas de las matemáticas, no conocí el <a title="Último Teorema de Fermat" href="http://es.wikipedia.org/wiki/%C3%9Altimo_teorema_de_Fermat" target="_blank">Último Teorema de Fermat</a> hasta que mi amigo Joel, estudiante de Filosofía, me lo comentó.



El problema en realidad no tiene mucho que ver con Fermat, pero sí con Pitágoras: dado un valor N, hay que encontrar <em>cuántos</em> tripletes x,y,z satisfacen <strong>x² + y² = z² </strong>tales que

</p><ul>

	<li>x,y,z sean menores o iguales a N</li>

	<li>x,y,z sean primos relativos (es decir que 1 es su único divisor común)</li>

	<li>x &lt; y &lt; z</li>

</ul>

Además hay que encontrar <em>cuántos</em> números mayores que 0 y menores o iguales a N no pertenecen a ninguno de los tripletes (no solo a los tripletes de primos relativos).



El enunciado original <a href="http://acm.uva.es/p/v1/106.html">aquí</a>.

<!--more-->

Una posibilidad sería explorar exasutivamente todas las combinaciones de números x,y,z menores o iguales a N, y para cada uno verificar si cumplen las características pedidas. Pero esto sería de altísima complejidad, sería de orden cúbico. Hay que pensar una mejor solución.



Empecemos con una función que dado 3 valores x,y,z me diga si satisfacen el Teorema de Pitágoras:

<code> </code>

<pre>from math import pow



def pythagoras(x,y,z):

    return (pow(x,2)+pow(y,2) == pow(z,2))

</pre>

<pre>

&gt;&gt;&gt; pythagoras(3,4,5)

True

&gt;&gt;&gt; pythagoras(1,1,1)

False

&gt;&gt;&gt; pythagoras()

True

</pre>

También necesito una función, que dado 3 valores x,y,z me diga sin son primos relativos entre sí:

<code> </code>

<pre>def mcd(a,b): # algoritmo de euclides

    if (a == b): return a

    elif (a &lt; b): a,b = b,a # a es el más grande

    while(b != 0):

        r = a % b

        a = b

        b = r

        return a



def rprim(x,y,z):

    return (mcd(mcd(x,y),z) == 1)

</pre>

La solución que explora todas las combinaciones de 3 números constaría de 3 ciclos <code>for</code> anidados y en el curerpo del más profundo se haría las preguntas pertitenes a la resolución del problema: ¿ese triplete satisface el teorema de pitagoras? ¿son primos relativos? ¿x&lt;y&lt;z?



<pre>for(x=1;x=&lt;N;x++)

    for(y=1;y=&lt;N;y++)

        for(z=1;z=&lt;N;z++)

            # ¿...?

</pre>

Una de las condiciones es que x&lt;y&lt;z, esto permite una redefinición tal que NO se exploren todas las combinaciones de 3 números menores que N sino solo las combinaciones que cumplen con esta restricción:



<pre>for(x=1;x=&lt;N-2;x++)

    for(y=x+1;y=&lt;N-1;y++)

        for(z=y+1;z=&lt;N;z++)

            # ¿..?

</pre>

¿Esta solución es buena o no es mucho mejor a una en la que todos los ciclos <code>for</code> vayan de 1 a N y por cada uno se pregunte si x,y,z?



En el archivo <a href="http://firebirds.com.ar/~juanjo/wordpress/files/pp/pythagoras.py.html">pythagoras.py</a> están definidas dos funciones: <code>solv106s(N)</code>, basada en la primera aproximación y <code>solv106(N)</code> que <em>espera</em> ser mejor.



Este programita sirve para medir el tiempo de las dos ejecuciones y compararlos.



<pre>import timing



def test(N=1000):

    timing.start()

    solv106s(N)

    timing.finish()

    print "la primer solución tardo " + str(timing.seconds()) + " segundos"

    timing.start()

    solv106(N)

    timing.finish()

    print "la segunda solución tardo " + str(timing.seconds()) + " segundos"

</pre>

Hago una prueba con un valor relativamente grande, N=1000 el valor por defecto:



<pre>&gt;&gt;&gt; test()

la primer solución tardo  1879 segundos

la segunda solución tardo 1561 segundos

</pre>

31 minutos contra 26 minutos.. no me parece una diferencia muy grande. Nota: mi máquina es un AMD K6 II de 700 Mhz.



Esta gráfica compara las dos soluciones luego de haberlas probado con diferentes valores de N, obtenido unos puntos e interpolar una curva representativa:



<img id="image87" title="comparacion" src="http://firebirds.com.ar/%7Ejuanjo/wordpress/wp-content/uploads/2006/05/comparacion106.png" alt="comparacion" align="middle">



mmm, hay que pensar una mejor solución.</body></html>