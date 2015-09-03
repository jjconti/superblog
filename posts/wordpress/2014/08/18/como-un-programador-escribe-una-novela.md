<html><body><p>La semana pasada <a href="http://www.colectivolibre.com.ar/" target="_blank">Colectivo Libre</a> organizó una conferencia (llamada <a href="http://crsl.colectivolibre.com.ar/" target="_blank">Conferencia de Software Libre del Litoral</a>) y me invitaron a hablar sobre cultura libre o crowdfunding o Creative Commons. En particular, que cuente mi experiencia.



Di una charla llamada <strong>Cómo un programador escribe una novela: crowdfunding, herramientas y licencias</strong> en la que conté mis peripecias financiando la impresión de mis libros (como ese camino fue evolucionando), hablé de las herramientas que desarrollé para imprimir Xolopes y cerré explicando brevemente las distintas licencias Creative Commons disponibles.



La presentación la armé con <a href="http://slides.com/" target="_blank">slides.com</a>, un sitio que utiliza la librería <a href="http://lab.hakim.se/reveal-js/" target="_blank">reveal.js</a>: <a href="http://slides.com/juanjoconti/como-un-programador-escribe-una-novela#/" target="_blank">http://slides.com/juanjoconti/como-un-programador-escribe-una-novela#/</a>

</p><center>

<iframe src="//slides.com/juanjoconti/como-un-programador-escribe-una-novela/embed" width="576" height="420" scrolling="no" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

</center>

<a href="/wp-content/uploads/2014/08/IMG_2037.jpg">

<img class="aligncenter size-large wp-image-4966" src="/wp-content/uploads/2014/08/IMG_2037-1024x768.jpg" alt="Cómo un programador escribe una novela" width="640" height="480"></a>

(<a href="https://www.facebook.com/juanjoconti/media_set?set=a.10204341456327390.1073741847.1559082191&amp;type=3" target="_blank">más fotos</a>)



Luego de la presentación hubieron muchos comentarios y preguntas. Estuvo muy bueno. <strong>¿Te al perdiste? Probablemente vuelta a darla en la Feria del Libro de Santa Fe el sábado 13 de septiembre a las 18 hs</strong>.



Lamentablemente no fue grabada y las <em>slides</em> dicen poco por si solas. Sin embargo, acabo de recuperar el borrador de un post que nunca publiqué. Su contenido coincide con un tercio de la charla, aunque tiene mucho más detalle técnico del que expuse en la conferencia:

<h2>Cómo escribí Xolopes</h2>

Este artículo habla sobre la novela corta <a href="http://www.juanjoconti.com.ar/libros/xolopes/" target="_blank">Xolopes</a>.



Durante mis últimas <a href="http://www.juanjoconti.com.ar/2013/07/12/algunas-fotos-de-las-vacaciones-en-mexico/">vacaciones</a> estuve tomando notas rápidas en el celular. Ideas, conversaciones, principios, finales. Al mismo tiempo estuve <a href="http://www.juanjoconti.com.ar/2013/07/12/camaragesell-guillermo-saccomanno/">leyendo</a> una novela cuya estructura me gustó mucho y quise imitar. Quise hacer un <a title="La canción que cada uno tiene adentro - Leonardo Oyola" href="http://www.youtube.com/watch?v=DC-OdcjzED0" target="_blank"><em>cover</em></a>.

<blockquote>—¿Y qué escribís? —se interesa el marido de la señora.

—Cuentos.

—Ah... hay que tener imaginación para eso.

—No tanta, me la paso recogiendo voces de otros.



Xolopes #46</blockquote>

La novela sería entonces una sucesión de textos, en su mayoría cortos, con un orden propio. El problema era que no conocía ese orden, que nuevas partes irían surgiendo y que otras serían eliminadas. Escribir todo en un único documento, "un Word", no parecía una elección correcta. Como me gusta programar, la solución a mi problema sería un programa.

<blockquote>... en lugar de ser una sucesión de pocos capítulos largos, se forma con una multiplicidad de textos cortos, uno a continuación del otro, una multitud de voces que van ingresando al texto para formarlo.



Xolopes #122</blockquote>

Pasé cada una de las partes que tenía hasta el momento a archivos de texto. Uno por cada parte. En otro archivo (índice) escribí un orden tentativo para las partes. Finalmente, escribí un <a title="El lenguaje de programación Python" href="http://www.python.org/" target="_blank">script en Python</a> (que se fue refinando y extendiendo) capás de leer índice y armar un documento <a href="http://es.wikipedia.org/wiki/LaTeX" target="_blank">Latex</a> con las partes y el orden especificado. Ese documento Latex puede compilarse a pdf, generando el archivo que voy a enviar a la imprenta.



Con el correr de los meses fui escribiendo el resto de las partes. Algunas historias son recuerdos de otros viajes, otras son el resultado de ejercicios en el taller, otras, anécdotas prestadas y otras, totales inventos. Mientras lo hacía, iba probando distintos ordenes hasta encontrar EL ORDEN definitivo que tendría la obra, ese que tenía desde antes de ser escrita pero que aún no conocía.



<strong>Control de cambios</strong>



Me resulta entretenido participar de todo el proceso de la concepción de un libro. Desde tipear sus palabras hasta imprimirlo y voy refinando e incrementando mi participación en todo el proceso lo más que puedo. En este experimento, a diferencia de los dos anteriores (1 y 2), intento



<strong>Además de escribir la novela usando un programa escrito especialmente para escribirla, la misma fue escrita de forma similar a la que se escribe un programa.</strong> Utilicé un sistema de control de versiones para llevar registro de cada uno de los cambios que iba haciendo.



Ejemplo: <a href="https://github.com/jjconti/novela-workflow/commit/47805ecaf6d873363f10220b27113ef53b6f1855#diff-b1d745729a42a8029705f6c847066918" target="_blank">https://github.com/jjconti/novela-workflow/commit/47805ecaf6d873363f10220b27113ef53b6f1855#diff-b1d745729a42a8029705f6c847066918</a>



<strong>Herramientas</strong>



Otras herramientas fueron escritas a la vez que se escribía la novela pero no quiero irme en detalles. Temo aburrir con muchos tecnicismos a los lectores, autores, editores que lean este post. También temo aburrir con muchas palabras a los hackers, programadores y geeks que lean este post. Por lo tanto voy a cerrarlo ahora mismo :)



Este es el set de herramientas propias y archivos utilizado para generar el pdf de la novela al momento de escribir este post. A los ojos de un programador, son herramientas simples que uno puede hacerse en un su casa. Pero tal vez les sean interesantes a autores o editores:

<ul>

	<li><a href="https://github.com/jjconti/novela-workflow/blob/blogpost/xolopes/format.sh" target="_blank">format.sh</a> (evita tener archivos muy "anchos" limitando el número de columnas)</li>

	<li><a href="https://github.com/jjconti/novela-workflow/blob/blogpost/xolopes/xolopesBase.tex" target="_blank">xolopesBase.tex</a> (template del documento Latex utilizado)</li>

	<li><a href="https://github.com/jjconti/novela-workflow/blob/blogpost/xolopes/regenerateIndex.py">regenerateIndex.py</a> (le agrega al <a href="https://github.com/jjconti/novela-workflow/blob/blogpost/xolopes/xolopes.index" target="_blank">índice</a> las primeras palabras de cada archivo para tener contexto y ayudarme a no perderme entre los nombres de archivos)</li>

	<li><a href="https://github.com/jjconti/novela-workflow/blob/blogpost/xolopes/xolopes.sh" target="_blank">xolopes.sh</a> (programa maestro, llama a xolopes.py y compila los documentos Latex a pdf)</li>

	<li><a href="https://github.com/jjconti/novela-workflow/blob/blogpost/xolopes/xolopes.py" target="_blank">xolopes.py</a> (genera el documento Latex en base a las partes y al índice, en dos versiones, con imágenes y sin imágenes)</li>

	<li><a href="https://github.com/jjconti/novela-workflow/blob/blogpost/xolopes/getDot.py" target="_blank">getDot.py</a> (genera el archivo .dot que representa el mapa de la novela)</li>

	<li><a href="https://github.com/jjconti/novela-workflow/blob/blogpost/xolopes/map.sh" target="_blank">map.sh</a> (en base al arcihvo .dot que representa el <a href="http://www.juanjoconti.com.ar/2014/01/05/el-mapa-de-xolopes/">mapa</a> de la novela genera el mapa en distintos formatos)</li>

</ul></body></html>