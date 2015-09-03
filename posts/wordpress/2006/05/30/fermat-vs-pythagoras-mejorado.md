<html><body><p>Logré bajar la complejidad de <a href="http://firebirds.com.ar/~juanjo/wordpress/2006/05/29/fermat-vs-pythagoras/">mi solución de un orden cúbico</a> a un orden cuadrático, la diferencia en cuanto a tiempo de ejecución requerido es sorprendente:



<img id="image88" src="http://firebirds.com.ar/%7Ejuanjo/wordpress/wp-content/uploads/2006/05/pytagoras2.png" alt="comparacion de 3 soluciones">



Pero todavía no e suficiente, con un N igual a 10000 la respuesta se obtiene luego de 10 minutos (en mi computadora de 700 Mhz).

<!--more-->

En esta solución ya no uso la función <code>pythagoras(x,y,z)</code>. Solo hay 2 ciclos <code>for</code> anidados y el valor de z se calcula como <code>z = sqrt( pow(x,2) + pow(y,2) )</code>. Si z es entero, se tiene un triplete válido y solo falta verificar si x,y,z son primos relativos.



</p><pre>def is_int(i):

    return i == int(i)



def solv106f(N):

    miembros = []

    tripletes_rprim = 0

    for x in range(1,N-1):

        for y in range(x+1,N):

            z = sqrt( pow(x,2) + pow(y,2) )

            if (is_int(z) and z &lt;= N):

                for a in [x,y,z]:

                    if a not in miembros:

                        miembros.append(a)

                if (rprim(x,y,z)):

                    tripletes_rprim +=1



    no_miembros = N - len(miembros)

    return N, tripletes_rprim, no_miembros

</pre></body></html>