<html><body><p>En PHP uno pude ir mandando datos al cliente (navegador) a medida que los va procesando en el servidor. En Django siempre creé el texto de la respuesta para luego pasársela al objeto HttpResponse. A pesar de que había preguntado varias veces en el canal de chat de Django si podía hacer algo así y me habían respondido que <strong>no</strong>, tenía la intuición de que algo se podría hacer y pensé en iteradores.

</p><p>

Por suerte este fin de semana tuvimos <a title="Python en Santa Fe" href="http://www.pythonsantafe.com.ar/" target="_blank">un gran evento de Python</a> y alojé en mi casa a <a title="John Lenton" href="http://john.lenton.com.ar/" target="_blank">John</a>, quien me explicó en 5 minutos cómo hacerlo. Aquí una recreación de su ejemplo (<strong>views.py</strong>):

</p>

<pre>

<code>

from django.http import HttpResponse

from time import sleep



def gen():

    for x in range(80):

        sleep(1)

        yield '*' * x + '&lt;br/&gt;'



def test(request):

    return HttpResponse(gen(), mimetype='text/html')

</code>

</pre>

<p>

Queda para el lector ver la salida en su navegador.

<code>gen</code> es una función que al llamarla devuelve un generador. El primer parámetro de <a href="http://code.djangoproject.com/wiki/HttpResponse">HttpResponse </a>puede ser un generador o cualquier objeto con el método <code>__iter__</code>.

</p><p>

En la misma jornada Nubis, <a title="Hacking Django" href="http://woobiz.com.ar/es/articles/hacking-django" target="_blank">estuvo explorando</a> esto mismo desde distintos ángulos.</p></body></html>