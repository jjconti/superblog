<html><body><p>Este mes, cuando empecé a escribir código Python y quise publicarlo en mi blog, quería que se vea bien. Probé algunos coloreadores de código que <a href="http://www.google.com.ar/search?q=python2html&amp;start=0&amp;ie=utf-8&amp;oe=utf-8">encontré en la web</a>, pero no me convencieron. Quería algo mas simple.



Entonces escribí un pequeño script que haga lo que yo quería, lo escribí logeado en  la sesión ssh donde chequeaba mi correo electrónico.. y funciono! :-)



Le hice algunos arreglos antes de publicarlo, el más importante es la capacidad de aceptar muchos archivos como argumentos, entonces se puede usar por ejemplo así:

</p><pre lang="bash">

juanjo@platon:$ ./py2html.py *.py

Archivo comparacion.py procesado.

Archivo divisible.py procesado.

Archivo funcionesPF.py procesado.

Archivo maxRecurDeep.py procesado.

Archivo nullShell.py procesado.

Archivo py2html.py procesado.

Archivo tartaglia.py procesado.

Archivo whiteSpaces.py procesado.

</pre>



Dejó el código fuente disponible por si a alguien le interesa, creo que es un buen ejemplo para empezar: <a href="http://firebirds.com.ar/~juanjo/wordpress/files/python/py2html.py.html">py2html.py</a>



¡Sugerencias son bienvenidas!</body></html>