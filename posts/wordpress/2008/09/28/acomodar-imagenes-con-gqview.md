<html><body><p>Algunas cámaras de fotos tienen un dispositivo que detecta su posición, entonces si sacamos una foto con la cámara posicionada verticalmente, la imagen resultante es más alta que ancha. Lo mismo sucede en el caso contrario, si se saca una foto con la cámara en forma horizontal, la imagen resultante será más ancha que alta.

Esto parece bastante bueno. Lamentablemente muchos dispositivos (cómo los celulares) no vienen equipados con este dispositivo y todas las fotos terminan siendo, por ejemplo, más altas que anchas. Otra cosa a tener en cuenta es que la mencionada funcionalidad no funciona del todo bien en todas las cámaras. Si bien en el siguiente caso es algo apropiado:



<a href="/wp-content/uploads/2008/09/imagen599.jpg"><img src="/wp-content/uploads/2008/09/imagen599-225x300.jpg" alt="" title="imagen599" width="225" height="300" class="aligncenter size-medium wp-image-576"></a>

En este no lo es:

<a href="/wp-content/uploads/2008/09/imagen558.jpg"><img src="/wp-content/uploads/2008/09/imagen558-225x300.jpg" alt="" title="imagen558" width="225" height="300" class="aligncenter size-medium wp-image-574"></a> Y nos interesa convertirla en:

<a href="/wp-content/uploads/2008/09/imagen5581.jpg"><img src="/wp-content/uploads/2008/09/imagen5581-300x225.jpg" alt="" title="imagen5581" width="300" height="225" class="aligncenter size-medium wp-image-575"></a>

El problema crece cuando sacamos muchas fotos[0]. Ya sea para compartirlas en Internet o para guardarlas en nuestra computadora queremos que estén posicionadas correctamente. En GNU/Linux es fácil rotar una imagen, el comando convert de ImageMagic, por ejemplo, lo hace en un instante. Si tenemos muchas imágenes a retocar, podemos hacer un script que recorra una lista de archivos y sobre todos realice el proceso. Pero en la mayoría de los casos no será tan simple. Querremos modificar algunas imágenes, pero querremos que otras se mantengan en su posición original.<!--more--> Lo ideal es utilizar un visualizador de imágenes y cada vez que encontramos una cuya posición queremos rotar, indicarle esto a visualizador para que la imagen sea rotada definitivamente.

<a href="http://gqview.sourceforge.net/">GQview</a> viene preparado para hacer esto, utilizando el comando <code>jpegtrans</code>. No tenía instalado este programa en mi computadora, pero pude editar la configuración del software para que ejecute mis comandos personalizados.

<a href="/wp-content/uploads/2008/09/gqview.png"><img src="/wp-content/uploads/2008/09/gqview-300x177.png" alt="" title="gqview" width="300" height="177" class="aligncenter size-medium wp-image-586"></a>

En Editar/Preferencias... solapa Editores podemos especificar una secuencia de comandos para ser ejecutados al elegir una opción del menú:

<a href="/wp-content/uploads/2008/09/gqview_preferencias.png"><img src="/wp-content/uploads/2008/09/gqview_preferencias-300x267.png" alt="" title="gqview_preferencias" width="300" height="267" class="aligncenter size-medium wp-image-587"></a>

Completé las filas 7 y 8 con los siguientes valores:



Rotar imagen (sentido horario) - <strong>convert -rotate 270 %p %p</strong>

Rotar imagen (antihorario) - c<strong>onvert -rotate 90 %p %p</strong>

Ahora cuando estoy visualizando imágenes y encuentro alguna mal orientada, simplemente tengo que apretar Ctrl-7 u Ctrl-8 para ajustarla.

<a href="/wp-content/uploads/2008/09/gqview2.png"><img src="/wp-content/uploads/2008/09/gqview2-300x177.png" alt="" title="gqview2" width="300" height="177" class="aligncenter size-medium wp-image-588"></a>

[0] en mi caso unas 1000, en mi viaje a Brasil.</p></body></html>