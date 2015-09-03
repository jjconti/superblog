<html><body><em>El siguiente texto es una traducción del artículo The Great (or Grand) Renaming de Guido van Rossum publicado en <a href="http://python-history.blogspot.com/" target="_blank">http://python-history.blogspot.com/</a>.</em>

<!--more-->

<h2>El Gran (o Enorme) Renombrado</h2>

Cuando creé Python, siempre lo imagine como un programa autónomo, enlazado ocasionalmente con bibliotecas de terceros. Por lo tanto, en el código fuente, se definían nombres globales con total libertad, como "object", "getlistitem", "INCREF" y muchos otros mas. Cuando la popularidad de Python se  incrementó, la gente comenzó a pedir una versión "embebida", que fuera también una biblioteca enlazable a otras aplicaciones - de una forma similar en la que Emacs incorpora un interprete de Lisp.



Desafortunadamente, la integración se complicaba por conflictos entre  los nombres globales de Python y los definidos por la aplicación - "object" era especialmente popular. Para lidiar con ese problemas se eligió una convención, por la cual todos los nombre globales comenzarían con "Py" o "_Py" (para los internos que tenían que ser globales por razones técnicas) o "PY" (para las macros).



Por razones de compatibilidad hacia atrás (ya que había muchos módulos de extensión de terceros) y para facilitar la transición a los desarrolladores del núcleo (que tenían los viejos nombres enquistados en sus mentes) hubieron dos fases. En la fase uno, el enlazador aceptaba los nombres antiguos, pero el código fuente usaba los nuevos, que eran traducidos a los antiguos usando muchas macros del pre procesador de C. En la fase dos, el enlazador veía los nuevos, pero, para beneficio de los módulos de extensión que todavía no habían sido portados, otro conjunto de macros traducía los viejos a los nuevos. En ambas fases el código podía incluir ambos, y funcionar correctamente.



Investigué un poco la historia en los <a href="http://svn.python.org/view/python/trunk/" target="_blank">logs de Subversion</a>. Encontré la revisión <a href="http://svn.python.org/view?view=rev&amp;revision=4583" target="_blank">r4583</a> del 12 de enero de 1995, que marca el comienzo de la fase dos, introduciendo los nuevos nombres a los archivos de encabezado. Pero en diciembre de 1996 el renombrado de los archivos fuentes ".c" seguia en marcha. En ese momento el renombrado parecía haber cambiado de nombre, los comentarios de registro lo llamaban "El Enorme Renombrado". Las macros de compatibilidad hacia atras fueron finalmente removidos en mayo de 2000, como resultado de la liberación 1.6. El comentario de <a href="http://svn.python.org/view?view=rev&amp;revision=15313" target="_blank">r15313</a> celebra este evento.



La mayor parte del crédito se lo llevaron Barry Warsaw y Roger Masse, que participaron en la desagradable tarea de renombrar los contenidos de archivo, tras archivo, tras archivo... (aunque con la ayuda de un script). También ayudaron en la tediosa tarea de agregar test unitarios para gran parte de la biblioteca estándar.



Wikipedia hace referencia a un anterior Gran Renombrado, que aparentemente consistió en el renombre de grupos de USENET. Probablemente lo recordaba de forma inconsciente cuando lo llamé asi. También encontré algunas referencias a un Gran Renombrado posterior en Sphinx, el paquete utilizado para generar la documentación de Python. Zope también tuvo uno, y algunos debates recientes de Py3k utilizan el término para el cambio de PyString a PyBytes (aunque es menor, comparado con los otros).



Los Grandes o Enormes cambios de nombres son a menudo eventos traumáticos para las comunidades de desarrollo de software, porque requieren que los cerebros de los programadores sean recableados, la documentación reescrita y se complica la integración de parches creados antes, pero aplicados después (esto es especialmente problemático cuando existen ramas no renombradas).

<em>Traducido por <a href="http://www.joaclandia.com.ar/" target="_blank">Joaquín Sorianello</a>.

Revisado por Juan José Conti.

Si encontrás errores en esta traducción, por favor reportalos en un comentario y los corregiremos a la brevedad.</em>

Todas las traducciones de esta serie pueden encontrarse en <a href="/categoria/aprendiendo-python/historia/" target="_self">La historia de Python</a>.</body></html>