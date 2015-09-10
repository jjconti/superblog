.. title: import_twitpic (plugin para Nikola)
.. slug: import_twitpic-plugin-para-nikola
.. date: 2015-09-07 21:54:49 UTC-03:00
.. tags: Nikola, Python, Twitpic, import_twitpic
.. category:
.. link:
.. description:
.. type: text

Revisando qué contenido viejo subido a otros sitios podía importar en mi nuevo blog,
me di cuenta que en mi `segunda era </posts/2010/09/08/fotografiando-desde-el-camino-segunda-edicion/>`_
de **subir fotos tomadas con el celular mientras ando** [1]_
mis fotos, por pura casualidad, se estuvieron `guardando en Twitpic <http://twitpic.com/photos/jjconti>`_ 
(`descanse en paz <https://blog.twitpic.com/2014/10/twitpics-future/>`_).

Afortunadamente el sitio (que fue comprado por Twitter y dejado en modo read-only) te deja
exportar tus datos. Me bajé un zip que adentro tenía una carpeta. La carpeta tenía todas las
imágenes más un archivo de texto con la fecha de publicación de cada una y su texto.

Armado con esto y mi experiencia haciendo el plugin import_goodreads cree 
`import_twitpic <https://plugins.getnikola.com/#import_twitpic>`_.

Este es su README:

.. admonition:: README.md

    This plugin imports Twitpic pics (including twitted text) as new posts.

    This plugin:

    * Creates post as a rst file using the tweet text and the `figure` directive
    * Copies images to images/POSTS_OUTPUT_FOLDER/POST_SLUG/
    * Uses original tweet date as post date
    * Uses "Twitpic: DATE" as title
    * Adds "Twitpic" as tag plus the ones passed as arguments
    * Adds mentionds as hashtags as tags, but if the site already have a similar tag \
      it use that (to avoid "ERROR: Nikola: You have tags that are too similar")

    Note: Twitpic export is a folder cotaining all your images plus a tweets.txt file.

Tiene dos mejoras que eventualmente voy a migrar a import_goodreads y, con suerte, a otros:

* agrega el parámetro `--tags` para definir tags extras a agregar a los posts que se crearán
* antes de agregar un tag, se fija si antes no existe uno similar. De ser así, usa ese.

En la `etiqueta Twitpic <link://tag/twitpic>`_ se puede ver el resultado luego de ejecutar el comando:

.. code-block::

    nikola import_twitpic -o posts/twitpic/  -t "Desde el camino, Fotos" dumps/twitpic/

.. [1] La primera era fue con un `Nokia 6132 y mucho ingenio </posts/2008/08/18/fotografiando-desde-el-camino/>`_. 
