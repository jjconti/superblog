<html><body><p>Para cierta cuenta de Twitter que administro, necesitaba dejar de seguir a todos los usuarios que no me seguían.



Busqué si había alguna web que diera el servicio y las que encontré (NotFollow y JustUnfollow) solo se limitaban a listar a quienes no te seguían y permitirte ir eliminándolos de a uno. Un chiste. (JustUnfollow te deja eliminar solo 50 usuarios por día si no te pasás a la cuenta premium, paga, o twitteas haciéndoles propaganda).



Tenía que eliminar a casi 2000 usuarios y no tenía ganas de que me diera tendinitis en el dedo índice derecho de tanto hacer click.



Como siempre, <strong>dada la herramienta correcta, un trabajo a primera vista tedioso o complicado puede resultar extremadamente fácil</strong>. Utilizando la librería <a title="PTT" href="https://pypi.python.org/pypi/twitter" target="_blank">Python Twitter Tools</a> hice este <em>script</em> que, luego de la <a href="https://dev.twitter.com/docs/auth" target="_blank">danza de OAuth</a> para autenticarse en Twitter, consta de 7 líneas. Tomen <em>community managers</em>, se los regalo:

</p><pre>following = twitter.friends.ids()

followingIds = following['ids']

followers = twitter.followers.ids()

followersIds = followers['ids']



for id in followingIds:

    if id not in followersIds:

        twitter.friendships.destroy(user_id=id)</pre>

PS: para los amantes del <a href="http://en.wikipedia.org/wiki/Code_golf" target="_blank">code golfing</a>, ahí va la versión en una línea:

<pre>[twitter.friendships.destroy(user_id=id) for id in twitter.friends.ids()['ids'] if id not in twitter.followers.ids()['ids']]</pre>

Nota: para dejar de seguir unos 1900 usuarios tardo una media hora en mi notebook.



Tarea para el lector: escribir un <em>script</em> para seguir a todos los seguidores que no estamos siguiendo.</body></html>