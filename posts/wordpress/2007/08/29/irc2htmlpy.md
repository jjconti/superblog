<html><body><p>Ayer colgué del blog el <a href="http://www.juanjoconti.com.ar/2007/08/28/log-de-tutorial-sobre-empaquetado-para-debianubuntu/" title="Paquetes para Debian">log de un tutorial</a> dictado a través del <a href="http://es.wikipedia.org/wiki/IRC" title="IRC" target="_blank">IRC</a>. Cuando <a href="http://www.google.com.ar/search?hl=es&amp;client=firefox-a&amp;rls=com.ubuntu%3Aen-US%3Aofficial&amp;hs=KTs&amp;q=irc2html&amp;btnG=Buscar&amp;meta=" title="Goooooooogling" target="_blank">busqué en Google</a> un <em>formateador de logs de irc</em> no encontré lo que buscaba. El principal <em>feature</em> que me interesaba era que se distinga a los diferentes usuarios con diferentes colores. Probablemente podría haber buscado con un poco más de empeño y habría encontrado lo que buscada, al fin de cuentas ya había usado un programa así hace unos años, pero me hubiera perdido de una hora entretenida programando y aprendiendo <a href="http://www.python.org" title="Python" target="_blank">Python</a>.



<!--more-->

</p><h2>Script irc2html.py</h2>

Primero lo primero. Tal vez llegaste a este blog buscando lo mismo que yo pero más adelante en el tiempo. <em>Good news</em>: <a href="http://www.juanjoconti.com.ar/files/python/irc2html.py.html" title="Source Code">irc2html.py</a>. <strong>UPDATE:</strong> <a href="http://www.juanjoconti.com.ar/files/python/irc2html-f.py.html" title="Source Code">irc2html-f.py</a> es una versión mejorada tras recibir un comentario en este post.



Uso:

<code>

./irc2html.py charla.log

</code>

escribe en la salida estándar código html listo para embeber. También podés hacer:

<code>

./irc2html.py charla.log &gt; charla.html

</code>

(prometo que tu <em>browser</em> no se va a quejar)

<h2>Un color para cada uno</h2>

Como decía más arriba, lo que más me interesaba era que se distinga, mediante colores, lo que los distintos usuarios dicen. Esto se hace más difícil a medida que aumenta el número de usuarios. La dificultad radica en encontrar colores lo suficientemente diferentes como para distinguir a los usuarios. Lo primero en lo que pensé fue en hacer una función que reciba un color inicial y que luego vaya saltando por la paleta de colores a medida que iba necesitando más colores.

<p align="center"><img src="/wp-content/uploads/2007/08/paletacolores.png" alt="Paleta de Colores"></p>

<p align="left">Hice algunas pruebas pero no prosperaron. Por suerte esto me sirvió como escusa para practicar <a href="http://docs.python.org/ref/yield.html" title="yield statement" target="_blank">yield</a> y <a href="http://www.python.org/dev/peps/pep-0255/" title="generators" target="_blank">generadores</a> y Python. Terminé con una implementación mucho menos ambiciosa que la original:</p>



<pre lang="python">

# Generador de colores:

#

# Para ayudar a distingir lo que dice un usuario de lo que dice otro,

# se utilizan distintos colores para cada uno.

#

# La idea original del generador de colores era que vaya saltando por

# la paleta de colores según un patrón matemático.

# La actual implementación es más simple y etática.



color_list = ['ff0000', 'fff200', '00ff00', '00fff2', '0000ff', 'aa18ff',

              'ff00fb', 'fbb636', 'b1466b', '3d3166',  'bfbf2e', '377972']



# Lighter colors:

#color_list = ['fff1df', 'feffdf', 'e3ffce', 'ffe4df', 'fcdfff', 'e7dfff',

#              'e7f1ff', 'e7fff9', 'f3ffe7', 'e9e9e9', 'ffedb9', 'f0e9d5']



def color_gen(l):

    colors = l[:]

    colors.reverse()

    while True:

        if colors:

            yield colors.pop()

        else:

            colors = l[:]</pre>

<h2>Expresiones regulares</h2>

En el script hago uso de <a href="http://docs.python.org/lib/module-re.html" title="Python regex " target="_blank">expresiones regulares</a> para <em>parsear</em>  las líneas del archivo de log. El archivo sobre el que trabajé tenía dos tipos de líneas. Con mensajes de usuarios, como:



'&lt;pablo_!~pablo@r190-64-130-143.dialup.adsl.anteldata.net.uy&gt; [17:00] comprendido marga :)\n'



o de información como:



'-charm.oftc.net- [17:00] garaguas (~garaguas@host193.200-82-125.telecom.net.ar) joined the channel\n'



Me interesan la primeras, a las segundas las puedo ignorar. La expresión regular que usé fue:



'\&lt;(?P&lt;nombre&gt;.+)!.*\&gt;(?P&lt;dicho&gt;.+)$'



y se lee:



1) el carácter '&lt;'.

2) de 1 a n caracteres de cualquier tipo (excepto '\n') y a las cadenas que <em>matchen</em> en esta parte de la expresión voy a referenciarlas luego como 'nombre'.

3) el carácter '!'.

4) de 0 a n  caracteres de cualquier tipo (excepto '\n').

5) el carácter '&gt;'

6) de 1 a n caracteres de cualquier tipo (excepto '\n') y a las cadenas que <em>matchen</em> en esta parte de la expresión voy a referenciarlas luego como 'dicho'.

7) final de línea ($).



Un ejemplo en el REPL de Python:

<pre>&gt;&gt;&gt; import re

&gt;&gt;&gt; a = '&lt;pablo_!~pablo@r190-64-130-143....&gt; [17:00] comprendido marga :)n'

&gt;&gt;&gt; b = '-charm.oftc.net- [17:00] garaguas (~garaguas@host...) joined the channeln'

&gt;&gt;&gt; rex = &lt;(?P&lt;nombre&gt;.+)!.*&gt;(?P&lt;dicho&gt;.+)$'

&gt;&gt;&gt; pat = re.compile(rex)

&gt;&gt;&gt; m = pat.match(b)

&gt;&gt;&gt; m

&gt;&gt;&gt; m == None

True

&gt;&gt;&gt; m = pat.match(a)

&gt;&gt;&gt; m

&lt;_sre.SRE_Match object at 0x8707698&gt;

&gt;&gt;&gt; m.group('nombre')

'pablo_'

&gt;&gt;&gt; m.group('dicho')

' [17:00] comprendido marga :)'</pre>

<h2>Resultado final</h2>

Comentando y descomentando las líneas:

<pre>#line_format = "&lt;span style='color:#%s'&gt;%s:&lt;/span&gt;%s&lt;br/&gt;"

line_format = "&lt;div style='background-color:#%s'&gt;&lt;b&gt;%s:&lt;/b&gt; %s&lt;/div&gt;"</pre>

se pueden obtener dos resultados distintos:

<h3>Formato 1:</h3>

<p align="center"><img src="/wp-content/uploads/2007/08/chat1.png" alt="Chat1"></p>



<h3>Formato 2:</h3>

<p align="center"> <img src="/wp-content/uploads/2007/08/chat21.png" alt="Chat2"></p>



<h2>Notas finales</h2>

<ul>

	<li>Espero este <em>script</em> les haya sido útil, ya sea para formatear logs de irc como para seguir aprendiendo Python (yo en particular casi no había usado <em>yield</em> y con <em>re</em> solo había hecho pruebas).</li>

	<li>La primer imagen del post es una composición de una captura de pantalla y esta <a href="http://www.iconfinder.net/index.php?q=color&amp;iconid=9953&amp;size=128&amp;q=color&amp;s12=on&amp;s16=on&amp;s22=on&amp;s32=on&amp;s48=on&amp;s64=on&amp;s128=on" title="colorpicker" target="_blank">linda imagen lgpl de un gotero</a>.</li>

</ul></body></html>