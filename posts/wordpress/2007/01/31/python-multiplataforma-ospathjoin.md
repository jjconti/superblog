<html><body><p>Por lo general cuando se habla de <strong>multiplataforma</strong> se hace sólo referencia al hecho de que cierto <em>código</em> pueda <em>ser ejecutado</em> en diferentes plataformas (léase en la mayoría de los casos hardware + SO) sin tener que ser <em>portado</em>, es decir que se realicen cambios importantes en este. 



En el caso de los programas escritos en un lenguaje compilado es necesario <em>construir</em> un archivo ejecutable (un archivo que contiene código binario) específico para cada plataforma en la que se lo quiera correr. Esto no sucede con los lenguajes interpretados, dónde la cuestión es más simple. Un programa escrito en un lenguaje interpretado será multiplataforma si el intérprete del lenguaje en el que está escrito lo es (siempre y cuando no se haga uso de alguna característica específica de alguna plataforma). Al fin de cuentas, el <em>archivo ejecutable</em> de un programa interpretado no será más que un archivo de texto plano.



Pero puede haber algo más...

<!--more-->

Hace poco, usando Python, descubrí algo que me hizo pensar un poco más sobre las características que debe brindar un lenguaje de programación para que lo consideremos multiplataforma. Piensen lo siguiente: archivos. Un programa suele hacer un uso intenso de archivos (de configuración, imágenes, para guardar datos y luego recuperarlos, etc..). Lo que nos lleva a pesar: ¿cómo encuentra un programa esos archivos? Probablemente el lenguaje de programación que estemos utilizando nos proveerá de una función para abrir archivos[1] que recibiera como parámetros el nombre del archivo y la forma (modo) en que queremos abrirlo (para lectura, para escritura, crearlo si no existe, en modo binario, etc..). Dejemos de lado el modo y pensemos en lo que significa el nombre del archivo, ¿sería <code>config.php</code> un nombre válido? ¿Lo sería <code>files/config.php</code>? ¿Y que tal <code>/var/www/prog/files/config.php</code>? Me animo a darles una alternativa más en la que pensar: <code>C:\wamp\www\prog\files\config.php</code>.



Con esto quiero expresar que el parámetro <em>nombre</em> puede ser tanto un nombre absoluto para el archivo como uno relativo. <code>config.php</code> y <code>files/config.php</code> son ejemplos de nombre relativo mientras que <code>/var/www/prog/files/config.php</code> y <code>C:\wamp\www\prog\files\config.php</code> lo son de nombres absolutos. En mi opinión lo más cómodo es utilizar nombres relativos al directorio dónde se encuentra el archivo ejecutable, pero tenerlos todos juntos en el primer nivel de este sería engorroso y poco elegante.



Uno puede pensar en tener una organización de directorios que le permita trabajar cómodo a la vez que les permite a otros encontrar fácilmente lo que esta buscando. Por ejemplo:



<code>data/</code> : para guardar los datos usados por el programa.

<code>data/imgs/</code> : para las imágenes

<code>data/sounds/</code> : para los sonidos

<code>config/</code> : para los archivos de configuración

etc..



Y aquí es justamente dónde surge el problema cuya solución quería comentar.



Habrán notado en los ejemplos de más arriba hay una sutil diferencia. En los primeros se separa los nombres de los directorios con la barra "/" y en otros con "\". El primero es el separador de directorios utilizado en GNU/Linux (y en UNIX en general), mientras que el segundo es el utilizado en MS Windows. Y este es solo un ejemplo, pero pueden existir muchas diferencias (en este punto) de plataforma en plataforma, algunas que incluso no conozcamos u otras que ni siquiera han surgido aún!!



Usando la función os.path.join, un <em>pathname</em> que funcione correctamente en la plataforma dónde el programa sea ejecutado será creado[2].



La forma de usarla que he siembre visto es importando el módulo os:



</p><pre>import os

os.path.join("data", "sounds", "wrong.wav")</pre>



Yo conocí esta función leyendo un <a href="http://www.pygame.org/docs/tut/chimp/ChimpLineByLine.html">tutorial de PyGame</a>. ¿Conocen algo parecido en otro lenguaje?



[1] Cuando hablo de abrir un archivo lo hago para ejemplificar la necesidad de encontrar un archivo, lo siguiente es igualmente válido para una función que por ejemplo reciba como parámetro el nombre de archivo de una imagen y la cargue en memoria para que luego podamos disponer de esta.

[2] Las versiones modernas de MS Windows se las arreglan para manejar pathnames que utilizan la barra "/" en lugar de la barra "\", pero esto es solo una parte de las plataformas dónde potencialmente ejecutaremos nuestro programa.</body></html>