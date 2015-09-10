.. title: Nikola, intento... 3? 4?
.. slug: nikola-intento-3-4
.. date: 2015-08-31 23:39:07 UTC-03:00
.. tags: Nikola
.. category: 
.. link: 
.. description: 
.. type: text

Como cada año, vuelvo a intentar pasarme a `Nikola <https://getnikola.com>`_. Esta vez,
la patada inicial vino por otro lado.

Tengo un grupo de amigos, el LugCOS (originalmente Linux Users Group del Centro Oeste
Santafesino) que hace un par de años (desde que nos reencontramos gracias a Whatsapp)
vienen reclamándome que vuelva a poner en línea nuestro viejo sitio. Uno quería subir
artículos de electrónica, otro una guía sobre cómo armar una impresonar 3D con piezas
recicladas de la basura y el resto simplemente me pinchaba por deporte.

Una noche, mientras nos comunicábamos, cual grupo de radioaficionados modernos,
me volvieron a mojar la oreja. No aguanté más.

De cero a Nikola en diez minuotas
=================================

Entré al `Getting Started de Nikola <https://getnikola.com/getting-started.html>`_ 
y a lo caballo con anteojeras seguí las instrucciones. Funcionaron de una.
Tenía un blog andando en mi máquina. ¿Y ahora? Necesitaba que esté en Internet.

Algo que tenía en claro que no quería, y es por esto que retracé tanto levantar un sitio
para el grupo, era encargarme del hosting del mismo. Se me ocurrió, entonces, usar
Github Pages y tener en un sistema de control de versiones tanto el *código fuente* de
la página como su versión *compilada*.

Tunning
=======

El resto fue *tunnear* un poco el sitio:

* le robé el *theme* `Humitos <http://elblogdehumitos.com.ar/>`_
* importé algunos posts viejos de distintos blogs de los miembros
* apuntamos un dominio un nuevo dominio al sitio
* y escribí una `pequeña guía sobre cómo publicar posts para personas que nunca había usado ni Nikola ni git <https://github.com/lugcos/web/blob/master/README.md>`_

Una comunidad con barrera de entrada muy baja
=============================================

Mientras acomodaba un poco el *theme* a las necesidades de un blog multi-usuario pregunté
cómo se hacía en Nikola para linkear a los posts escritos por un author. Quería que cuando
se mostrara el nombre de un autor, por ejemplo bajo el título de cada post, este esté linkedo
a todos sus artículos. La respuesta fue que no se generaban páginas por autor, por lo que
no se podía. Se me ocurrió que podía hacer una contribución.

Ya había estado aportando cambios menores como pequeños fixes en la documentación, pero esto
era algo más grande. Hice un fork del repo y trabajé unas horas en privado. Cuando no supe
como seguir, ralsina me sugirió que haga un pull request agregándole WIP (Work in progress)
al título: https://github.com/getnikola/nikola/pull/1972.

En pocos días la feature estaba funcionando gracias a los comentarios de los desarrolladores
de Nikola, el fin de semana terminé los cambios que me sugirieron y hoy se mergió.

Continuará
==========

Puede ser que este sea el año en el que me pase a Nikola. Realmente quiero hacerlo desde hace
rato, quiero una forma simple (para una definición de simple dada por un programador) de
publicar mi contenido en la web, pero también quiero otras cosas. Me gustaría por ejemplo,
importar "posts" que escribí en distintas plataformas. Este es el plan:

* importar posts seleccionados de http://www.juanjoconti.com.ar (blog WordPress)
* Importar videos de youtube: https://www.youtube.com/feeds/videos.xml?user=juanjoconti
* Importar tweets: crear consola de importación para seleccionar qué tweets importar. Usar el type micro.
* Importar del posts blog: Lo que me llegó de China (http://loquemellegodechina.blogspot.com.ar/)
* Importar de Google docs?
* Importar de Facebook?
* Importar de alguna otra red social que haya usado?
* Importar de Goodreads

Algo que siempre me tira para atrás es que mi posts de WordPress no se ven muy bien en Nikola
apenas los importás. *I'll try to not overthink it too much*.


