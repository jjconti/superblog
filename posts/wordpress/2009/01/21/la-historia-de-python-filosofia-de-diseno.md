<html><body><em>El siguiente texto es una traducción del artículo Python's Design Philosophy de Guido van Rossum publicado en <a href="http://python-history.blogspot.com/" target="_blank">http://python-history.blogspot.com/</a>. </em><!--more-->

<h2>Filosofía de Diseño de Python</h2>

Los próximos artículos se sumergirán en los detalles internos de la historia de Python. Sin embargo, antes de hacer eso, me gustaría detallar las guías filosóficas que me ayudaron a tomar decisiones mientras diseñaba e implementaba Python.



Ante todo, Python fue originalmente concebido como un proyecto de una sola persona; no había presupuesto oficial, y quería resultados rápidos, en parte para poder convencer a los gerentes de apoyar el proyecto (en el que estaba teniendo bastante éxito). Esto llevó a un número de reglas para ahorrar tiempo:

<ul>

	<li>Tomar ideas prestadas de otros lugares siempre que tuviera sentido.</li>

	<li>"Las cosas deben ser tan simples como sea posible, pero no más simples." (Einstein)</li>

	<li>Haz una cosa bien (la "filosofía de Unix").</li>

	<li>No preocuparse mucho sobre la performance; planea optimizar luego, cuando sea necesario.</li>

	<li>No pelear con el entorno y seguir la corriente.</li>

	<li>No intentar la perfección porque "suficientemente bueno" es a menudo eso.</li>

	<li>(Corolario) Está bien tomar atajos a veces, especialmente si se puede hacer bien luego.</li>

</ul>

Otros principios no fueron pensados para ahorrar tiempo. A veces era justamente lo contrario:

<ul>

	<li>La implementación de Python no debe estar atada a una plataforma en particular. Está bien si algunas funcionalidades no están siempre disponibles, pero el núcleo debe correr en todo lugar.</li>

	<li>No molestar a los usuarios con detalles de los que la máquina se puede encargar (no siempre seguí esta regla y algunas de las desastrosas consecuencias se describen en las siguientes secciones).</li>

	<li>Soportar y animar a que el código de los usuarios sea independiente de la plataforma, pero no evitar el acceso a las capacidades o propiedades de la plataforma (esto contrasta bruscamente con Java).</li>

	<li>Un sistema complejo y grande debe poderse extender en muchos niveles. Esto maximiza las oportunidades para los usuarios, sofisticados o no, de ayudarse a sí mismos.</li>

	<li>Los errores no deben ser fatales. Esto significa que el código de los usuarios debe ser capaz de recuperarse de condiciones de error mientras que la máquina virtual siga funcionando.</li>

	<li>Al mismo tiempo, los errores no deben pasar inadvertidos (estos dos últimos ítems llevan naturalmente a la decisión de usar excepciones en la implementación).</li>

	<li>No se debe permitir que un error en el código Python del usuario lleve al intérprete de Python a un comportamiento no definido; un fallo de segmento (core dump) no es nunca culpa del usuario.</li>

</ul>

Finalmente, tengo varias ideas sobre el diseño de buenos lenguajes de programación, que el grupo de desarrollo de ABC marcó en mí; en él tuve mi primera experiencia real con el diseño e implementación de lenguajes. Estas ideas son las más difíciles de poner en palabras, ya que la mayoría giran en torno a conceptos subjetivos como elegancia, simplicidad y legibilidad.



A pesar de que más adelante voy a tratar más sobre la influencia de ABC en Python, me gustaría mencionar especialmente una regla de legibilidad: los caracteres de puntuación deben ser usados en forma conservadora, de forma alineada con el uso que se les da en Inglés o álgebra universitaria. Se hacen excepciones cuando una notación particular es una tradición antigua en los lenguajes de programación, como "x*y" para multiplicar, "a[i]" para acceder al elemento de un array o "x.foo" para seleccionar un atributo, pero Python no usa "$" para indicar variables, ni "!" para indicar operaciones con efectos secundarios.



Tim Peters, un antiguo usuario de Python quien eventualmente se convirtió en su más prolífero y tenaz desarrollador del núcleo, intentó capturar mis principios de diseño tácitos en lo que llamó el "<a href="http://www.python.org/dev/peps/pep-0020/" target="_blank">Zen de Python</a>". Lo cito aquí enteramente:

<ul>

	<li>Hermoso es mejor que feo.</li>

	<li>Explícito es mejor que implícito.</li>

	<li>Simple es mejor que complejo.</li>

	<li>Complejo es mejor que complicado.</li>

	<li>Plano es mejor que anidado.</li>

	<li>Ralo es mejor que denso.</li>

	<li>La legibilidad importa.</li>

	<li>Los casos especiales no son tan especiales como para romper las reglas.</li>

	<li>Aunque lo práctico vence a lo puritano.</li>

	<li>Los errores nunca deben pasar desapercibidos.</li>

	<li>A menos que sean explícitamente silenciados.</li>

	<li>Ante la ambigüedad, rechaza la tentación de adivinar.</li>

	<li>Debe haber una forma (y preferentemente sólo una forma) obvia de hacerlo.</li>

	<li>Aunque esa forma no sea obvia al principio a menos que seas Holandés.</li>

	<li>Ahora es mejor que nunca.</li>

	<li>Aunque nunca es a menudo mejor que ya.</li>

	<li>Si la implementación es difícil de explicar, es una mala idea.</li>

	<li>Si la implementación es fácil de explicar, puede ser una buena idea.</li>

	<li>Los espacios de nombre son geniales; hagamos más de ellos!</li>

</ul>

A pesar de que mi experiencia en el grupo de desarrollo de ABC influenció en gran medida a Python, tenían algunos principios de diseño que eran radicalmente diferentes a los de Python. De muchas maneras, Python nace deliberadamente de estos:

<ul>

	<li>El grupo de desarrollo de ABC se esforzaba en alcanzar la perfección. Por ejemplo, usaban algoritmos de estructuras de datos arbóreas que se había probado eran óptimos para casi infinitas colecciones (pero no eran tan geniales para colecciones pequeñas).</li>

	<li>Querían aislar al usuario, tanto como sea posible, del "enorme y malvado mundo de las computadoras" que había ahí afuera. No solo no debía haber un límite en el rango de números, el largo de las cadenas de texto, o el tamaño de las colecciones (aparte del total de memoria disponible), sino que los usuarios tampoco tendrían que ocuparse de discos, otros programas o guardar archivos. ABC debía ser la única herramienta que podrían necesitar. Este deseo también causó que el grupo de desarrollo de ABC cree un entorno de edición totalmente integrado, único para ABC (por supuesto, había una posibilidad de escapar del entorno de ABC, pero fue una idea de último momento y no era accesible directamente desde el lenguaje).</li>

	<li>Asumieron que los usuarios no tendrían experiencia previa con computadoras (o estarían deseando olvidarla). Así, se introdujo terminología alternativa considerada más amigable para los novatos que términos estándares de programación. Por ejemplo, los procedimientos se llamaban "how-tos" y las variables "locations".</li>

	<li>El grupo de desarrollo de ABC diseñó ABC sin un camino evolutivo en mente y sin esperar la participación de  los usuarios en el diseño del lenguaje. ABC fue creado como un sistema cerrado, tan impecable como sus diseñadores podían hacerlo. No se alentaba a los usuarios a mirar que pasaba dentro. Aunque se habló sobre abrir partes de la implementación a usuarios avanzados durante las últimas etapas del proyecto, esto nunca se concretó.</li>

</ul>

En muchas formas, la filosofía de diseño que usé cuando diseñaba Python es probablemente una de las principales razones de su éxito final. En lugar de intentar alcanzar la perfección, los primeros usuarios vieron que Python funcionaba "suficientemente bien" para sus propósitos. Al crecer la base de usuarios, se incorporaron gradualmente sugerencias para mejorar el lenguaje. Como veremos en las futuras secciones, muchas de estas mejoras necesitaron cambios sustanciales y la reimplementación del núcleo del lenguaje. Incluso hoy, Python continua evolucionando.



<em>Traducido por Juan José Conti.

Revisado por César Portela.

Si encontrás errores en esta traducción, por favor reportalos en un comentario y los corregiremos a la brevedad.</em>

Todas las traducciones de esta serie pueden encontrarse en <a href="/categoria/aprendiendo-python/historia/" target="_self">La historia de Python</a>.</body></html>