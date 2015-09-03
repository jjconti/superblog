<html><body><p>Hace un par de días Walter de Nicaragua me consultaba:

</p><blockquote>Estoy trabajando en una aplicacion para niños en las xo´s , estoy usando sqlite3 para guardar la informacion, y tambien necesito guardar fotos dentro de la base de datos.



Como la fotos seran tomadas con la camara de las propias XO's, asumo no son tan grande en resolucion y tamaño.



Tambien, estuve revizando la lista de correo, pero no hay nada concreto, y  a decir verdad recomiendan que guarde una referencia de la imagen en la base de datos, y luego haga una consulta, para recuperarla, pero tambien he visto que tiene sus pro y sus contras.</blockquote>

Esta es la respuesta. Primero necesitamos una tabla con un campo de tipo BLOB donde guardar la imagen:

<pre>&gt;&gt;&gt; import sqlite3

&gt;&gt;&gt; conn = sqlite3.connect('/tmp/example')

&gt;&gt;&gt; c = conn.cursor()

&gt;&gt;&gt; c.execute('''create table imagenes (imagen BLOB);''')

</pre>

Abro una imagen que tengo en disco, mismo directorio que donde ejecute

el intérprete de Python, la cargo en memoria y la guardo en la base.

<pre>&gt;&gt;&gt; imgdata = open('tomyNarnia.jpg', 'r').read()

&gt;&gt;&gt; len(imgdata)

1613949

&gt;&gt;&gt; buff = sqlite3.Binary(imgdata)

&gt;&gt;&gt; c.execute('insert into imagenes values(?);', (buff,))

&gt;&gt;&gt; conn.commit()

&gt;&gt;&gt; conn.close()

</pre>

Luego podemos cerrar el intérprete. Con sqlite3 importado, recuperamos

la imagen.

<pre>&gt;&gt;&gt; conn = sqlite3.connect('/tmp/example')

&gt;&gt;&gt; c = conn.cursor()

&gt;&gt;&gt; a = c.execute('select imagen from imagenes')

&gt;&gt;&gt; img = a.fetchone()

&gt;&gt;&gt; len(img)

1

&gt;&gt;&gt; img

(&lt;read-write buffer ptr 0x1c75d60, size 1613949 at 0x1c75d20&gt;,)

</pre>

El resultado es una tupla, pero como seleccionamos un solo campo de la

tabla, hay un solo elemento.

<pre>&gt;&gt;&gt; img = img[0]

&gt;&gt;&gt; len(img)

1613949

</pre>

Finalmente lo escribimos en una imagen.

<pre>&gt;&gt;&gt; f = open('newimage.jpg', 'w')

&gt;&gt;&gt; f.write(img)

&gt;&gt;&gt; f.close()

</pre></body></html>