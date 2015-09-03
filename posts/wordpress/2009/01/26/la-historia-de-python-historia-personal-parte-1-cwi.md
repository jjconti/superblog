<html><body><em>El siguiente texto es una traducción del artículo Personal History - part 1, CWI de Guido van Rossum publicado en <a href="http://python-history.blogspot.com/" target="_blank">http://python-history.blogspot.com/</a>.</em><!--more-->

<h2>Historia personal - parte 1, CWI</h2>

El desarrollo de Python empezó en un instituto de investigación en Amsterdam llamado <a href="http://www.cwi.nl/" target="_blank">CWI</a>, el cual es un acrónimo en holandés que en español significa Centro de Matemáticas y Ciencias de la computación. CWI es un lugar interesante; fundado por el Departamento de Educación del gobierno y otros fondos para investigación, guía investigaciones de nivel académico en ciencias de la computación y matemáticas. En todo momento está lleno de estudiantes de doctorado paseando y los más viejos profesionales deben aún recordar su nombre original, el Centro Matemático. Bajo este nombre, es tal vez más famoso por la invención de <a href="http://en.wikipedia.org/wiki/ALGOL_68" target="_blank">Algol 68</a>.



Empecé a trabajar en CWI al final de 1982, recién salido de la universidad, como programador en el grupo de desarrollo de <a href="http://en.wikipedia.org/wiki/ABC_%28programming_language%29" target="_blank">ABC</a> liderado por <a href="http://en.wikipedia.org/wiki/Lambert_Meertens">Lambert Meertens</a> y <a href="http://en.wikipedia.org/wiki/Steven_Pemberton" target="_blank">Steven Pemberton</a>. Luego de 4 o 5 años, el proyecto ABC fue interrumpido debido a la obvia falta de éxito y me trasladé al grupo <a href="http://en.wikipedia.org/wiki/Amoeba_distributed_operating_system" target="_blank">Amoeba</a> liderado por Sape Mullender. Amoeba era un sistema operativo distribuido basado en micro-kernel desarrollado en forma conjunta por CWI y la <a href="http://en.wikipedia.org/wiki/Vrije_Universiteit" target="_blank">Vrije Universiteit of Amsterdam</a>, bajo la dirección de <a href="http://en.wikipedia.org/wiki/Andrew_S._Tanenbaum" target="_blank">Andrew Tanenbaum</a>. En 1991, Sape dejó CWI para dar clases en la <a href="http://en.wikipedia.org/wiki/University_of_Twente" target="_blank">University of Twente</a> y terminé en otro grupo recientemente formado en CWI sobre multimedia liderado por <a href="http://homepages.cwi.nl/%7Edcab/" target="_blank">Dick Bulterman</a>.



Python es un producto directo de mi experiencia en CWI. Como explico más adelante, ABC me dio la inspiración clave para Python, Amoeba la motivación inmediata, y el grupo multimedia fomentó su crecimiento. Sin embargo, hasta donde sé, ningún fondo de CWI fue alguna vez destinado oficialmente para su desarrollo. En cambio, sólo evolucionó como una herramienta importante para usar en los grupos Amoeba y de multimedia.



Mi motivación original pare crear Python fue la necesidad que percibí por un lenguaje de alto nivel en el proyecto Amoeba. Me dí cuenta de que el desarrollo de utilidades para administración de sistemas en C llevaría mucho tiempo. Más aún, hacer esto en el shell Bourne funcionaría por una variedad de razones. La más importante fue que al ser Amoeba un sistema micro-kernel distribuido con un diseño radicalmente nuevo, sus operaciones primitivas eran diferentes (y de granularidad fina) de las primitivas tradicionales disponibles en el shell Bourne. Existía la necesidad de un nuevo lenguaje que "una la brecha entre C y el shell". Por mucho tiempo, este fue el principal slogan de Python.



En este punto tal vez se pregunte "¿por qué no portar un lenguaje existente?". En mi forma de verlo, no había muchos lenguajes apropiados en esos días. Estaba familiarizado con Perl 3, pero estaba más atado a Unix que el shell Bourne. Tampoco me gustaba la sintaxis de Perl --mi gusto en la sintaxis de los lenguajes de programación fue fuertemente influenciado por lenguajes como <a href="http://en.wikipedia.org/wiki/ALGOL" target="_blank">Algol 60</a>, Pascal, Algol 68 (a todos los había aprendido mucho antes) y, por último pero no el peor, ABC, en el cual gasté cuatro años de mi vida. Así que decidí diseñar un lenguaje por mi cuenta que tomaría prestado todo lo que me gustaba de ABC a la vez que arreglaba todos sus problemas (como los percibía).



¡El primer problema que decidí arreglar era el nombre! Sucedió que el equipo de desarrollo de ABC tenía algunos problemas en elegir un nombre para su lenguaje. El nombre original del lenguaje, <em>B</em>, tuvo que ser abandonado porque se confundía con otro lenguaje llamado B, que era más viejo y más conocido. De cualquier modo, <em>B</em> era solo un título de trabajo (el chiste era que <em>B</em> era el nombre de la variable que contenía el nombre del lenguaje, de ahí la itálica). El equipo tuvo un concurso público para obtener un nuevo nombre, pero ninguna de las propuestas fue apropiada, y al final el backup interno prevaleció. Con el nombre se quería expresar la idea de que el lenguaje hacía que la programación sea "tan simple como el ABC", pero a mi nunca me convenció mucho.



Así que, en lugar de sobre analizar el problema del nombre, decidí hacer lo contrario. Elegí el primer nombre que me vino a la mente, que resultó ser <a href="http://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus" target="_blank">Monty Python’s Flying Circus</a>, uno de mis grupos cómicos preferidos. La referencia parece bastante irrelevante para lo que era esencialmente un proyecto innovador pero solitario. La palabra "Python" era pegadiza, te ponía un poco los pelos de punta, y al mismo tiempo encajaba en la tradición de ponerle a los lenguajes nombres de personas famosas, como Pascal, Ada y Eiffel. Puede que el equipo de The Monty Python no sea famoso por sus avances en ciencia o tecnología, pero son ciertamente un favorito de los geeks. También encajaba en la tradición del grupo Amoeba de CWI de ponerle a los programas el nombre de shows televisivos.



Por muchos años resistí la tentación de asociar el lenguaje con serpientes. Finalmente me rendí cuando O'Reilly quizo poner una serpiente en la tapa del primer libro de Python "Programming Python". Era una tradición de O'Reilly usar fotos de animales, y si tenía que ser un animal, que sea una serpiente.



Con el asunto del nombre resuelto, empecé a trabajar en Python a finales de diciembre de 1989, y tuve una versión funcionando en los primeros meses de 1990. No tomé notas, pero recuerdo vivamente que la primer pieza de código que escribí de la implementación de Python era un <em>LL(1) parser generator</em> simple que llamé "pgen". Este parser generator es aún parte de los fuentes de Python y probablemente lo menos cambiado de todo el código. Esta versión temprana de Python fue usada por algunas personas en CWI, mayormente, pero no en forma exclusiva en el grupo Amoeba durante 1990. Los desarrolladores clave, demás de mi, eran mis compañeros de oficina, los programadores  <a href="http://homepages.cwi.nl/%7Esjoerd/" target="_blank">Sjoerd Mullender</a> (el hermano menor de Sape) y <a href="http://homepages.cwi.nl/%7Ejack/" target="_blank">Jack Jansen</a> (quien fue uno de los desarrolladores líderes de la versión para Macintosh por muchos años, luego de dejar CWI).



El 20 de febrero de 1991 publiqué por primera vez Python para el mundo en el grupo de noticias <a href="http://www.faqs.org/faqs/alt-sources-intro/" target="_blank">alt.sources</a> (como 21 partes <a href="http://en.wikipedia.org/wiki/Uuencode" target="_blank">codificadas</a> que tenían que ser juntadas y decodificadas para formar el archivo tar comprimido). Esta versión fue etiquetada 0.9.0 y publicada bajo una licencia que era prácticamente una copia textual de la licencia MIT usada por el proyecto X11 en ese entonces, poniendo “Stichting Mathematisch Centrum”, la organización padre de CWI, como la entidad responsable legal. Así que, como casi todo lo que he escrito, Python era open source antes de que el término sea inventado por <a href="http://en.wikipedia.org/wiki/Eric_S._Raymond">Eric Raymond</a> y <a href="http://en.wikipedia.org/wiki/Bruce_Perens" target="_blank">Bruce Perens</a> a finales de 1997.



Enseguida hubo mucha retroalimentación y con este apoyo mantuve un firme flujo de publicaciones durante algunos años. Empecé a usar <a href="http://en.wikipedia.org/wiki/Concurrent_Versions_System" target="_blank">CVS</a> para seguir los cambios y para facilitar compartir la responsabilidad de codificar con Sjoerd y Jack (coincidentemente, CVS fue desarrollado originalmente como un set de shell scripts por <a href="http://en.wikipedia.org/wiki/Dick_Grune" target="_blank">Dick Grune</a>, quien era uno de los miembros originales del equipo de desarrollo de ABC). Escribí una FAQ, que era regularmente publicada en algunos grupos de noticias, como era costumbre para las FAQs en aquellos días anteriores a la web. Empecé una lista de correos, en marzo de 1993 se creó el grupo de noticias <a href="http://groups.google.com/group/comp.lang.python/topics" target="_blank">comp.lang.python</a> con mi apoyo pero sin estar directamente involucrado. El grupo de noticias y la lista de correos fueron unidos mediante un gateway bidireccional que aún existe, aunque hoy está implementado con mailman (el gestor de listas de correos líder, escrito en Python).



En el veranode 1994, en el grupo de noticias apareció un hilo titulado "<a href="http://www.python.org/search/hypermail/python-1994q2/1040.html" target="_blank">¿si a Guido lo atropella un colectivo?</a>" sobre la dependencia de la creciente comunidad de Python en mis contribuciones personales. Culminó con una invitación que me hizo Michael McLay para pasar dos meses como investigador invitado en el <a href="http://www.nist.gov/" target="_blank">NIST</a>, el Instituto Nacional de Estándares y Tecnologías de los Estados Unidos, antes el <em>Bureau</em> Nacional de Estándares, en Gaithersburg, Maryland. Michael tenía varios "clientes" del NIST interesados en usar Python para una variedad de proyectos relacionados con estándares y el presupuesto para mi estancia allí nació de la necesidad de ayudarlos a mejorar sus habilidades con Python, así como posiblemente adaptar Python a sus necesidades.



El primer workshop de Python se llevó a cabo mientras estuve allí en noviembre de 1994, con el programador del NIST, <a href="http://en.wikipedia.org/wiki/Ken_Manheimer" target="_blank">Ken Manheimer</a>, dándome un importante apoyo. De los aproximadamente 20 asistentes, alrededor de la mitad son aún participantes activos de la comunidad de Python y algunos se volvieron líderes principales de proyectos open sources (<a href="http://www.zope.com/about_us/management/james_fulton.html" target="_blank">Jim Fulton</a> de <a href="http://www.zope.org/" target="_blank">Zope</a> y <a href="http://barry.warsaw.us/" target="_blank">Barry Warsaw</a> de <a href="http://en.wikipedia.org/wiki/GNU_Mailman" target="_blank">GNU mailman</a>). Con el apoyo del NIST también di una charla para 400 personas en la conferencia Usenix Little Languages en Santa Fe, organizada por <a href="http://en.wikipedia.org/wiki/Tom_Christiansen" target="_blank">Tom Christiansen</a>, un defensor de Perl de mente abierta quien me presentó al creador de Perl, <a href="http://en.wikipedia.org/wiki/Larry_Wall" target="_blank">Larry Wall</a>, y al author de Tcl/Tk, <a href="http://home.pacbell.net/ouster/" target="_blank">John Ousterhout</a>.



En la próxima entrega: cómo conseguí un trabajo en los Estados Unidos...

<em>Traducido por Juan José Conti.

Revisado por César Portela.

Si encontrás errores en esta traducción, por favor reportalos en un comentario y los corregiremos a la brevedad.</em>

Todas las traducciones de esta serie pueden encontrarse en <a href="/categoria/aprendiendo-python/historia/" target="_self">La historia de Python</a>.</body></html>