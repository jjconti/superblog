<html><body><p>Ayer llevé acabo un <a href="http://en.wikipedia.org/wiki/Code_refactoring" target="_blank">refactoring</a> importante en mi proyecto <a href="http://svn.juanjoconti.com.ar/dyntaint/" target="_blank">Taint Mode para Python</a>.



En resumen: <a href="http://svn.juanjoconti.com.ar/dyntaint/dyntaint.py" target="_blank">dyntaint.py</a> es un módulo que permite seguirle la huella a datos que ingresan a un programa con el objetivo de evitar que lleguen a ciertas áreas sensibles. Por ejemplo, <strong>que "42 or 1=1" no llegue a una consulta SQL que se ejecutará contra una base de datos</strong>.



Si lo anterior no te dice nada, te recomiendo que leas mi <a title="Taint Mode en Python: cómo encontrar vulnerabilidades mediante el uso de variables manchadas" href="http://www.juanjoconti.com.ar/2009/09/07/charla-taint-mode-en-python/" target="_blank">presentación sobre el tema</a>.



Hasta hoy, el registro de qué variables estaban manchas con qué tipo de manchas en una corrida del programa se llevaba en una estructura de datos auxiliar llamada TAINTED. Básicamente un <a href="http://docs.python.org/tutorial/datastructures.html#dictionaries" target="_blank">diccionario</a> en el cual cada clave se corresponde con un tipo de mancha (o vulnerabilidad), y cada valor es un <a href="http://docs.python.org/tutorial/datastructures.html#sets" target="_blank">conjunto</a> de variables manchadas con el tipo de mancha de la clave correspondiente.



El refactoring consistió en cambiar de este esquema a uno en el cual cada variable manchada tiene un atributo (taints) que es un conjunto de identificadores de manchas. Entonces si antes tenía algo como:

</p><pre>{XSS: set(['manchado1', 'manchado2']),

SQLI: set(['manchado1'])}</pre>

ahora tengo:

<pre>&gt;&gt;&gt; manchado1.taints

set([XSS, SQLI])</pre>

<pre>&gt;&gt;&gt; manchado2.taints

set([XSS])</pre>

La revisión 59 también incluye algunas otras limpiezas. Para ver los cambios:

<pre>svn diff -r 58:59 http://svn.juanjoconti.com.ar/dyntaint/</pre>

Después de hacer las modificaciones necesarias, y corregir errores, las pruebas corren ok:

<pre>Ran 84 tests in 0.006s



OK</pre>

Podemos discutir los cambios en los comentarios.</body></html>