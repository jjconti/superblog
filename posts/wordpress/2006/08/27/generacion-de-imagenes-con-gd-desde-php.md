<html><body><p>Este es un ejemplo minimalista (pero de alguna utilidad) en el que un script php devuelve una imagen.

<!--more-->

</p><h2>Antes que nada</h2>

Para que funcione hay que tener instalado el paquete php4-gd, descomentar la línea <code>extension=gd.so</code> en el archivo <code>/etc/php4/apache2/php.ini</code> y reiniciar el servidor web (apache).



<h2>Barra de progreso</h2>

Este script recibe como parámetro un pocentaje (10, 20, 50 o 90, qué tan completa está una tarea) y genera la barra de progreso correspondiente.



Ver archivo: <a href="../../../../files/progreso.php.html">progreso.php</a>



Si accedemos a este script desde un navegador y le damos un valor al parámetro <code>porcentaje</code> obtendremos imágenes como estas:



(suponiendo que el archivo está en <code>/home/juanjo/public_html/</code>)



<strong>http://localhost/~juanjo/progreso.php?porcentaje=10</strong>

<center><img id="image139" src="http://firebirds.com.ar/%7Ejuanjo/wordpress/wp-content/uploads/2006/08/10.png" alt="10"></center>



<strong>http://localhost/~juanjo/progreso.php?porcentaje=20</strong>

<center><img id="image140" src="http://firebirds.com.ar/%7Ejuanjo/wordpress/wp-content/uploads/2006/08/20.png" alt="20"></center>



<strong>http://localhost/~juanjo/progreso.php?porcentaje=60</strong>

<center><img id="image141" src="http://firebirds.com.ar/%7Ejuanjo/wordpress/wp-content/uploads/2006/08/60.png" alt="60"></center>



<strong>http://localhost/~juanjo/progreso.php?porcentaje=90</strong>

<center><img id="image142" src="http://firebirds.com.ar/%7Ejuanjo/wordpress/wp-content/uploads/2006/08/90.png" alt="90"></center>

Más interesante que acceder directamente a este script es utilizarlo como fuente para una etiqueta <code>img</code> en html.  Podemos tener un template donde haya algo como esto:



<code>

&lt;img src="progreso.php?porcentaje={P}"/&gt;

</code> 



y a P se le da un valor calculado dinámicamente cada vez que se solicita la página.

<h2>Recursos</h2>

Un ejemplo más completo en: <a href="http://www.zend.com/zend/tut/dynamic.php">http://www.zend.com/zend/tut/dynamic.php</a> (fué el hola-mundo con el que empecé a probar GD)



GD en php.net: <a href="http://www.php.net/gd">http://www.php.net/gd</a>

</body></html>