<html><body><p>Bidirectional dict o <a href="http://en.wikipedia.org/wiki/Injective_mapping" target="_blank">Injective mapping</a> es una estructura de datos muy útil.



Por lo general cuando usamos un diccionario o tabla hash, tenemos un valor asociado a una clave:

</p><pre>&gt;&gt;&gt; d = {1:'uno', 2:'dos'}

&gt;&gt;&gt; d[1]

'uno'</pre>

Pero algunas veces también resulta útil indexar por el valor y obtener la clave.

<pre lang="python" escaped="true">&gt;&gt;&gt; d['uno']

1</pre>

Por ejemplo, en un programa tengo un archivo de configuración que contiene un diccionario dónde las claves son strings de 3 caracteres representando un edificio ('SFE', 'GDP', ...) y las claves números de puerto (5007, 5008, ...). En algunas partes el programa requiere conocer el edificio a partir del número de puerto y en otras el puerto a partir del edificio.

<h2>¿Cómo obtenemos este comportamiento?</h2>

Pregunté en <a href="http://stackoverflow.com/questions/3318625/efficient-bidirectional-hash-table-in-python" target="_blank">StackOverflow</a> y si bien me apuntaron a una <a href="http://pypi.python.org/pypi/bidict/" target="_blank">implementación</a>, la solución que más me gustó fue esta:



<pre>&gt;&gt;&gt; d.update( dict((d[k], k) for k in d))</pre>



Así se ve <code>d</code> ahora: <pre>{1: 'uno', 2: 'dos', 'uno': 1, 'dos': 2}</pre>



Y podemos efectivamente indexar por clave o por valor:



<pre>&gt;&gt;&gt; d[1]

'uno'

&gt;&gt;&gt; d['uno']

1

</pre>

<h2>Advertencias</h2>

<h3>No se pueden usar objetos mutables</h3>

En los diccionarios de Python <a href="http://www.python.org/doc/faq/es/general/#por-qu-las-claves-de-los-diccionarios-deben-ser-inmutables" target="_blank">solo objetos inmutables pueden ser clave de diccionarios</a>, por lo tanto, en nuestro diccionario bidireccional, tanto las claves como los valores deberán serlo.

<h3>Actualizaciones</h3>

Otra limitación de este enfoque son las desincronizaciones que puede sufrir al modificar el <em>bidict</em> luego de realizar la transformación; hay que tener cuidado!

<ul>

	<li>Luego de agregar un nuevo elemento debemos volver a ejecutar la línea mágica para que cree la entrada inversa.</li>

	<li>No podemos agregar un par que tenga como clave algo que ya existía como valor o que tenga como valor algo que ya existía como clave.</li>

	<li>Si borramos una entrada, hay que también borrar su inversa.</li>

</ul>

<h2>Conclusión personal</h2>

Como les contaba antes, yo estaba usando el diccionario original en un archivo de configuración, por lo que no toco la estructura de datos durante la ejecución del programa, así que esta solución compacta y elegante... como dijo el filósofo: <strong>me viene al pelo!</strong>



Espero a alguien más le sirva.</body></html>