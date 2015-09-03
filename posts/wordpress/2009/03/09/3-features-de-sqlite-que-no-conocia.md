<html><body><a href="http://www.sqlite.org/" target="_blank">SQLite</a> es (o se debate entre si es o no) un motor de base de datos liviano. No requiere configuración, no usa un servidor, su código ocupa poco espacio y una base de datos ocupa un solo archivo. Tal vez por estas características es usado no solo en aplicaciones de escritorio y sitios web, sino también dentro de: el lenguaje de programación PHP, el navegador web Firefox y muchos dispositivos móviles (<a href="http://www.sqlite.org/famous.html" target="_blank">más</a>). Hace unos días lo estoy usando para una aplicación Django mono-usuario. Hoy leyendo su página web, descubrí 4 características que no conocía, me llamaron la atención y me gustaron mucho.<!--more-->



La siguiente es una traducción libre de la página web de la herramienta.

<h2>El archivo de la base de datos se mantiene en distintas plataformas</h2>

El formato de archivo de SQLite es cross-platform. Un archivo de base de datos escrito en una máquina puede ser copiado a y usado en una máquina diferente con una arquitectura diferente. Big-endian o little-endian, 32-bit o 64-bit, no importa. Todas las máquinas usan el mismo formato de archivo. Más aún, los desarrolladores han mantenido el formato estabe y compatible hacia atrás, entonces versiones nuevas de SQLite pueden leer y escribir archivos de base de datos más viejos



La mayoría de los otros motores SQL requieren que bajes y restaures la base de datos al cambiar de una plataforma a otra y a menudo al actualizar a una nueva versión del software.

<h2>Tipado manifesto</h2>

La mayoría de los motores SQL usan tipado estático. Un tipo de dato es asociado con cada columna en una tabla y solo valores de ese tipo en particular se pueden guardar en esa columna. SQLite relaja esta restricción usando tipado manifiesto. En este tipo de tipado, el tipo de dato es una propiedad del valor en si mismo, no de la columna en el que el valor es almacenado. SQLite así permite que el usuario almacene cualquier valor de cualquier tipo de dato en una columna sin importar el tipo declarado de esa columna. (Hay algunas excepciones a esta regla: una columna de tipo INTEGER PRIMARY KEY solo almacenará enteros. Y SQLite intentará acomodar los valores al tipo de dato declarado en la columna cuando pueda).



Creemos que la especificación del lenguaje SQL permite el uso de tipado manifiesto. De todas formas, la mayoría de los otros motores SQL son estáticamente tipados y por eso algunas personas creen que el uso de tipado manifiesto es un bug en SQLite. Pero los autores de SQLite están convencidos de que esto es una característica valiosa. El uso de tipado manifiesto en SQLite es una decisión de diseño deliberada que ha probado en la práctica hacer que SQLite sea más confiable y fácil de usar, especialmente cuando se usa en combinación con lenguajes de programación dinámicamente tipados como Tcl y Python.

<h2>Registros de tamaño variable</h2>

La mayoría de los otros motores de base de datos SQL reservan una cantidad fija de espacio en disco por cada fila en la mayoría de las tablas. Hacen algunos trucos para manejar BLOBs y CLOBs que pueden tener un tamaño muy variable. Pero para la mayoría de las tablas, si declarás una columna de tipo VARCHAR(100), entonces el motor de base de datos reservará 100 bytes de espacio en disco sin importar cuanta información realmente guardes en esa columna.



SQLite, en contraste, usa dolo la cantidad de espacio en disco que realmente se necesita para almacenar la información en la fila. Si guardás un solo carácter en un columna de tipo VARCHAR(100), solo un byte de espacio en disco será consumido. (En realidad 2 bytes - hay cierta sobrecarga el principio de cada columna para guardar su tipo de dato y longitud).



El uso de registros de tamaño variable en SQLite tiene varias ventajas. Resulta en archivos de base de datos más pequeños, obviamente. También hace que la base de datos corra más rápido, ya que hay menos información que mover desde y hacia el disco. Y, el uso de registros de tamaño variable hace posible que SQLite use tipado manifiesto en lugar de tipado estático.

<h2>Más características</h2>

Una lista de todas las características de SQLite puede encontrarse en <a title="Características" href="http://www.sqlite.org/different.html" target="_blank">http://www.sqlite.org/different.html</a></body></html>