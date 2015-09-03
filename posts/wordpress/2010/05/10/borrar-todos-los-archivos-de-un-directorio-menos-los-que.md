<html><body><a href="/wp-content/uploads/2010/05/ter.png"><img class="alignright size-full wp-image-2236" title="ter" src="/wp-content/uploads/2010/05/ter.png" alt="ter" width="128" height="128"></a>Menos los que respetan un PATRON:



<code>for a in `ls | grep -v PATRON`; do rm -fr $a; done</code>



Menos los que contienen tar.gz en su nombre:



<code>for a in `ls | grep -v tar.gz`; do rm -fr $a; done</code>



Útil en muchas situaciones.



La línea de comandos es tu amiga.</body></html>