.. title: Importar tweets al blog
.. slug: importar-tweets-al-blog
.. date: 2015-09-03 22:00:16 UTC-03:00
.. tags: The Martian, Nikola, Twitter
.. category:
.. link:
.. description:
.. type: text

Estos días, en mis ratos libres, además de leer The Martian, estoy haciendo algunas aportes a Nikola.

Algo a lo que le vengo dando vueltas es a la idea de importar tweets a este blog.

Hubo una época (o mejor dicho "hay", porque aún no termina) en la que Twitter mató a muchos blogs: 
más fácil, más rápido, más corto. *Fast food* para la era de la información.

Tengo la teoría, y de esto no estoy seguro, de que puedo rescatar mucha historia personal
de tweets que escribí y ya olvidé.

Con la página de Twitter podés ir para atrás en tu historia pero, superado cierto límite de tweets
ya no podés llegar al principio. Desde hace poco, Twitter te permite bajarse un archivo con todos 
tus tweets (incluso está acompañado por una aplicación web local con la cual es fácil navegarlos). 

Bueno, quiero tomar ese archivo, seleccionar los tweetsccon algún valor e importarlos como posts 
(tal vez agregados por día? por tema?) en este blog.

Abrí un `Issue <https://github.com/getnikola/plugins/issues/107>`_ para esto:

.. admonition:: Issue #107

    I'm planning to implement import_tweets. Version V0.1 will:

    * read from Twitter provided json files for a user
    * present each tweet asking the user if adding it or not
    * have a non-interactive parameter
    * have a parameter to filter replies
    * generate rst posts, one per day with tweets
    * (probably) download images and include them in the posts
    * Ideas or suggestions?
