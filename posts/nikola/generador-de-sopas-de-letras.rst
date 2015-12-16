.. title: Generador de sopas de letras
.. slug: generador-de-sopas-de-letras
.. date: 2015-12-15 20:51:59 UTC-03:00
.. tags: Python
.. category: 
.. link: 
.. description: 
.. type: text

Desde hace un par de meses vengo usando un script en Python para generar sopas de letras.

Cuando busqué qué herramienta usar,
encontré `wordsearch.py <https://github.com/rboulton/wordsearch>`_ de Richard Boulton 
(entre otras opciones) qué básicamente hacía lo que quería: tomar una lista
de palabras y generar una sopa de letras lista para imprimir.

Desde entonces le hice algunas mejoras:

* Mejor disposición de la grila en el pdf generado
* Encabezado y pie configurables
* Permite palabras con espacios (usando comillas). Ejemplo:

Ejemplo del pdf generado: https://github.com/jjconti/sopa-de-letras/blob/master/output_example.pdf

.. code-block:: bash

    python wordsearch.py hard word1 "word with spaces" word3

* Permite caracteres no ascii en las palabras (por ejemplo ñ, á, é, í, ó, ú)

Mi versión se puede instalar desde: https://github.com/jjconti/sopa-de-letras/

PD para no programadores: si querés bajarlo y no sabés como hacerlo con el anterior link,
escribime y te ayudo!
