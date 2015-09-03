<html><body><p>Hace unos días <a href="http://grulic.org.ar/lurker/message/20070418.172626.30d2f52b.en.html" title="mi mail a PyAr" target="_blank">mandé a la lista de correos de PyAr</a> una implementación inicial del juego <a href="http://en.wikipedia.org/wiki/Fifteen_puzzle" title="N-Puzzle" target="_blank">N-Puzzle</a>. <a href="http://juanjoconti.com.ar/files/python/n-puzzle-0.1.tgz" title="n-puzzle-0.1.tgz">n-puzzle-0.1.tgz</a>.



Es muy sencilla. Toma una imagen, la parte en cuadraditos, quita uno de los cuadraditos y los mezcla. Luego uno puedo deslizar los cuadraditos adyasentes al espacio en blanco con las flechas de teclado. El objetivo del juego es recomponer la imagen original.



</p><center><img src="/wp-content/uploads/2007/04/pantallazo-n-puzzle001.png" title="N Puzzle 0.01" alt="N Puzzle 0.01"></center>Hoy estuve mejorando el código y agregándole una funcionalidad que permite que la computadora resuelva el problema (o nos ayude a hacerlo).La idea original para este programa es luego utilizarlo para probar los métodos de búsqueda que estamos estudiando en <a href="http://www.frsf.utn.edu.ar/matero/visitante/index.php?id_catedra=142" title="IA Cátedra" target="_blank">Inteligencia Artificial</a>.



<!--more--> Ojo! Si bien en esta nueva versión apretando la tecla 'S' entramos y salimos del modo Auto Solve, no estoy usando IA para implementarlo. Siempre pueden mirar el código y ver como lo estoy haciendo :)



Actualmente el juego está planteado como una prueba de concepto más que como un programa totalmente usable. Esto implica que pueden ocurrir errores durante su ejecución y que algunas opciones que podrían ser configurables están clavadas en el código:

<ul>

	<li>N es el número de fichas que participan del juego: 8 (en un tablero de 3 x 3), 15 (en uno de 4 x 4), 24 (en uno de 5 x 5). Por defecto es 8 pero puede cambiarse en el archivo <code>run.py</code>.</li>

	<li>La imagen que se usará para generar las fichas se llama ejemplo.jpg y debe estar en el mismo directorio que los scripts (yo proveo una). Pueden pisarla con otra imagen o pueden cambiar la ruta a la misma en el archivo <code>run.py</code>. La imagen debe ser de 600 x 600 pixeles.</li>

	<li>El desordenamiento original del tablero se efectua mediante un número X de movimientos. En el código fuente el valor usado es 20 pero puede cambiarse en el método <code>__init__</code> de la clase Puzzle en el archivo <code>puzzle.py</code> (van a encontrarlo en la llamada al método <code>_shuffle</code>).</li>

</ul>

El puzzle resuelto se ve así:



<center><img src="/wp-content/uploads/2007/04/pantallazo-n-puzzle-solved.png" title="N Puzzle solved" alt="N Puzzle solved"></center>La última versión puede encontrarse en: <a href="http://www.juanjoconti.com.ar/files/python/n-puzzle-0.1-1.tgz" title="n-puzzle-0.1-1.tgz">files/python/n-puzzle-0.1-1.tgz</a>.Y este es el CHANGELOG de mi primer intento a este segundo mejorado:

<blockquote>0.1-1:



mix(x,y) se realiza ahroa como x,y = y,x en lugar de usar

una variable temporal.



Cada Card tiene un cid (Card ID), un par i,j correspondiente

a su posición original en el tablero.



El desordenado del tablero se realiza mediante el movimiento

aleatorio de las piezas (usando los métodos up, down, right

y left) para evitar que el juego comience con una configuración

que no tiene solución (Para un ejemplo, Google: 14-15 Puzzle).



Apretando la tecla 'S' se entra y sale del modo 'Auto Solve' en

el cual la computadora nos ayuda a resolver el juego. Atención:

NO IA was used in this feature.</blockquote>

Requiere <a href="http://www.python.org" title="Python" target="_blank">Python</a> y <a href="http://www.pygame.org" title="Python Game Lib" target="_blank">PyGame</a>. Si tienen problemas para instalarlos mandenme un mail y los ayudo.</body></html>