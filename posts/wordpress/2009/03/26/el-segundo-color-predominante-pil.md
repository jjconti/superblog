<html><body><p>Hace unas semanas necesité hacer un script en Python que genere algunas decenas de imágenes. Básicamente, se tiene como entrada imágenes como estas:



<a href="/wp-content/uploads/2009/03/die4side.png"><img class="aligncenter size-full wp-image-1354" title="die4side" src="/wp-content/uploads/2009/03/die4side.png" alt="" width="100" height="100"></a>



<a href="/wp-content/uploads/2009/03/die8side.png"><img class="aligncenter size-medium wp-image-1355" title="die8side" src="/wp-content/uploads/2009/03/die8side.png" alt="" width="100" height="100"></a>

(un borde con alguna forma y un color en un fondo blanco)



Las imágenes generadas tienen que tener ciertos números en el centro, pintados en cada caso del mismo color que el borde:



<a href="/wp-content/uploads/2009/03/d20_12.png"><img class="aligncenter size-full wp-image-1357" title="d20_12" src="/wp-content/uploads/2009/03/d20_12.png" alt="" width="100" height="100"></a>



<a href="/wp-content/uploads/2009/03/d8_1.png"><img class="aligncenter size-full wp-image-1356" title="d8_1" src="/wp-content/uploads/2009/03/d8_1.png" alt="" width="100" height="100"></a>



La primer parte del script tiene que determinar el segundo color predominante de la imagen (el primero es el blanco), esta es la forma en que lo hice usando <a title="Python Imaging Library (PIL)" href="http://www.pythonware.com/products/pil/" target="_blank">PIL</a>:

</p><pre>def get_color(image):

    colors = image.getcolors()  # colors is a list of (count, color)

    colors.sort(lambda y,x: cmp(x[0], y[0])) # bigger count first

    c = colors.pop(0)

    while white(c): # find the non-white color most used in the image

        c = colors.pop(0)

    return c[1]



def white(color):

    color = color[1]

    return color[0] == 255 and color[1] == 255 and color[2] == 255</pre></body></html>