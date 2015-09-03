<html><body><img class="size-thumbnail wp-image-1362 alignright" title="wordpress-logo" src="/wp-content/uploads/2009/03/wordpress-logo-150x150.png" alt="" width="150" height="150"><em>El siguiente artículo no está pensado para ser leído por informáticos sino por no-informáticos. De todas formas, se agradece la lectura por parte de informáticos y sus comentarios para mejorarlo. El texto es una adaptación de un correo electrónico que le envié a un amigo luego de solucionar un problema que tenía con su blog alojado en <a href="http://www.wordpress.com" target="_blank">wordpress.com</a>.</em>



<!--more-->



Suele pasar, y esto lo se de leer tantas veces consultas en foros especializados, que sin aparente causa algunos blogs hechos con WordPress de repente se ven mal: la disposición (layout) de los elementos se rompe, cambia el color de fondo, la barra lateral aparece abajo de todo. ¿Cuál es la razón? Este "efecto indeseable" puede ser provocado de distintas maneras, pero una suele ser la causa en la mayoría de los casos: un error al crear entradas (o posts) para el sitio. Otro dato a tener en cuenta es que el error se suele manifestar cuando se utiliza la etiqueta especial 'more' (seguir leyendo).



En forma particular el problema se suele dar cuando el código HTML que conforma una entrada no es correcto; hay etiquetas (o 'tags') que abren pero no cierra o que están mal anidados. Se dice que un tag "abre" cuando es de la forma &lt;NOMBRE&gt; y "cierra" cuando es de la forma &lt;/NOMBRE&gt;. Lo que está en el medio de esas marcas es su contenido.



&lt;NOMBRE&gt;Contenido&lt;/NOMBRE&gt;



Estas etiquetas se utilizan para definir todo lo que se ve (y no se ve) en una página web. Un ejemplo sencillo: la etiqueta 'b' sirve para mostrar un texto (el contenido) en negrita (o bold). &lt;b&gt;esto aparece en negrita&lt;/b&gt; es mostrado por un navegador así: <strong>esto aparece en negrita</strong>. De la misma forma existen etiquetas para mostrar texto en itálica, poner colores, insertar imágenes y muchísimas cosas más.



Si te interesa aprender HTML podés leer <a href="http://www.w3schools.com/html/DEFAULT.asp" target="_blank">este tutorial</a>. Seguimos.



El siguiente es un ejemplo de tags mal anidados:



&lt;div&gt;

texto

&lt;p&gt;

texto

&lt;/div&gt;

texto

&lt;/p&gt;



En uno de los posts del sitio que revisé había un párrafo de esta forma:



&lt;div&gt;

palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras palabras

&lt;/p&gt;



Se abría un tag 'div' y se cerraba uno 'p'. Este error era el que causaba el problema en este sitio en particular. Fue solucionado cambiando &lt;div&gt; por &lt;p&gt;. Puede ocurrir que el error no sea tan trivial, pero en la mayoría de los casos será de la misma familia, aunque esté más oculto.



La siguiente lista enumera 3 reglas para tener en cuenta como forma de prevensión de estos errores.



<strong>Reglas prácticas para no tener problemas al publicar en WordPress:</strong>



1) Antes de publicar, pasar de la vista Visual a la vista HTML y ver que no haya problemas como el que describí arriba con las etiquetas.



2) Insertar la etiqueta 'more' la vista HTML para asegurarse de que no sea insertada dentro de otras etiquetas:



&lt;div&gt;

texto

&lt;!--more--&gt;

&lt;/div&gt;



está mal.



&lt;div&gt;

texto

&lt;/div&gt;

&lt;!--more--&gt;



está bien.



3) Es una fuente de errores de este estilo copiar y pegar texto desde otras páginas web o documentos de Word (ya que traen atachadas muchas etiquetas de formato). Una práctica para estar seguros de que no traemos de esas marcas es pasar el texto por el bloc de notas antes de pegarlo en el editor de WordPress. Luego en el editor mismo podemos darle formato (negrita, itálica, etc...)</body></html>