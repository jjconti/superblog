<html><body><em>El siguiente texto es una traducción del artículo How Exceptions Came to be Classes de Guido van Rossum publicado en <a href="http://python-history.blogspot.com/" target="_blank">http://python-history.blogspot.com/</a>.</em>

<!--more-->

<h2>Cómo las excepciones llegaron a ser clases</h2>



Pronto supe que quería que Python utilice excepciones para el manejo de errores. Sin embargo, una parte crítica para que las excepciones funcionen es lograr algún tipo de esquema para identificar distintos tipos de excepciones. En los lenguajes modernos (incluyendo el moderno Python :-), las excepciones son definidas en términos de clases definidas por los usuarios. Sin embargo, en los comienzos de Python, elegí identificar las excepciones por strings. Esto fue desafortunado, pero tenía dos razones para tomar esta aproximación. Primero, aprendí sobre las excepciones en Modula-3, donde las mismas son señales únicas. Segundo, introduje las excepciones antes de introducir las clases definidas por los usuarios.



En teoría, supongo que podría haber creado un nuevo tipo de objeto a medida para ser utilizado en excepciones, pero como todo tipo de objeto a medida requiere un considerable esfuerzo de codificación en C, decidí reutilizar un tipo a medida existente. Y, ya que las excepciones están relacionadas con mensajes de error, pareció natural usar strings para representar excepciones.



Lamentablemente elegí una semántica donde diferentes objetos string podían representar diferentes excepciones, aún cuando tenían el mismo valor (es decir, contenían la misma secuencia de caracteres). Elegí esta semántica porque quería que las excepciones definidas en distintos módulos sean independientes, incluso si sucedía que tenían el mismo valor. La idea era que las excepciones siempre debían ser referenciadas por su nombre, lo que implicaría identidad del objeto, nunca por su valor, lo que requeriría string iguales.



Este enfoque fue influenciado por las excepciones de Modula-3, donde cada declaración de excepción crea una única “señal de excepción” que no puede ser confundida con cualquier otra. Creo que también quería optimizar el testeo de excepciones usando punteros de comparación en vez de valores de strings en un equivocado intento de optimización prematura del tiempo de ejecución (un caso inusual – ¡yo generalmente optimizaba mi propio tiempo de codificación!). La principal razón, sin embargo, es que me preocupaban los conflictos de nombres entre excepciones no relacionadas definidas en diferentes módulos. Intenté usar patrones para adherirme estrictamente a la convención de definir una excepción como una constante global en algunos módulos, y, entonces, usarla por nombre en todo, lanzamiento o captura (esto fue mucho tiempo antes de que ciertos string literales fueran automáticamente “internos”).



¡Ay de mí!, en la práctica las cosas nunca resultan como se espera. Pronto los usuarios de Python descubrieron que dentro del mismo módulo, el compilador byte code unificaba los strings literales (es decir, creaba un sólo objeto compartido para todas las ocurrencias de strings literales con el mismo valor). Así, por accidente, los usuarios encontraron que las excepciones podían ser capturadas especificando el nombre de la excepción o el string literal conteniendo el mensaje de error. Bien, al menos esto parecía trabajar la mayor parte del tiempo. En realidad, esto sólo trabajó para el código definido en el mismo módulo. Si uno intentaba capturar excepciones usando el mensaje de error de la excepción en un módulo diferente, el código se rompía misteriosamente. Es innecesario decir que este es el tipo de cosas que causa una gran confusión.



En 1997, con Python 1.5, introduje clases para excepciones dentro del lenguaje. Aunque este ha sido el enfoque recomendado desde entonces, las excepciones de strings todavía eran soportadas para el uso en determinadas aplicaciones heredadas hasta Python 2.5. Estas fueron eliminadas en Pyton 2.6.

<em>Traducido por César Portela.

Revisado por Juan José Conti.

Si encontrás errores en esta traducción, por favor reportalos en un comentario y los corregiremos a la brevedad.</em>

Todas las traducciones de esta serie pueden encontrarse en <a href="/categoria/aprendiendo-python/historia/" target="_self">La historia de Python</a>.</body></html>