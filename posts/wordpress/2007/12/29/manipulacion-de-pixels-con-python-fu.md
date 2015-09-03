<html><body><p>Usando <a title="The GNU Image Manipulation Program" href="http://www.gimp.org" target="_blank">GIMP</a> y el complemento que permite crear <a title="Python-Fu doc" href="http://www.gimp.org/docs/python/index.html" target="_blank">plug-ins en Python</a> podemos hacer manipulación a bajo nivel de los pixels de una imagen.

</p><h2>PixelRegion</h2>

PixelRegion permite realizar una abstracción sobre una imagen de forma tal de verla como una región de pixeles. Cada posición x,y de la región corresponde a un pixel de la imagen. En el caso de las imágenes <a title="Red, Green, Blue" href="http://es.wikipedia.org/wiki/Modelo_de_color_RGB" target="_blank">RGB</a>, cada pixel tiene 3 valores. En Python-Fu estos valores son representados con un string de 3 caracteres en el que cada caracter es uno de aquellos que tiene su número de orden (función <code>ord</code>) entre  y 255.



Los siguientes ejemplos son una demostración sencilla de como trabajar con PixelPerfect para manipular imágenes. En el primer ejemplo  se leen los valores de algunos de los pixeles de la imagen y en el segundo se escriben otros.<!--more-->

<h3>Ejemplo 1 (lectura)</h3>

La siguiente imagen de 5x5 pixeles (ampliada) será usada para este ejemplo:

<p align="center"><img src="/wp-content/uploads/2007/12/5-big.jpg" alt="5×5 pixel image"></p>

<p align="center"><em>Imagen original</em></p>



La función <code>pixel</code> es la que se ejecutará cuando ejecutemos el plug-in creado para este ejemplo. No se ingresan parámetros desde la interfaz gráfica del mismo, pero la función recibe 2 argumentos. Objetos que representan la imagen y la capa (layer) a procesar.

<pre>def pixels(img, layer):



    w = layer.width

    h = layer.height



    pr = layer.get_pixel_rgn(0, 0, w, h)



    print "Valores de los pixeles de las esquinas de la imagen"



    r,g,b = pr[0,0]

    print [ord(x) for x in r,g,b]



    r,g,b = pr[0,4]

    print [ord(x) for x in r,g,b]



    r,g,b = pr[4,0]

    print [ord(x) for x in r,g,b]



    r,g,b = pr[4,4]

    print [ord(x) for x in r,g,b]



    layer.update(0, 0, w, h)

    layer.flush()

    gimp.displays_flush()</pre>

El ejemplo es sencillo y lo que hace es instanciar una PixelRegion tan grande como la capa (layer). Luego los diferentes pixeles de la misma pueden accederse mediante sus coordenadas: <code>pr[x,y]</code>.



Se muestran los valores RGB de cada uno de los puntos del ejemplo.



Código fuente: <a title="read" href="http://www.juanjoconti.com.ar/files/python/fu/pixels/pixels-read.py.html" target="_blank">pixels-read.py</a>

<h3>Ejemplo 2 (escritura)</h3>

En una porción de código que empieza de forma similar a la del ejemplo anterior podemos ver que una vez que hemos obtenido la PixelRegion que nos interesa, podemos escribir pixeles en ella.



El siguiente ejemplo aplicado sobre la imagen del ejemplo anterior dibuja una equis amarilla:

<pre>def pixels_write(img, layer):



    w = layer.width

    h = layer.height

    pr = layer.get_pixel_rgn(0, 0, w, h)



    yellow_rgb = (255,255,0)

    yellow_str = chr(yellow_rgb[0]) + chr(yellow_rgb[1]) + chr(yellow_rgb[2])



    for i in xrange(5):

        pr[i,i] = yellow_str

        pr[4-i,i] = yellow_str



    layer.update(0, 0, w, h)

    layer.flush()

    gimp.displays_flush()</pre>

<p align="center"><img src="/wp-content/uploads/2007/12/5-big-yellow.jpg" alt="5×5 image with yellow pixels"></p>

<p align="center"><em>Imagen procesada con el código del ejemplo 2</em></p>

<p align="left">Código fuente: <a title="write" href="http://www.juanjoconti.com.ar/files/python/fu/pixels/pixels-write.py.html" target="_blank">pixels-write.py</a></p>



<h2>Links</h2>

<ul>

	<li><a title="Mis artículos sobre plug-ins para GIMP en Python" href="http://www.juanjoconti.com.ar/categoria/aprendiendo-python/python-fu/" target="_blank">Más artículos</a> relacionados con Python-Fu.</li>

	<li>Experimentos con PixelRegion.</li>

	<li><a title="API" href="http://developer.gimp.org/api/2.0/app/app-pixel-region.html" target="_blank">API en C</a> de PixelRegion.</li>

</ul></body></html>