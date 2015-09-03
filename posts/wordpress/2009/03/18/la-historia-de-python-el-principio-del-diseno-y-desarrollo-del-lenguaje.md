<html><body><em>El siguiente texto es una traducción del artículo Early Language Design and Development Guido van Rossum publicado en <a href="http://python-history.blogspot.com/" target="_blank">http://python-history.blogspot.com/</a>.</em>

<!--more-->

<h2>El principio del diseño y desarrollo del lenguaje</h2>

<h3>De ABC a Python</h3>

La primera y principal influencia de Python fue <a href="http://homepages.cwi.nl/%7Esteven/abc/" target="_blank">ABC</a>, un lenguaje diseñado a principios de los 80 por Lamber Meertens, Leo Geurts y otros en CWI. El objetivo de ABC era ser un lenguaje de enseñanza, un reemplazo para BASIC, y un lenguaje y entorno para computación personal. Fue diseñado en un principio haciendo un análisis de la tarea de programar y luego haciendo varias iteraciones que incluían pruebas de usuario a conciencia. Mi rol en el grupo de ABC era principalmente implementar el lenguaje y su entorno integrado de edición.



El uso que Python hace de la identación viene directamente de ABC, pero esta idea no se originó con ABC (ya había sido promovida por Donald Knuth y era un concepto bien conocido de estilo de programación). (El lenguaje de programación <a href="http://en.wikipedia.org/wiki/Occam_programming_language" target="_blank">occam</a> también lo usaba). Si embargo, los autores de ABC sí inventaron el uso de los dos puntos que separa la cláusula inicial del bloque identado. Luego de las primeras pruebas con usuarios sin los dos puntos, se descubrió que el significado de la identación no le quedaba claro a los principiantes que tomaban sus primeras lecciones de programación. Agregar los dos puntos clarificó su significado: los dos puntos de alguna formar guiaban la atención a lo que seguía y unía lo anterior con lo siguiente de forma correcta.



Los principales tipos de datos de Python también vienen de ABC, aunque con algunas modificaciones. Las listas en ABC eran en realidad bags o multisets, que siempre se mantenían ordenadas utilizando una implementación modificada de árboles B. Sus tablas eran arrays asociativos que se mantenían ordenados en forma similar mediante claves. Encontré que ningún tipo de dato era preciso para representar, por ejemplo, la secuencia de líneas leídas de un archivo, el cual anticipé que sería un caso de uso común (en ABC tenías que usar una tabla con el número de línea como clave, pero eso complicaba las inserciones y los borrados). Entonces convertí el tipo lista en un array flexible con operaciones de inserción y borrado, dándole a los usuarios control total sobre el orden de los elementos en una lista. Un método sort soportaba la necesidad ocasional de resultados ordenados.



También reemplacé las tablas ordenadas implementando una tabla hash. Elegí una tabla hash porque creía que sería más rápida y fácil de implementar que el árbol B de ABC. Estaba teóricamente probado que los árboles B eran asintóticamente óptimos en tiempo y espacio para una gran variedad de operaciones, pero en la práctica se volvieron difíciles de implementar correctamente debido a la complejidad de sus algoritmos. Por la misma razón, la performance tampoco era óptima para tablas pequeñas.



Mantuve el tipo de dato inmutable de ABC llamado tupla (las operaciones de empaquetado y desempaquetado en Python vienen directamente de ABC). Ya que las tuplas son implementadas mediante arrays, decidí agregarles indexación y rebanado.



Una consecuencia de añadirle una interfaz de tipo array a las tuplas fue que tuve que pensar en una forma de resolver los casos límites de tuplas de longitud 0 ó 1. Una de las reglas que tomé de ABC fue que cada tipo de datos, al ser impreso o convertido a string, debía ser representado por una expresión que sea una entrada válida para el parser del lenguaje. De esto siguió que necesitaba notaciones para las tuplas de longitud 0 y 1. Al mismo tiempo no quería perder la distinción entre una tupla y una expresión entre paréntesis, entonces utilicé un enfoque feo pero pragmático en el cual una coma final convertiría una expresión en una tupla de un elemento y "()" representaría a una tupla de cero elementos. Vale la pena mencionar que los paréntesis por lo general no son necesarios en la sintaxis de Python, excepto aquí (representar la tupla vacía con "nada" podría fácilmente enmascarar errores genuinos).



Los strings de Python empezaron con una semántica (inmutable) muy parecida a los strings de ABC, pero con una notación diferente e indexación basada en 0. Ya que ahora tenía tres tipos indexables -listas, tuplas y strings- decidí generalizar todo en un concepto común, la secuencia. Esta generalización hizo que ciertas operaciones básicas como obtener la longitud (len(s)), indexar (s[i]), rebanar (s[i:j]) e iterar (for i in s) funcionen de la misma forma en cualquier tipo que sea una secuencia.



Los números son uno de los puntos en los que más en desacuerdo estuve con ABC. ABC tenía dos tipos de números en tiempo de ejecución; los números <em>exactos</em> que eran representados como números racionales de precisión arbitraria y los números <em>aproximados</em> que eran representados mediante punto flotante binario con un rango de exponente extendido. Los números racionales no encajaban en mi visión del tema (anécdota: una vez intenté computar mis impuestos usando ABC. El programa, que parecía bastante directo, estaba demorando mucho en computar unos pocos números. Luego de investigar descubrí que estaba haciendo aritmética con números con miles de dígitos de precisión, que tenían que ser redondeados a florines -pie 100 centavos holandeses - y centavos para ser impresos). Es por esto que para Python elegí un modelo más tradicional con enteros de máquina y punto flotante binario de máquina. En la implementación de Python, estos números son representados simplemente con los tipos de datos de C long y double respectivamente.



Creyendo que también había un caso de uso importante para números exactos sin límite, agregué un tipo de dato <em>bignum</em>, que llamé <em>long</em>. Ya tenía una implementación de bignum que había sido el resultado de un intento inconcluso por mejorar la implementación de ABC unos años antes (la implementación original de ABC, una de mis primeras contribuciones, usaba una representación decimal internamente). Sonaba lógico usar este código en Python.



A pesar de haber agregado bignums a Python, es importante enfatizar que no quería usar bignums para todas las operaciones entre enteros. De extrapolar lo que veía en programas escritos por mí y por colegas en CWI, sabía que las operaciones entre enteros representaban una porción significativa del total del tiempo que la mayoría de los programas corrían. El uso más común de los enteros es indexar secuencias que entran en memoria. Así, decidí usar enteros de máquina para los casos de uso más comunes y el rango extra de bignums solo para hacer "matemática seria" o calcular la deuda externa de Estados Unidos en peniques.

<h3>El problema con los números</h3>

La implementación de números, especialmente enteros, es un área en la que cometí varios errores de diseño serios, pero también aprendí lecciones importantes sobre el diseño de Python.



Ya que Python tiene dos tipos diferentes de enteros, necesitaba una forma de distinguir entre los dos tipos en un programa. Mi solución era pedirle a los usuarios que explícitamente digan cuando querían usarlos agregando una L al final de los números (por ejemplo 1234L). Esta es un área en la que Python violaba la filosofía inspirada en ABC de no necesitar que los usuarios se encargar de detalles de implementación que no les importaban.



Lamentablemente, este era solo el menor detalle de un problema mayor. Un error más ilustre fue que mi implementación de enteros y longs ¡tenía una ligera diferencia semántica en algunos casos! Ya que el tipo int era representado como un entero de máquina, las operaciones que desbordaban silenciosamente recortaban el resultado a 32 bits o a la precisión que el tipo long de C tuviera. Además, el tipo int, que normalmente se considera tiene signo, era tratado como sin signo por las operaciones bitwise y shift y en la conversión desde/hacia octales o hexadecimales representados como int o long. Los longs, por otro lado, siempre se consideraban con signo. Por lo tanto, algunas operaciones producían un resultado diferente, dependiendo de si un argumento era representado como int o como long. Por ejemplo, en una aritmética de 32 bits, 1&lt;&lt;31 (1 shift a izquierda 31 bits) produciría el entero negativo más grande de 32 bits y 1&lt;&lt;32 produciría cero, mientras que 1L&lt;&lt;31 (1 representado como long shift a izquierda 31 bits) produciría un entero enorme igual a 2**31 y 1L&lt;&lt;32 produciría 2**32.



Para resolver algunos de estos asuntos hice un arreglo simple. En lugar de tener operaciones entre enteros que recorten silenciosamente el resultado, cambié la mayoría de las operaciones aritméticas para que lancen una excepción OverflowError cuando el resultado no encaje. (La única excepción a este control eran las operaciones de "bit-wise" mencionadas anteriormente, ya que asumí que los usuarios esperarían que estas operaciones se comporten como en C). Si no hubiese añadido este control, los usuarios de Python indudablemente hubiesen empezado a escribir código dependiente de la semántica de la aritmética binaria con signo de módulo 2**32 (como hacen los usuarios de C), y arreglar el error hubiese sido una transición mucho más dolorosa para la comunidad.



A pesar de que la inclusión del control de desborde pueda parecer un detalle de implementación menor, una dolorosa experiencia de debugging me hizo dar cuenta que era una característica útil. Como uno de mis primeros experimentos en Python, intenté implementar un algoritmo matemático simple, el computo de los "Números de Meertens", un poco de matemática recreativa inventada por Richard Bird al celebrar los 25 añosen WCI del principal autor de ABC. Los primeros números de Meertens son pequeños, pero al traducir el algoritmo en código no me había dado cuenta de que los resultados intermedios del computo eran mucho más grandes que 32 bits. Me llevó una larga y dolorosa sesión de debugging descubrir esto, y decidí entonces manejar el asunto controlando todas las operaciones entre enteros y lanzando una excepción siempre que el resultado no pueda ser representado como un long de C. El costo extra del control de desborde no se notaría junto a la sobrecarga que ya tenía con la decisión de implementación de crear un nuevo objeto para el resultado.



Lamentablemente, siento decir que lanzar una excepción por desborde ¡tampoco era la solución correcta! En ese entonces, estaba trabado por la regla de C "las operaciones con tipos numéricos T retornan un resultado de tipo T". Esta regla también era la razón de mi otro gran error en la semántica de los enteros: truncar el resultado de la división entre enteros, que discutiré en una de las próximas entradas. En retrospectiva, debí hacer que las operaciones entre enteros que desbordaban cambien el tipo de su resultado a long. Esta es la forma en que Python funciona hoy, pero completar esta transición llevó mucho tiempo.



A pesar del problema con los números, una cosa muy positiva salió de esta experiencia. Decidí que no debía haber valores de retorno no definidos en Python, en lugar de esto, siempre se lanzarían excepciones cuando un valor de retorno no correcto podía ser computado. Así, los programas escritos en Python nunca fallarían debido a que valores no definidos se estén pasando silenciosamente por detrás. Este es aún un principio importante del lenguaje, tanto en el lenguaje propiamente dicho como en las librerías.



<em>Traducido por Juan José Conti.

Revisado por César Portela.

Si encontrás errores en esta traducción, por favor reportalos en un comentario y los corregiremos a la brevedad.</em>

Todas las traducciones de esta serie pueden encontrarse en <a href="/categoria/aprendiendo-python/historia/" target="_self">La historia de Python</a>.</body></html>