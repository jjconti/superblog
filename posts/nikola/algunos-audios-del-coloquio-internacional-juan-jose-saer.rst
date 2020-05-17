.. title: Algunos audios del Coloquio internacional Juan José Saer
.. slug: algunos-audios-del-coloquio-internacional-juan-jose-saer
.. date: 2017-05-23 22:00:27 UTC-03:00
.. tags: Saer
.. category: 
.. link: 
.. description: 
.. type: text

Parto de la premisa de que soy un afortunado. ¿Poder estar un jueves a la mañana escuchando ponencias sobre un escritor? En suerte podría haberme tocado estar cosechando alguna oleaginosa en África.

La segunda idea importante es que disponemos de tecnología asombrosa al alcance de la mano.

¿Qué me cuesta, mientras estoy escuchando una charla, apretar un botón en mi celular y grabar el audio? Nada, solo haber recordado cargar la batería y no tener la memoria llena. Grabar en video es bastante más engorroso: require mucha más memoria, mucha más batería y sobre todo, mucho más pulso.

El restultado lo subo a Youtube porque es el sitio que estimo más perdurará en el futuro. Sin embargo, Youtube carece de una *feature* que sería muy útil para mi caso: poder subir solo audio o audio acompañado de una imagen. Por lo tanto, debo renderizar un video con el audio (y una imagen ilustrativa) antes de poder compartirlo. Hacerlo con un programa gráfico de edición de video, si bien sería sencillo, consume demasiado tiempo humano (mío), pero contando con un sistema operativo tipo Unix y algunos programas de línea de comando instalados podemos hacerlo en paralelo para todos los audios.

Este es el comando que utilicé para generar los siguientes videos:

.. code-block::

	ffmpeg -loop 1 -i imagen.jpg -i audio.mp3 -c:v libx264 -tune stillimage -c:a libvo_aacenc -b:a 192k -pix_fmt yuv420p -shortest video.mp4 


Miércoles
=========

.. media:: https://www.youtube.com/watch?v=bzUFXJjNWsw


.. media:: https://www.youtube.com/watch?v=I5Z4pZVm84Y


.. media:: https://www.youtube.com/watch?v=gQPb8k8Vh0E


Jueves
======

.. media:: https://www.youtube.com/watch?v=I-Sfl7I_ZAw


.. media:: https://www.youtube.com/watch?v=MOZnVRHIJVI


.. media:: https://www.youtube.com/watch?v=TJBMuLaO4k0


.. media:: https://www.youtube.com/watch?v=_dmnJthhF20


Viernes
=======

.. media:: https://www.youtube.com/watch?v=R0QCXDKPucA


.. media:: https://www.youtube.com/watch?v=Gw0jKbnUBbk


.. media:: https://www.youtube.com/watch?v=TbaZyqTwbCM


.. media:: https://www.youtube.com/watch?v=VSbHKOh3XlU


.. media:: https://www.youtube.com/watch?v=k-2137ezXbc


.. media:: https://www.youtube.com/watch?v=HKbe82gagAM


.. media:: https://www.youtube.com/watch?v=3vVmvGZ7MH4


PD1: no son todas, pero son varias. Son las que escuché.


PD2: la organización está editando la versión en HD de estas charlas. No se si de todas, pero tal vez sí. Mientras tanto, esto es mejor que nada. UPDATE: https://www.youtube.com/channel/UCqycy_4W2w_-q9aPDdhhLb
