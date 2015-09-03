<html><body><em>El siguiente texto es una traducción del artículo Python's Use of Dynamic Typing de Guido van Rossum publicado en <a href="http://python-history.blogspot.com/" target="_blank">http://python-history.blogspot.com/</a>.</em>

<!--more-->

<h2>El uso de tipado dinámico en Python</h2>

Una diferencia importante entre ABC y Python es el estilo general del sistema de tipos. ABC es estáticamente tipado, lo cual significa que el compilador de ABC analiza el uso de tipos en un programa y decide si están siendo usados consistentemente. Si no, el programa es rechazado y su ejecución no puede comenzar. A diferencia de la mayoría de los lenguajes con tipado estático de esos días, ABC usaba inferencia de tipos (no distinto que Haskell) en lugar de declaraciones explícitas de tipos como en C. En contraste, Python es dinámicamente tipado. El compilador de Python ignora felizmente los tipos usados en un programa y todo el control de tipos es hecho en tiempo de ejecución.



Aunque esto pueda parecer muy distinto de ABC, no es tan diferente como uno imaginaría. A diferencia de otros lenguajes de tipado estático, ABC no depende (¿dependía? es prácticamente histórico hoy : - ) exclusivamente de controles de tipado estático para evitar que el programa termine abruptamente, también tiene una librería en tiempo de ejecución que controla los tipos de los argumentos en todas las operaciones nuevamente cada vez que son ejecutadas. Esta verificación no estaba de más para los algoritmos de control de tipos del compilador, que no estaban totalmente implementados en el primer prototipo del lenguaje. La librería en tiempo de ejecución también servía como una ayuda para la depuración, ya que el control de tipos explícito en tiempo de ejecución puede producir lindos mensajes de error (algo requerido por los implementadores), en lugar de los vuelcos de memoria que sucederían si el intérprete siguiera ciegamente con una operación sin controlar si los argumentos tienen sentido.



Sin embargo, la razón más importante por la que ABC tenía control de tipos en tiempo de ejecución, además de control de tipado estático, es su naturaleza interactiva. En una sesión interactiva, el usuario tipea sentencias de ABC y definiciones que son ejecutadas tan pronto como son completadas. En una sesión interactiva, es posible crear una variable y asignarle un número, borrarla y luego volver a crearla (en otras palabras, crear otra variable con el mismo nombre) y asignarle un string. Dentro de un solo procedimiento, sería un error de tipado estático usar el mismo nombre de variable primero como un número y luego como un string, pero no sería razonable forzar ese control entre diferentes sentencias entradas en una sesión interactiva, mientras que la creación accidental de una variable llamada x a la que se le asigna un número, !prohiba para siempre la creación de una variable x con otro tipo!. El compromiso de ABC es usar control de tipos dinámico para las variables globales, pero estático para las locales. Para simplificar la implementación, las variables locales obtienen control de tipo dinámico también.



Así, hay solo un pequeño paso desde el enfoque usado en la implementación de ABC para el control de tipos al de Python; Python simplemente deja todo el control de tipos en tiempo de compilación. Esto se alinea completamente con la filosofía de Python de "tomar atajos", ya que simplifica la implementación y no afecta la eventual seguridad, ya que todos los errores de tipo son atrapados en tiempo de ejecución antes de que causen un mal funcionamiento del intérprete de Python.



Sin embargo, una vez que te decides por el tipado dinámico no hay vuelta atrás. Las operaciones de ABC fueron cuidadosamente diseñadas para que el tipo de los argumentos pueda ser deducido de la forma de los operadores. Por ejemplo, de la expresión "x^y" el compilador deduciría que las variables x e y son strings, así como el resultado. En Python, esa deducción no se puede generalizar. Por ejemplo, la expresión "x+y" puede ser una concatenación de strings, una suma entre números, o una operación sobrecargada sobre tipos definidos por el usuarios.



<em>Traducido por Juan José Conti.

Revisado por César Portela.

Si encontrás errores en esta traducción, por favor reportalos en un comentario y los corregiremos a la brevedad.</em>

Todas las traducciones de esta serie pueden encontrarse en <a href="/categoria/aprendiendo-python/historia/" target="_self">La historia de Python</a>.</body></html>