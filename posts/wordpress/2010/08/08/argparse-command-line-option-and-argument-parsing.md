<html><body><p>Hoy recibí la <a href="http://blog.doughellmann.com/2010/08/pymotw-argparse-command-line-option-and.html" target="_blank">última edición</a> de <a href="http://www.doughellmann.com/PyMOTW/" target="_blank">Python Module of the Week</a>, un semanal de Doug Hellmann sobre módulos de Python. Leo:

</p><blockquote>The <code>argparse</code> module was added to Python 2.7 as a replacement

for <code>optparse</code>.</blockquote>

Nunca había usando <code>optparse</code> hasta hace un par de meses y estaba contento de haberlo empezado a usar, ordenaba mis programas de línea de comando con bonitos parámetros. ¿Tengo que aprender otro sistema totalmente nuevo? Veamos.<!--more-->



Esta es una parte de mi programa original:



<pre>from optparse import OptionParser

parser = OptionParser(usage="rpcping ip [-p port] [-r rep] [-s size]", version="rpcping 1.0")



parser.add_option("-p", type="int", dest="port", default=PORT)

parser.add_option("-r", type="int", dest="rep", default=REP)

parser.add_option("-s", type="int", dest="size", default=SIZE)

(options, args) = parser.parse_args()



if not args:

    parser.error("se necesita la direccion ip del servidor como argumento posicional.")

else:

    ip = args[0]



if not 1024 &lt; options.port &lt; 65535:

    parser.error("el puerto debe ser mayor a 1024 y menor a 65535.")

else:

    port = options.port



if not 0 &lt; options.rep &lt; 101:

    parser.error("las repeticiones deben ser mayores a 0 y menores a 101.")

else:

    rep = options.rep



if not 0 &lt; options.size &lt; 10001:

    parser.error("el tamaño deben ser mayores a 0 y menores a 10001.")

else:

    size = options.size

</pre>



Qué tuve que cambiar para que funcione con <code>argparse</code>:



<ul>

	<li>Cambiar nombres; <code>optparse</code> por <code>argparse</code>, <code>OptionParser</code> por <code>ArgumentParser</code>,<code> add_option</code> por <code>add_argument</code>.</li>

	<li>Cambiar el valor del agumento <code>type</code> de string a un tipo de verdad. En mi caso <code>type="int</code>" por <code>type=int</code>.</li>

	<li>Si tratamos de obtener el resultado del parsing así <code>(options, args) = parser.parse_args()</code>, vamos a tener un error <code>TypeError: 'Namespace' object is not iterable</code>. El nombre <code>result</code> en el nuevo código está asociado a un objeto del tipo <code>Namespace</code>.</li>

	<li><code>optparse</code> no trabaja con argumentos obligatorios, por lo que para el argumento ip había tenido que escribir código extra por mi cuenta. En <code>argparse</code> es más simple.</li>

</ul>

El resultado es:

<pre>from argparse import ArgumentParser

parser = ArgumentParser(description="Realiza ping via RPC contra un servidor", version="rpcping 1.0")



parser.add_argument("ip")

parser.add_argument("-p", type=int, dest="port", default=PORT)

parser.add_argument("-r", type=int, dest="rep", default=REP)

parser.add_argument("-s", type=int, dest="size", default=SIZE)

result = parser.parse_args()



ip = result.ip



if not 1024 &lt; result.port &lt; 65535:

    parser.error("el puerto debe ser mayor a 1024 y menor a 65535.")

else:

    port = result.port



if not 0 &lt; result.rep &lt; 101:

    result.error("las repeticiones deben ser mayores a 0 y menores a 101.")

else:

    rep = result.rep



if not 0 &lt; result.size &lt; 10001:

    parser.error("el tamaño deben ser mayores a 0 y menores a 10001.")

else:

    size = result.size

</pre>

Parece que con poco esfuerzo se puede migrar de <code>optparse</code> a <code>argparse</code> y luego empezar a estudiar las nuevas funcionalidades que incorpora.

<blockquote>The implementation of <code>argparse</code> supports features that would not have been easy to add to <code>optparse</code>, and that would have required backwards-incompatible API changes, so a new module was brought into the library instead. <code>optparse</code> is still supported, but is not likely to receive new features.</blockquote>

Más en: <a href="http://www.doughellmann.com/PyMOTW/argparse/" target="_blank">PyMOTW: argparse - Command line option and argument parsing</a>.</body></html>