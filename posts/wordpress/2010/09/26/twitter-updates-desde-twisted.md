<html><body><em>Este artículo es una re-edición del publicado el 24/08/2010 ya que cuando lo publiqué, Twitter estaba terminando su proceso apagar el sistema de autenticación básica para pasar al <a href="http://dev.twitter.com/pages/auth_overview" target="_blank">más complejo sistema de la danza oAuth;</a> lo cual convirtió al artículo en inservible. El artículo anterior no está más disponible. Gracias a <a href="http://www.pupeno.com" target="_blank">Pupeno</a> por revisar esta versión.

</em>



¿Tenés un servidor escrito en <a href="http://twistedmatrix.com" target="_blank">Twisted</a>? ¿Tenés eventos críticos o importantes que mandás por mail o a celulares? ¿Qué tal publicarlos en <a href="http://www.twitter.com" target="_blank">Twitter</a>?



La versión original de este artículo utilizaba la biblioteca <a href="http://github.com/dustin/twitty-twister" target="_blank">Twitty Twister</a>, la única pensada para usar Twitter desde Twisted. Lamentablemente no funciona bien con el nuevo sistema de autenticación de Twitter por lo que voy a usar <a href="http://github.com/joshthecoder/tweepy" target="_blank">Tweepy</a>, una librería con la cual hacer la danza de oAuth es muy sencillo.



1) <a href="https://twitter.com/signup" target="_blank">Registrar</a> un usuario dónde publicar las notificaciones.

2) Con ese usuario, <a href="http://dev.twitter.com/apps/new" target="_blank">registrar una aplicación</a>. Es muy importante usar el mismo usuario para ahorrarnos algunos pasos en la danza oAuth.

3) De la página de la aplicación creada, tomar la siguiente información: consumer key, consumer secret (desde la home de la aplicación), access token y access token secret (de la página My Access Token).

4) Código:



Con los datos del punto 3, creamos el módulo <strong>twitterupdates.py</strong>:

<pre>import tweepy



TWITTER_KEY = 'xxxxxxxxxxxxxxxx'

TWITTER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

MY_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxx'

MY_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'



auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)

auth.set_access_token(MY_KEY, MY_SECRET)

twitter = tweepy.API(auth)</pre>

y desde nuestra aplicación Twisted lo importamos:

<pre>from twitterupdates import twitter</pre>

Postear una actualización en Twitter o cualquier otra petición a un servidor externo tiene una naturaleza bloqueante y en un framework de concurrencia colaborativa, como es Twisted, no podemos darnos ese lujo. Para solucionar esto, utilizamos <a href="http://twistedmatrix.com/documents/10.1.0/api/twisted.internet.threads.deferToThread.html" target="_blank">deferToThread</a>:

<pre>deferToThread(twitter.update_status, "Mensaje a postear en Twitter")</pre>

Esta llamada retorna un objeto <a href="http://twistedmatrix.com/documents/current/core/howto/defer.html" target="_blank">Deferred</a> al cual se le pueden añadir callbacks o errbacks. La llamada bloqueante es corrida en un hilo aparte.



Enjoy!</body></html>