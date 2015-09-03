.. title: import_goodreads plugin for Nikola
.. slug: import_goodreads-plugin-for-nikola
.. date: 2015-09-02 15:43:15 UTC-03:00
.. tags: Nikola, Goodreads 
.. category: 
.. link: 
.. description: 
.. type: text

Ayer creé un nuevo plugin para Nikola como parte de mi esfuerzo por centralizar en este
nuevo blog estático, distintos contenidos creados a lo largo de los años en distintas
plataformas web.

Hoy, luego de algunos ajustes, lo mergiamos.

https://plugins.getnikola.com/#import_goodreads

Este es el README:

.. admonition:: README.md

    This plugin import Goodreads read books from Goodreads RSS to an existing site.

    It:

    * uses the date the user ends to read the book as post date
    * includes user review
    * includes user rating
    * includes a link to the original review
    * uses author name, book title and "Goodreads review" as tags
    * writes output by default in posts/

    To Do:

    * include book cover (dowloading the image)
    * add parameters to customize tags and content generated

Estaría bueno que no tenga código repetido con otros plugins: sí.

Estaría bueno que tenga más parámetros: sí.

¡Pero para ser la versión 0.1 está bastante bien!

El resultado en este blog se puede ver en el tag `Goodreads review <link://tag/goodreads-review>`_.