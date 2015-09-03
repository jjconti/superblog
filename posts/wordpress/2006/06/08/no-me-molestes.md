<html><body><p>Ayer empecé a ser atacado por un <a href="http://es.wikipedia.org/wiki/Spam">smmaper</a> que despiadadamente cada minuto publicaba un comentario en uno de mis artículos en este blog, siempre desde diferentes IPs (seguro esto no era real, pero así lo veía mi WordPress), siempre con diferents e-mals y siempre con diferente contenido.



Cómo no podía evitar que sus comentarios se publiquen y como no quería que estos molesten a alguno de mis visitantes, configuré WordPress para que todos los comentarios no enviados por usuarios que tengan comentarios previamente autorizados sean marcados como <em>pendientes de moderación</em>. Ayer en un rato se juntaron 69 mensajes!! Necesitaba una solución definitiva.

<!--more-->

Hoy <a href="http://www.mozilla.com/thunderbird/">Thunderbird</a> (mi cliente de correo) me avisó que <a href="http://lucas.lunix.com.ar/wordpress">Lucas</a> tenía un nuevo artículo en su blog, se titulaba: <strong>SPAM: esa gran molestia…</strong>. No lo podía creer, le estaba pasando lo mismo que a mí. En una parte decía:

</p><blockquote>

a alguien le pareció muy cheto spammear sitios pedorros como este!

</blockquote>



Qué identificado me sentí!! Así que como decía en su artículo, también instalé <a href="http://dev.wp-plugins.org/browser/wp-morph/trunk/">wp-morph</a>, un plug-in para WordPress hecho por <a href="http://neuromancer.inf.um.es/blog/">Diego Sevilla</a>, y hasta ahora (llava una hora en funcionamiento) no he tenido problemas. Gracias Diego! y gracias Lucas!



Les dejo aca el LEEME del programa para que vayan viendo de que se trata y los instalen en su WordPRess para eviatr estos problemas:





<blockquote>

LEEME de WP-Morph

-----------------



WP-Morph es un plugin anti-spam para WordPress.  Características:



* No requiere de ningún "capcha". El usuario no tiene que introducir 

  ningún código extraño ni se entera de nada del proceso.

* Se requiere JavaScript en el browser.

* Los Spammers tendrían que interpretar el código JavaScript de la 

  página para poder enviar comentarios. Hasta ahroa no conozco a 

  ningún programa spammer que haya sido capaz de interpretar también 

  el código JavaScript de la página.



Instalación

-----------



* Descarga el plugin de aquí: http://dev.wp-plugins.org/browser/wp-morph/trunk/

* Copia wp-morph.php en el directorio de plugins de WordPress 

  (normalmente WP-ROOT/wp-content/plugins/ ).

* Ve al menú "Plugins" de la administración de WordPress.

* Activa el plugin "WP-Morph".



¡¡Y ya está!! ¡¡Adios spam!!



Change Log

----------



v1.5:

* Sólo actúa sobre comentarios. No sobre trackbacks ni pingbacks.



v1.4:

* Adaptado a la versión 2 de WordPress con cambios mínimos.



v1.3:

* Documento válido en XHTML (Gracias a Will http://www.willsdownloads.com/blog/

  por sugerir esto).



v1.2:

* Un mensaje de error más explicativo.

* $rnd_val se calcula automaticamente y se almacena como una opción de WP.

  Así no se necesita interacción ni configuración por parte del usuario.

  (Gracias a Denis de Bernardy <denis.at.semiologic.com> por sugerir esto).

* Pequeños cambios en la generación del JavaScript para evitar overflows.



v1.1:

* Generación de valores mejorada. Ahora los formulario expiran después

  de un número de minutos configurado por parte del usuario del plugin.

* Muestra que el formulario está protegido por WP-Morph.



v1.0:

* Versión inicial.





Info

----



Para más información, por favor, ve a:



http://neuromancer.dif.um.es/blog/index.php?s=wp-morph&amp;submit=Search



¡Disfruta!

diego.



(¿Comentarios? ¿Preguntas?: dsevilla@um.es ).

</denis.at.semiologic.com></blockquote>







</body></html>