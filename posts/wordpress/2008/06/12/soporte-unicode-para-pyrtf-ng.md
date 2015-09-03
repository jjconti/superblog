<html><body><p><a href="http://code.google.com/p/pyrtf-ng" title="code" target="_blank">pyrtf-ng</a> es un módulo para Python que permite generar archivos en formato <a href="http://en.wikipedia.org/wiki/Rich_Text_Format" title="RTF" target="_blank">RTF</a> en forma dinámica. Esta semana empecé a probarlo con la idea de usarlo para generar documentos de texto con formato (<a href="http://es.wikipedia.org/wiki/DOC" title=".doc?" target="_blank">Word</a>-like) en forma dinámica.

</p><p>

Al intentar instalarlo tuve algunos problemas , se los comenté al autor y le sugerí soluciones. Rápidamente estas modificaciones estuvieron hechas en el repositorio del proyecto.

</p><p>

Una vez que tuve la librería instalada y los ejemplos corriendo, empecé a modificar algunos para experimentar un poco. Cuando quise generar un documento que contenga una palabra con tilde (cómo <code>canción</code>), el programa tiró una horrible excepción. Esto hacía que desechara totalmente la idea de usar este software.

</p><p>

Leí sobre la codificación utilizada por el formato RTF y descubrí que <a href="http://en.wikipedia.org/wiki/Rich_Text_Format#Character_encoding" title="RTF Encoding" target="_blank">no soporta Unicode</a> en forma nativa, pero si mediante una secuencia de escape de la forma: <code>\uxxxx?</code> en dónde <code>xxxx</code> es un entero con signo de 16 bits correspondiente al caracter que se quiere representar. Ejemplo: <a href="http://www.fileformat.info/info/unicode/char/00e1/index.htm" title="LATIN SMALL LETTER A WITH ACUTE" target="_blank">á</a>.

</p><p>

Pedí instrucciones al autor de la librería, quien me indicó que partes del código tendría que revisar par incluir la funcionalidad de soportar Unicode. Luego de algunas horas empapándome en la arquitectura de clases de pyrtf, tenía un parche listo para ser aplicado e incorporar la funcionalidad. Hoy <a href="http://code.google.com/p/pyrtf-ng/source/detail?r=69" title="Parche para Unicode" target="_blank">fue incluido</a> en la versión en desarrollo de la librería.</p>

<h2>Código</h2>

Un pequeño snippet que muestra el algoritmo básico para pasar de un string Unicode a su representación codificada en RTF:



<code>encoded = ''.join(['\u%s?' % str(ord(b)) for b in base])</code>

<h2>Datos</h2>

<ul>

	<li>pyrtf-ng es mantenido por <a href="http://oubiwann.blogspot.com/" title="Duncan's blog" target="_blank">Duncan Mc Greggor</a> y está basado en <a href="http://pyrtf.sourceforge.net/" title="PyRTF" target="_blank">PyRTF,</a> un proyecto que ya no es mantenido.</li>

	<li>Se encuentra en activo desarrollo: modificación del <a href="http://www.python.org/dev/peps/pep-0008/" title="PEP8" target="_blank">estilo</a> del código y <em>refactoring</em>.</li>

	<li>También puede ser modificado mediante bazaar en <a href="https://launchpad.net/pyrtf" title="Launchpad" target="_blank">lauchpad</a>.</li>

</ul></body></html>