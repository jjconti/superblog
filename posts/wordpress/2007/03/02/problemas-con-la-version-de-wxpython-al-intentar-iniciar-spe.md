<html><body><a href="http://pythonide.stani.be/">SPE</a> (Stani's Python Editor) es un Entorno de Desarrollo Integrado (IDE leyendo las siglas de atrás para adelante :-) ) libre (licenciado bajo GPL) para Python. Estaba con ganas de probarlo así que hoy lo instalé. En Debian:

<pre lang="bash">

apt-get install spe

</pre>

Cuando intenté ejecutarlo, hubo un problema:

<pre lang="bash">

juanjo@sarge:~$ spe

You need to install at least wxPython v2.5.4.1 to run SPE.

Get it from http://www.wxpython.org

</pre>

Pero mi versión instalada de wxPython era la 2.6.x.. en el resto del artículo: 2 formas de solucionar el problema.

<!--more-->

Además de saber que el paquete que tenía instalado era wxpython2.6 y no wxpython2.4 (que también era un candidato), comprobé la versión que tenía instalada desde el intérprete interactivo de Python:

<pre>

&gt;&gt;&gt; import wxPython

&gt;&gt;&gt; dir(wxPython)

['__builtins__', '__doc__', '__file__', '__name__', '__path__', '__version__', '_controls', '_core', '_gdi', '_misc', '_windows', '_wx', 'wx']

&gt;&gt;&gt; wxPython.__version__

'2.6.3.2'

</pre>

Entré al canal <code>#python</code> de <code>irc.freenode.org</code> donde alguien me dijo que en las versiones viejas de SPE había un bug con el chequeo de versiones y me me convenía instalar manualmente la última versión.

<pre lang="bash">

svn checkout svn://svn.berlios.de/python/spe/trunk/_spe

python _spe/SPE.py</pre> me daba el mismo error.

Cundo revisé el código de <code>_spe/SPE.py</code>, estas eran las primeas líneas:

<pre>

import sys

try:

    WX_VERSION  = '2.5.4.1'

    import wxversion

    wxversion.ensureMinimal(WX_VERSION)

except ImportError:

    print 'You need to install at least wxPython v%s to run SPE.\nGet it from http://www.wxpython.org'%WX_VERSION

    sys.exit()

</pre>

<h2>Solución 1</h2>

Probé importar <code>wxversion</code> desde un interprete de Python, no tenía el módulo y eso producía una excepción, lo que producía que se muestre ese error y se termine el programa. Comentando las líneas:

<pre>

    #import wxversion

    #wxversion.ensureMinimal(WX_VERSION)

</pre>

pude correr el programa sin problemas.

<h2>Solución 2</h2>

En realidad el problema es que el módulo <code>wxversion</code> no está instalado. En un momento había pasado por la página de <a href="http://www.wxpython.org/">wxPython</a> y entre sus nuevas <em>features</em> había leido:

<blockquote>

..wxPython now supports having more than one wxPython runtime installed at the same time, and provides a mechanism for choosing a non-default version at runtime if the app needs to.

</blockquote>

El módulo <code>wxversion</code> sirve para hacer la selección de versión de wxPython. Por lo que la otra solución es instalar este módulo:

<pre lang="bash">

apt-get install python-wxversion

</pre></body></html>