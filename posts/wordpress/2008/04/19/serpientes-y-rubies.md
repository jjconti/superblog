<html><body><p>Ja! Levanto el guante del desafío que <a href="http://gastonramos.wordpress.com/2008/04/19/snakes-and-rubies/" title="Gastón Ramos" target="_blank">plantea Gastón en su blog</a>:

</p><pre>

juanjo@albus:~$ python

Python 2.5.1 (r251:54863, Mar  7 2008, 03:41:45)

[GCC 4.1.2 (Ubuntu 4.1.2-0ubuntu4)] on linux2

Type "help", "copyright", "credits" or "license" for more information.

</pre><!--more-->1. Dado un array con nombres de persona eliminar los nombre que comienzan con “Pe”:

<pre>

&gt;&gt;&gt; nombres = ['Pablo', 'Raul', 'Pedro', 'Pepe', 'Ariel', 'TerePe']

&gt;&gt;&gt; [n for n in nombres if not n.startswith("Pe")]

['Pablo', 'Raul', 'Ariel', 'TerePe']

</pre>

2. Verificar si el mismo array contiene el nombre “Raul”:

<pre>

&gt;&gt;&gt; "Raul" in nombres

True

</pre>

3. Generar un string con todos los nombres unidos por “-”:

<pre>

&gt;&gt;&gt; "-".join(nombres)

'Pablo-Raul-Pedro-Pepe-Ariel-TerePe'

</pre>

4. Generar un segundo array con los nombres todos en minúsculas ordenado alfabéticamente:

<pre>

&gt;&gt; sorted([n.lower() for n in nombres])

['ariel', 'pablo', 'pedro', 'pepe', 'raul', 'terepe']

</pre>

5. Desordenar el array:

<pre>

&gt;&gt;&gt; from random import shuffle

&gt;&gt;&gt; shuffle(nombres)

&gt;&gt;&gt; nombres

['Pepe', 'Pedro', 'Ariel', 'Raul', 'Pablo', 'TerePe']

</pre>

6. Averiguar si la lista siguiente tiene números pares:

<pre>

&gt;&gt;&gt; bool([n for n in numeros if n % 2 == 0])

True

</pre>

7. Averiguar si toda la lista son números pares:

<pre>

&gt;&gt;&gt; len(numeros) == len([n for n in numeros if n % 2 == 0])

False

</pre>

8. Obtener el producto de una lista de números:

<pre>

&gt;&gt;&gt; f = lambda x,y: x*y

&gt;&gt;&gt; reduce(f, numeros)

120

</pre>

9. Obtener el factorial de 9999:

<pre>

&gt;&gt;&gt; reduce(f, xrange(1, 10000))

# la respuesta tiene 35656 caracteres.

</pre>

10. Averiguar si dos arrays son iguales:

<pre>

&gt;&gt;&gt; [1,2,3,4] == [1,2,3,4]

True

</pre>

¿Conclusiones? Creo que las listas por comprensión de la serpiente le gana a los .metodos del rubí. Pero en 6 y 7 perdemos feo :-/ ¿Algún pythonista que reescriba esos ejercicios?</body></html>