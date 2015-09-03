<html><body><p>Si tenés un blog con Wordpress y te atrasás con las actualizaciones (o no) tarde o temprano te embocan (no es la primera vez que me pasa). Alguna herramienta automática detecta que estás corriendo una versión vulnerable a cierto fallo de seguridad reciente y otra inserta código malicioso en todos los archivos de tu sistema de blogging en los que pueda escribir.



Las consecuencias son que cuando tus visitantes intenta entrar al blog son redirigidos a un sitio porno o de venta de Viagra. Si se accede con Chrome a uno de estos sitios infectados, un enorme cartel rojo de avisa que el sitio incluye contenido de una web rumana reportada como distribuidora de malware.



Tu hosting te manda un mail diciéndote que no te sientas solo por que no lo estás, pero en realidad si lo estás. Te recomiendan cosas poco prácticas como actualizar, cambiar claves o restaurar un back-up previo a la infección. Tengo casi 1000 archivos .php llenos de código malicioso y me decís que cambié mis claves (?). Necesito una forma de arreglar esto.



Dejo aquí unos tips en base a mi experiencia personal, con la certeza de que en cualquier momento voy a volver a buscarlos por necesidad.



Muchas de las herramientas que agregan código malicioso (las más simples) agregan una línea al principio de todos los .php en los que pueden escribir. En mi caso esta línea tenía esta forma:

</p><pre> &lt;?php /**/ eval(base64_decode("aWYoZnVuY3...oZnVu"));?&gt;&lt;?php</pre>

(código codificado que es decodificado y evaluado al ejecutar el archivo).



¿Qué archivos están infectados?

<pre lang="bash">grep -l eval\(base64_decode -R *</pre>

¿Cuantos archivos hay infectados? (aprox.)

<pre lang="bash">grep -l eval\(base64_decode -R * | wc -l</pre>

Limpiar todos los archivos:

<pre lang="bash">for x in `grep -l eval\(base64_decode -R * | grep -v .back`; do sed -i.back '1d' $x ; sed -i '1 i <?php ' $x; done</pre>

El anterior comando busca todos los archivos infectados (excepto los que tienen extensión .back), les borra la primer línea y luego les agrega una primer línea "



Mejoras, sugerencias y correcciones bienvenidas!</pre></body></html>