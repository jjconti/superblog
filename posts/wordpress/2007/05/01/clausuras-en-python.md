<html><body><p>Hace unos días leí <a title="Ruby at Smaldone" href="http://blog.smaldone.com.ar/2007/04/26/el-secreto-de-ruby-las-clausuras/" target="_blank">este post</a> en el blog de <a title="Smaldone" href="http://blog.smaldone.com.ar/" target="_blank">Javier Smaldone</a>.

</p><blockquote><strong>Closures:</strong> Essentially a closure is a block of code that can be passed as an 	argument to a function call.</blockquote>

Como parte de la didáctica Javier iba mostrando ejemplos que resolvía con algún lenguaje sin Clausuras (como Java o PHP) y con Ruby (el post trata sobre las Clausuras como una fortaleza de Ruby). Mientras leía fuí resolviendo los mismos ejemplos en Python y los dejé en forma de comentos. Como la identación no salió muy bien, los reproduzco aca:



<!--more--> <strong>Juanjo:</strong>

Las que siguen son soluciones en Python de los ejemplos que planteaste, algunas usan clausuras, otros puede que no :)



El ejemplo simple:

<blockquote>Supongamos que deseamos escribir una función que tome como parámetro un arreglo de valores enteros y retorne otro arreglo, producto de multiplicar por 2 cada uno de los elementos del parámetro.</blockquote>

<pre>def f(a):

    return [2*x for x in a]</pre>

El ejemplo de people:

<blockquote>Supongamos ahora que tenemos una clase "<code>Person</code>", cuyo método "<code>age</code>" calcula la edad de la persona. Si tenemos una colección de personas en el arreglo "<code>people</code>" y deseamos obtener sólo aquellas que son mayores de 18 años.</blockquote>

<pre>[p.name for p in people if p.age &gt; 18]</pre>

Problema 1:

<blockquote>Convertir las cadenas de un arreglo a mayúsculas.</blockquote>

<pre>a = [x.upper() for x in a]</pre>

Problema 2:

<blockquote>Dado un arreglo de la forma <code>[["nombre", "apellido"]]</code>, obtener un arreglo de la forma <code>["apellido, nombre"]</code>. Por ejemplo, dado:

<blockquote><code>[["Javier","Smaldone"],["Santiago","Lobos"],["Bon","Scott"]]</code></blockquote>

obtener:

<blockquote><code>["Smaldone, Javier", "Lobos, Santiago", "Scott, Bon"]</code></blockquote>

</blockquote>

<pre>[”, “.join([y,x]) for [x,y] in a]</pre>

Problema 3:

<blockquote>Listar los nombres de las personas mayores de edad y mostrar la edad promedio de las mismas (según el ejemplo planteado anteriormente).</blockquote>

Este no quedó tan bien como los otros, pero te dejo mi interacción en REPL de Python:

<pre>&gt;&gt;&gt; p1 = Persona()

&gt;&gt;&gt; p1.age = 19

&gt;&gt;&gt; p1.name = “Juan Hewr”

&gt;&gt;&gt; p2 = Persona()

&gt;&gt;&gt; p2.age = 2

&gt;&gt;&gt; p2.name = “Baby Jones”

&gt;&gt;&gt; p3 = Persona()

&gt;&gt;&gt; p3.age = 30

&gt;&gt;&gt; p3.name = “Sussan Ahoria”

&gt;&gt;&gt; people = [p1, p2, p3]



&gt;&gt;&gt; s = 0.0

&gt;&gt;&gt; adults = [p for p in people if p.age &gt; 18]

&gt;&gt;&gt; for p in adults:

print p.name

s += p.age

Juan Hewr

Sussan Ahoria

&gt;&gt;&gt; print s/len(adults)

24.5</pre>

Problema 4:

<blockquote>Dado un arreglo de cadenas, obtener la de mayor longitud.</blockquote>

<pre>max(cadenas)</pre>

<strong>Javier:</strong>



Muchas gracias Juanjo por las soluciones.

Con respecto al problema 4, un detalle:

En Ruby también puedes obtener el máximo elemento de un arreglo ‘a’ usando

a.max

Sin embargo, la idea era mostrar como aplicar una función al estilo del ‘fold’ de los lenguajes funcionales. ¿Podrías reescribir la solución en esos términos?



<strong>Juanjo:</strong>



Primero una aclaración de algo que me pasé por alto: max(a) en Python cuando a es una lista de strings no da el string más largo sino el que está más al final en un ordenamiento creciente alfabético estando las minúsculas después que las mayúsculas. Es así también en ruby?

<pre>

&gt;&gt;&gt; max(”hola”, “juanjo”)

‘juanjo’

&gt;&gt;&gt; max(”hola”, “Juanjo”)

‘hola’

&gt;&gt;&gt; max(”a”, “A”)

‘a’

&gt;&gt;&gt; max(”a”, “AAAAAAAAAAAAAAAAAAAAAa”)

‘a’

&gt;&gt;&gt; max(”a”, “AAAAAAAAAAAAAAAAAAAAA”, “a”)

‘a’

&gt;&gt;&gt; max(”AAAAAAAAAAAAAAAAAAAAA”, “a”)

‘a’

&gt;&gt;&gt; max(”b”, “a”)

‘b’

&gt;&gt;&gt; max(”B”, “a”)

‘a’

</pre>

<strong>Javier:</strong>



Así es, Juanjo. Yo también me equivoqué. max, aplicado a strings devuelve el máximo según el orden lexicográfico, y no según la longitud.



Me sigue quedando la duda. ¿Hay algo similar a ‘inject’ o ‘fold’ en Python?



<strong>Juanjo:</strong>



Ahora si vamos a intentar resolver el ejemplo 4 en Python:



Mmm inject está bueno para resolver ese problema.. pero creo que no tenemos algo así en Python. Intentemos de todas formas:



Tenemos una lista de strings:

<pre>a = [”hola”, “juAnjO”, “Argentina”, “8″]</pre>

Una función ‘criterio’:

<pre>def longer(a, b):

    if len(a) &gt; len(b):

        return a

    else:

        return b</pre>

And this magic functions called ‘mas’:

<pre>def mas(l, c, v):

    if l:

        return mas(l[1:], c, c(l[0], v))

    else:

        return v</pre>

Que nos va a permitir hacer algo como esto:

<pre>&gt;&gt;&gt; mas(a, longer, “”)

‘Argentina’</pre>

Mirando desde más cerca.. esta función ‘mas’, es muy parecida a ‘inject’, salvo por el nombre :)

<pre>&gt;&gt;&gt; inject = mas

&gt;&gt;&gt; numeros = [1,2,3,4,5,6]

&gt;&gt;&gt; def suma(a, b):

    return a + b

&gt;&gt;&gt; inject(numeros, suma, 0)

21</pre>

Mmm parece que funciona, comprobemoslo:

<pre>&gt;&gt;&gt; sum(numeros)

21</pre>

Si!



Nos leemos!</body></html>