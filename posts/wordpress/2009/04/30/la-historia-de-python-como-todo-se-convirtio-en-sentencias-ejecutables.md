<html><body><em>El siguiente texto es una traducción del artículo How Everything Became an Executable Statement de Guido van Rossum publicado en <a href="http://python-history.blogspot.com/" target="_blank">http://python-history.blogspot.com/</a>.</em>

<!--more-->

<h2>Cómo todo se convirtió en sentencias ejecutables</h2>

Los nuevos usuarios de Python a veces se sorprenden al descubrir que todas las partes del lenguaje son sentencias ejecutables, incluyendo la definición de funciones y clases. Eso significa que cualquier sentencia puede aparecer en cualquier lugar en un programa. Por ejemplo, una definición de una función puede aparecer dentro de una sentencia "if" si así se lo desea.



En una versión muy temprana de la gramática de Python esto no era así: los elementos de la gramática tenían un "sabor decorativo", las sentencias import y la definición de funciones solo eran permitidas en el nivel superior de un módulo o script (dónde eran ejecutadas para efectivizarse).



De todas formas, cuando estaba agregando soporte para clases, decidí que esto era muy restrictivo.



Mi razonamiento fue más o menos como sigue. En lugar de definir el cuerpo de una clase sólo como una serie de declaraciones de funciones, también parecía adecuado permitir asignaciones a variables allí. De todas formas, si iba a permitir eso, ¿por qué no ir un escalón más arriba y permitir código ejecutable arbitrario? O, llevando esto aún más lejos, ¿por qué no permitir declaración de funciones dentro de sentencias "if", por ejemplo? Rápidamente se vio que esto permitía una simplificación de la gramática, ya que ahora todos los usos de sentencias (estén identados o no) podían compartir la misma regla de gramática, y de hecho el compilador podría usar la misma función generadora de byte code para todas ellas.



A pesar de que este razonamiento me permitía simplificar la gramática y los usuarios podían colocar sentencias Python en cualquier lugar, esta característica no habilitaba necesariamente ciertos estilos de programación. Por ejemplo, la gramática de Python técnicamente permitía a los usuarios escribir cosas como funciones anidadas aunque la semántica subyacente de Python no aceptara ámbitos anidados. Por lo tanto, el código así operaría de formas inesperadas o "rotas" comparadas con lenguajes que realmente estaban diseñados con esa característica en mente. Con el paso del tiempo, muchas de esas características "rotas" se arreglaron. Por ejemplo, la definición de funciones anidadas sólo empezó a funcionar un poco más correcta en Python 2.1.

<em>Traducido por Juan José Conti.

Revisado por César Portela.

Si encontrás errores en esta traducción, por favor reportalos en un comentario y los corregiremos a la brevedad.</em>

Todas las traducciones de esta serie pueden encontrarse en <a href="/categoria/aprendiendo-python/historia/" target="_self">La historia de Python</a>.</body></html>