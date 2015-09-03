<html><body><p>Hoy <a href="http://twitter.com/pedroprez/status/34967078767169536" target="_blank">Pedro preguntó en Twitter</a> "Que lenguajes de programación permiten a día de hoy soporte full unicode para codear?". Algunos contestaron que Java o C#. No los conozco, <span style="text-decoration: line-through;">pero creo que no</span>. Creo que respondieron que el lenguaje puede trabajar con strings unicode, lo cual es bastante común hoy en día. Mi respuesta fue: Python 3. Con Python 3 podemos tener caracteres unicode en el código fuente, en el nombre de las variables por ejemplo:

</p><pre>&gt;&gt;&gt; á = 1

&gt;&gt;&gt; print(á)

1

&gt;&gt;&gt; 大家好 = range(10)

&gt;&gt;&gt; for ä in 大家好:

...     print(ä)

...

0

1

2

3

4

5

6

7

8

9

&gt;&gt;&gt; año = 2027

&gt;&gt;&gt; año += 1

&gt;&gt;&gt; print(año)

2028

</pre></body></html>