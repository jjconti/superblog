<html><body><p>Desde el etorno gráfico de tu GNU/Linux abrí una terminal (gnome-terminal, Konsole, Eterm u otra). Con tu editor preferido (vi, emacs, gedit u otro) creá el archivo <code>love</code> con este contenido:

</p><pre>plot a*(1-sin(t))

a = a - 2

pause 1

if(a == 0) a = 16

reread

</pre>

Desde la terminal ejecutá el comando <code>gnuplot</code> y allí:

<pre>gnuplot&gt; set polar

        dummy variable is t for curves

gnuplot&gt; set xrange[-25:25]; set yrange[-35:5]

gnuplot&gt; a = 16

gnuplot&gt; set title "All you need is love"

gnuplot&gt; load 'love'

</pre>

Done! All you need is love!.. and gnuplot! :)

<!--more-->

<a href="http://www.gnuplot.info">Gnuplot</a> es un potente <a href="http://www.gnu.org/philosophy/free-sw.es.html">Software Libre</a> que permite graficar funciones matemáticas tanto en 2 como en 3 dimenciones.



a*(1-sin(t)) es una función matemática en coordenadas polares que se denomina cardioide por su forma de corazón.



Este pequeño ejemplo ilustra como utilizar esta herramienta para crear animaciones en base a la parametrización de funciones matemáticas que nos permitan observar comportamientos según cambian los valores de los parámetros.</body></html>