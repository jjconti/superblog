<html><body><p>Estas son los slides (más texto con el grueso de lo que dije) de mi charla en <a href="http://ar.pycon.org/2009/about/" target="_blank">PyCon Argentina 2009</a>. La misma se anunciaba como:

</p><blockquote>Taint Mode es una característica implementada en algunos lenguajes con el objetivo de prevenir que usuarios malintencionados alteren entradas al sistema para lograr la ejecución de comandos no permitidos u otros tipos de ataques.

En esta charla se introducen los conceptos básicos de Taint Mode y se discute la forma de implementarlo en Python mediante el uso de decoradores. Se muestra una implementación concreta y se analizan sus resultados.</blockquote>

<img class="aligncenter size-full wp-image-1769" title="img0" src="/wp-content/uploads/2009/09/img0.jpg" alt="img0" width="512" height="384">

<!--more--><img class="aligncenter size-full wp-image-1770" title="img1" src="/wp-content/uploads/2009/09/img1.jpg" alt="img1" width="512" height="384">



Cómo digo ahí, no soy un experto en seguridad aunque es un área que me interesa, sino me considero un desarrollador.



Cómo desarrollador, muchas veces me encuentro dejando de lado la seguridad por cuestiones más apremiantes.



<strong>Por hacer lo urgente, no hacemos lo importante.</strong>



Entonces las fechas límite para entregas, las presiones por incorporar nuevas características, el pago <em>solo</em> por lo que se ve, hace que mucho software salga a la calle sin los más mínimos recaudos de seguridad.



Esto trae consecuencias graves para muchas organizaciones y personas, como:

<ul>

	<li>Robo o alteración de información</li>

	<li> Bloqueos en la disponibilidad de un recurso</li>

	<li> Suplantación de identidad</li>

</ul>

<p style="text-align: left;">Formas de mitigar este problema sin duda hay muchas. Una puede ser contar con herramientas que en tiempo de desarrollo permitan verificar la existencia de vulnerabilidades en el código escrito. ¿Qué vulnerabilidades? ¿Todas? Eso sería seguramente imposible. Pero existen herramientas que se especializan en distintos nichos: buffer overflow en C, XSS en PHP.</p>



Empecé a prestarle atención a este tipo de cosas cuestiones cuando empecé a participar de un grupo de investigación sobre seguridad en mi facultad. Yo me estaba postulando para obtener una beca de maestría y una de las condiciones era participar de un grupo de investigación.



Así que empecé a buscar en Internet papers que relacionen cuestiones de  seguridad con Python, como una forma de encontrar algún tema que me interese y pueda profundizar.



Encontré algunos papers de 2 investigadores de la Universidad Estatal de Moscú, Andrew Petukhov y Dimitry Kozlov en los que discutían cómo implementar Taint Mode en Python. Si bien su enfoque consistía en modificar el intérprete en C de Python para lograrlo, de su trabajo incorporé la mayoría de los conceptos que voy a mencionar en la primer parte de la charla. A diferencia de ellos, mi implementación de Taint Mode para Python está escrita totalmente en Python.

<img class="aligncenter size-full wp-image-1771" title="img2" src="/wp-content/uploads/2009/09/img2.jpg" alt="img2" width="512" height="384">

<img class="aligncenter size-full wp-image-1772" title="img3" src="/wp-content/uploads/2009/09/img3.jpg" alt="img3" width="512" height="384">



El modelo de las manchas intenta describir cómo se comportan los valores que ingresan a un sistema desde el exterior y tiene 3 componentes fundamentales.



<strong>FUENTES NO CONFIABLES, FUNCIONES LIMPIADORAS Y SUMIDEROS SENSIBLES.</strong>



Todo valor que ingresa a un programa desde el exterior, es considerado por defecto como un valor manchado, ya que no sabemos de su procedencia. Decimos que viene de una fuente no confiable. Los valores recibidos desde el exterior pueden haber sido deliberadamente modificados para causar daño o simplemente por error causar un un problema dentro del sistema.Estas manchas se propagan por el programa mediante operaciones como la asignación o la concatenación.



Las funciones limpiadoras representan los mecanismos que se pueden utilizar dentro de un programa para convertir un valor manchado en un limpio: escapando, codificando o incluso eliminando caracteres sospechosos.



Los valores manchados no deben ser utilizados para: generar respuestas hacia los clientes o construir comandos a ser utilizados contra servicios externos, como los provistos por el sistema operativo, motores de bases de datos o el mismo intérprete. A estos componentes a los que no queremos que lleguen valores manchados, los denominamos "sumidero sensible".

<img class="aligncenter size-full wp-image-1773" title="img4" src="/wp-content/uploads/2009/09/img4.jpg" alt="img4" width="512" height="384">



Si un valor manchado alcanza un sumidero sensible, entonces existe una vulnerabilidad en el programa.



De esto se deduce que los valores manchados deben ser limpiados antes de que el flujo del programa los lleve hacia un sumidero sensible.



Esto es correcto, pero debemos preguntarnos: ¿son todas las manchas iguales? ¿Una función limpiadora puede quitar todas las manchas de un valor? ¿Son todos los sumideros sensibles al mismo tipo de mancha? NO.

<ul>

	<li> Un valor puede tener más de un tipo de mancha.</li>

	<li>Una función limpiadora, por lo general, limpia un solo tipo de mancha.</li>

	<li>Un sumidero es sensible a un solo tipo de mancha.</li>

</ul>

Cuando un valor ingresa al programa, no sabemos que manchas tiene ¿Debe un desarrollador aplicar todas las funciones limpiadoras a cada valor que procede de una fuente no confiable? No toda función limpiadora es apropiada para procesar todos los valores manchados e incluso hacerlo consumiría recursos en forma innecesaria.



Una mejor estrategia es, dado un tipo de mancha determinado, aplicar una función limpiadora de esta mancha solo a aquellos valores que alcanzarán un sumidero sensible a la mancha en cuestión.

<img class="aligncenter size-full wp-image-1774" title="img5" src="/wp-content/uploads/2009/09/img5.jpg" alt="img5" width="512" height="384">



En concreto. Este valor está manchado con SQL Injection y no deberíamos dejar que forme parte de una sentencia que se va a ejecutar contra una base de datos. Pero, en principio, no habría problemas en que se use para renderizar una página que será devuelta al usuario.



Algo similar sucede con este valor. Si bien está manchado para XSS. En principio no habría problemas en que se utilice para generar un comando a ejecutar contra el sistema operativo.

<img class="aligncenter size-full wp-image-1776" title="img7" src="/wp-content/uploads/2009/09/img7.jpg" alt="img7" width="512" height="384">

<img class="aligncenter size-full wp-image-1777" title="img8" src="/wp-content/uploads/2009/09/img8.jpg" alt="img8" width="512" height="384">



Tres menciones sobre la implementación antes de ver ejemplos de uso.



1) Existen 2 formas generales de implementar este tipo de análisis. De forma estática o de forma dinámica. Una implementación estática realiza la detección analizando el texto de un programa, sin ejecutarlo. Mientras que una implementación dinámica, analiza el coportamiento del programa. Esta es una implementación dinámica, por lo que va a requerir que el programa a evaluar sea ejecutado y utilizado: ejecutando manualmente casos de uso o corriendo tests automatizados.



2) El uso de módulo requiere que sea importado dentro del programa a evaluar y hacer algunas modificaciones en el código fuente. Es intrusivo.



3) La implementación se basa en el uso de decoradores. Existen decoradores para marcar dentro del programa los 3 tipos de elementos del modelo de las manchas: FUENTES NO CONFIABLES, FUNCIONES LIMPIADORAS Y SUMIDEROS SENSIBLES.

<img class="aligncenter size-full wp-image-1778" title="img9" src="/wp-content/uploads/2009/09/img9.jpg" alt="img9" width="512" height="384">

<img class="aligncenter size-full wp-image-1779" title="img10" src="/wp-content/uploads/2009/09/img10.jpg" alt="img10" width="512" height="384">



Cada tipo de mancha con la que va a trabajar el módulo es identificada por un entero. En la lista KEYS que se ve en la pantalla, XSS es identificada con el 0, SQLI con el 1 y así. Esta lista de valores debe ser modificada si se quiere agregar nuevas vulnerabilidades para que sean reconocidas por la herramienta.



TAINTED es la la estrucutura de datos dónde se lleva el registro de qué variables están manchadas. Es un diccionario dónde las claves son los enteros de la lista KEYS sus valores conjuntos, sets, inicialmente vacíos. Cuando se recibe un valor manchado del exterior, este es almacenado en todos los conjuntos, ya que por defecto tiene todas las manchas y a medida que se va limpiando, es eliminado del conjunto correspondiente.



STR, en mayúsuculas, es una clase que envuelve a la clase str, en minúsculas, provista por Python. Ya que en Python los strings son inmutables, siempre que se procesa un string, por ejemplo cuando se obtiene un substring, se crea un nuevo objeto. Esta clase es necesaria para sobreescribir los métodos que generan un nuevo string y así hacer que la mancha perdure a lo largo del flujo del programa. Por ejemplo:

<img class="aligncenter size-full wp-image-1780" title="img11" src="/wp-content/uploads/2009/09/img11.jpg" alt="img11" width="512" height="384">



Si a está manchada, y b está limpia. El string que se obtiene de concatenarlos, también está manchado. Lo mismo sucede con otras operaciones sobre strings: multiplicación, rebanada, formateo, métodos como upper que convierten el string a mayúsculas, o split que devuelve una lista de strings. Por ejemplo, si en este último caso 'a' sería un string de palabras separadas por coma, esta llamada al método split devolvería una lista de palabras y cada una estaría manchada.



Los siguientes elementos a mostrar son los decoradores necesarios para que los elementos del programa manchen variables, las limpien o se alarmen.

<img class="aligncenter size-full wp-image-1781" title="img12" src="/wp-content/uploads/2009/09/img12.jpg" alt="img12" width="512" height="384">untrusted es un decorador utilizado para indicar que los valores retornados por una función o método no son confiables. Como los valores no confiables pueden contener potencialmente cualquier tipo de mancha, estos valores son marcados como manchados por todos los tipos de machas.



Si se tiene acceso a la definición de la función o método, se puede utilizar la sintáxis provista por Python para aplicar el decorador.

Al usar módulos de terceros, podemos aplicar de todas formas el decorador. Este ejemplo es de un programa que utiliza el framework web.py.

<img class="aligncenter size-full wp-image-1782" title="img13" src="/wp-content/uploads/2009/09/img13.jpg" alt="img13" width="512" height="384">



Algunos frameworks funcionan de una forma diferente: le piden al programador que escriba cierta función o método de forma tal que luego el framework las utiliza para pasarle como parámetro al programa de usuario los valores recibidos desde el exterior. El framework para hacer aplicaciones de red, Twisted, provee un claro ejemplo  cuando se extiende la clase LineOnlyReceiver. Nos pide sobreescribir el método lineReceived, el cual se ejecutará cada vez que se recibe una cadena desde el exterior.



En estos casos, utilizar el decorador untrusted es engorroso o incluso imposible. En su lugar se debe utilizar el decorador untrusted_args, que recibe 2 argumentos opcionales: una lista de posiciones de argumentos no confiables y una lista de argumentos de palabra clave.



En el ejemplo se indica que el argumento de posición 1 no es confiable, y debe ser mancado como tal. Entonces cuando se ejecute el método, el valor recibido será manchado.



Tanto para el decorador untrusted como untrusted_args, se utiliza la siguiente regla para marcar valores:

<ol>

	<li>Si el valor a manchar es un string, se utiliza para crear una instancia de STR y este objeto es guardado en TAINTED.</li>

	<li>Si el valor es una lista. Se aplica este algoritmo a todos los elementos de la lista y se retorna una nueva lista con el resultado de cada aplicación.</li>

	<li>Si el valor es un diccionario. Se aplica este algoritmo a todos los valores del diccionario y se retorna un nuevo diccionario con las claves originales y los resultados de cada aplicaicón como valores.</li>

</ol>

<img class="aligncenter size-full wp-image-1784" title="img14" src="/wp-content/uploads/2009/09/img141.jpg" alt="img14" width="512" height="384">



Una vez que los valores manchados ingresan en el programa, fluirán a lo largo del mismo y en algún momento, puede ser que se encuentren con una función limpiadora como esta. texto_plano elimina las marcas html de un string.



cleaner es un decorador utilizado para indicar que un método o función tiene la habilidad de limpiar manchas en un valor. Se debe indicar mediante un parámetro el tipo de mancha que la función es capás de limpiar. Como con los otros decoradores, tenemos dos formas de aplicarlo: dependiendo de si tenemos acceso o no a la definición de la función limpiadora.



Funciona de la siguiente forma: si la función texto_plano decorada se aplica al primer ejemplo, nada cambia. Como el valor retornado es distinto al argumento, un proceso de limpieza fue llevado acabo. El valor argumento sigue en la estructura de datos TAINTED.



En cambio, si es aplicada al segundo ejemplo, el valor argumento es igual al retornado, no se limpió nada por que no se requería limpiar nada. El valor original, presumido manchado, en realidad no estaba manchado (para XSS) y por eso es removido del conjunto correspondiente.



<img class="aligncenter size-full wp-image-1785" title="img15" src="/wp-content/uploads/2009/09/img15.jpg" alt="img15" width="512" height="384">



Los últimos elementos a marcar en el programa son los sumideros sensibles.



Se utiliza el decorador ssink para marcar aquellas funciones o métodos que no queremos sean alcanzadas por valores manchados.



La función eval de Python es un típico ej. de sumidero sensible a ataques de Interpreter Injection, ya que interpreta ciegamente el string que recibe como  argumento.



Supongamos q nuestro programa es una calculadora e implementamos la funcionalidad de sumar 2 números evaluando el string formado por: un primer valor recibido del exterior, el signo más y un segundo valor recibido desde el exterior. Si los valores no son apropiadamente validados, un atacante, utilizando nuestra calculadora, podría leer el contenido de archivos locales, borrarlos, colgar el programa o cualquier otra cosa que se pueda hacer desde el intérprete de Python.



Aplicando el decorador a eval podemos detectar cuando esta función es utilizada con un valor no confiable como parámetro. Otra forma de lograr el mismo efecto en el ejemplo sería aplicando el decorador a la función suma en lugar de a eval.



<img class="aligncenter size-full wp-image-1786" title="img16" src="/wp-content/uploads/2009/09/img16.jpg" alt="img16" width="512" height="384">



El segundo ejemplo también es tomado del framework web.py y marca como sumideros sensibles a SQL Injection los métodos delete, select e insert del objeto que accede a la base de datos.



<img class="aligncenter size-full wp-image-1787" title="img17" src="/wp-content/uploads/2009/09/img17.jpg" alt="img17" width="512" height="384">



Con las fuentes inseguras, las funciones limpiadoras y los sumideros sensibles marcados en el programa, podemos ejecutarlo y utilizarlo para ir obteniendo las advertencias sobre posibles problemas de seguridad. Se pueden obtener mensajes de este tipo por la salida estándar, escribir en un archivo o daler cualquier otro destino.



<img class="aligncenter size-full wp-image-1788" title="img18" src="/wp-content/uploads/2009/09/img18.jpg" alt="img18" width="512" height="384">



Algunas otras cosas que podemos encontrar con/en el módulo:

<ul>

	<li>una batería de más de 80 tests que prueban su funcionalidad</li>

	<li>la posibilidad de definir la función que se ejecutará cuando una variable manchada con X alcanza un sumidero sensible a X</li>

	<li>la posibilidad de establecer una bandera que indique si la ejecución se debe cortar o no cuando una variable manchada con X alcanza un sumidero sensible a X</li>

	<li>un nuevo decorador, validator, para marcar funciones que retornan un valor booleano indicando si una variable puede usarse o no</li>

	<li>funciones auxiliares para manchar un valor o para testear si un valor está manchado</li>

</ul>

<img class="aligncenter size-full wp-image-1789" title="img19" src="/wp-content/uploads/2009/09/img19.jpg" alt="img19" width="512" height="384">



Último slide de la charla. Todo lo que mostré hasta ahora es un experimento. Puede haber errores u omisiones, de hecho mientras lo fui desarrollando, al probarlo con aplicaciones reales encontraba errores en la implementación o situaciones en los que no podía aplicarlo, lo que me obligaba a darle una vuelta más de rosca a la implementación: así surgió por ejemplo el decorador untrusted_args.



La pregunta ahora es cómo seguimos, y el objetivo de la charla era justamente presentar esta idea entre desarrolladores Python para continuarla en conjunto. Hay  muchas que podemos pensar, desde detalles de implementación hasta casos de uso que se pueden lograr, integración con frameworks de desarrollo para que alguien que se sienta a codificar un sistema tenga facilitada la aplicación de esta herramienta.



Por ejemplo, para web.py sería relativamente sencillo crear un parche para que por defecto los valores recibidos estén manchados. En Django hice el ejercicio de escribir un middleware que haga ese trabajo. Y así, es necesario ir probando cómo se puede adaptar el módulo a herramientas de desarrollo ya conocidas.



Hace poco cree una <a href="http://groups.google.com/group/python-taint" target="_blank">lista de correos en Google Groups</a> para charlar estos temas, así que los que estén interesados en discutir al respecto y desarrollar esta herramienta, pueden suscribirse.



<img class="aligncenter size-full wp-image-1790" title="img20" src="/wp-content/uploads/2009/09/img20.jpg" alt="img20" width="512" height="384">

<img class="aligncenter size-full wp-image-1794" title="img21" src="/wp-content/uploads/2009/09/img21.jpg" alt="img21" width="512" height="384"></body></html>