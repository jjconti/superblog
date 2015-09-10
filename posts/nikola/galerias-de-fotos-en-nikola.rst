.. title: Galerías de fotos en Nikola
.. slug: galerias-de-fotos-en-nikola
.. date: 2015-09-08 12:19:42 UTC-03:00
.. tags: Nikola
.. category:
.. link:
.. description:
.. type: text

Hubo una época, pre-Facebook, en la que los informáticos instalábamos programas 
de galerías de imágenes escritos en PHP en nuestros propios servidores y subíamos
allí las fotos sacadas con nuestras nuevas cámaras digitales de 4 megapixeles.

El problema con estos programas (había realmente muchos para elegir) es que requiren
que uno (el *administrador de sistemas*) los actualice (entre otros mantenimientos 
requeridos). Esto es divertido al principio, una molestia después y al final es
algo que dejamos de hacer.

Si visitamos alguno de esos sitios hoy, alrededor de las imágenes se pueden ver errores
como:

.. error::

    Deprecated: Function ereg() is deprecated in /home/jjconti/galeria.juanjoconti.com.ar/zp-core/functions-i18n.php on line 190

    Warning: Cannot modify header information - headers already sent by (output started at /home/jjconti/galeria.juanjoconti.com.ar/zp-core/functions-i18n.php:190) in /home/jjconti/galeria.juanjoconti.com.ar/zp-core/functions.php on line 1897

    Warning: session_start() [function.session-start]: Cannot send session cookie - headers already sent by (output started at /home/jjconti/galeria.juanjoconti.com.ar/zp-core/functions-i18n.php:190) in /home/jjconti/galeria.juanjoconti.com.ar/zp-core/admin-functions.php on line 6

En estos días, que ando buscando qué me dejé olvidado en Internet para importarlo aquí, 
encontré uno de estos sitios que instalé en su momento.
    
Como el programa organizaba los álbums en carpetas y sub carpetas, con el siguiente comando


.. code-block::

    tar cvfz albumns.tgz  --exclude="*.php" albums/
    
pude crear un archivo listo para crear una galería en Nikola.

Crear una galería de fotos en Nikola es extremadamente fácil. Solo hay que agregar carpetas
con fotos a la carpeta `galleries` o a la que se haya definido en `conf.py` y ejecutar:

.. code-block::

	nikola build

`Fotos </fotos/>`_.