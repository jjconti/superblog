<html><body><p>Plasmo en el blog esta idea por que me parece importante compartirla.



Primero repacemos dos conceptos:

</p><h2>Software Libre</h2>

Cuando hablamos de <em>Software Libre</em> nos referimos a software que da a sus usuarios una suma de libertades. La libertad de ejecutar, copiar, distribuir, estudiar, cambiar y mejorar. De un modo más preciso, un software es considerado libre cuando le da a todos sus usuarios estas 4 libertades:

<ul>

	<li>La libertad de usar el programa, con cualquier propósito (libertad 0).</li>

	<li>La libertad de estudiar el funcionamiento del programa, y adaptarlo a las necesidades (libertad 1).</li>

	<li>La libertad de distribuir copias, con lo que puede ayudar a otros (libertad 2).</li>

	<li>La libertad de mejorar el programa y hacer públicas las mejoras, de modo que toda la comunidad se beneficie (libertad 3)</li>

</ul>

<h2>Software Privativo</h2>

En oposición al tipo de software que da libertades a sus usuarios, se considera <em>Software Privativo</em> a aquel que limite su copia, ejecución, distribución, estudio o modificación.



Recibir un software y tener prohibido darle copias de ese software a nuestros compañeros es un claro ejemplo de <em>Software Privativo</em>. También lo es software que no podemos modificar, ya sea porque su código fuente es inaccesible (no nos fue proporcionado y solo disponemos de una versión ejecutable del software) o porque (a pesar de disponer del código fuente, como es común en los programas escritos en lenguajes interpretados) su licencia de uso nos lo impide.



Para más información sobre Software Libre y Privativo, así como definiciones más exhaustivas, se puede visitar el sitio web del proyecto GNU: <a href="http://www.gnu.org/philosophy/philosophy.es.html" title="Filosofía GNU" target="_blank">http://www.gnu.org/philosophy/philosophy.es.html</a>



Dadas las dos definiciones previas enunciamos:



<strong>El estado no puede usar Software Privativo para cumplir sur rol, si lo hace está traicionando la confianza del pueblo.</strong>



En el resto del post se justifica esta afirmación. <!--more-->

<h2>¿Por qué?</h2>

Hoy vivismo en la llamada <em>Sociedad de la Información</em>. Muchas de las actividades que realizamos (como pagar impuestos o estudiar en la universidad) son replicadas en datos procesados por computadoras y archivados en soportes digitales. Muchas veces estamos en contacto con estas computadoras sin siquiera darnos cuenta o pensar en ello: cuando sacamos dinero del banco, pagamos por combustible o recibimos un <em>ticket</em> luego de comprar alimentos.



Entidades públicas y privadas hacen uso de este tipo de nuevas tecnologías para llevar a cabo de forma más eficiente sus actividades. El Estado imprimiendo impuestos para su cobro es un ejemplo de esto, pero por supuesto no el único.



En esta Sociedad de la Información el estado <em>necesita</em> utilizar Tecnologías de la Información para llevar a cabo una de sus funciones: mantener los registros públicos. Registros que indican quienes somos, que poseemos o que hacemos. Estos datos no <em>pertenecen</em> al estado, sino que son de los ciudadanos, pertenecen a la nación.



Cuando digo que <em>necesita</em> hacerlo trato de expresar que <em>imperiosamente necesita hacerlo</em>. No tiene otra alternativa, ya que no hacerlo así (no utilizar Tecnologías de Información para realizar las tareas que lo demanden) implicaría llevar un ritmo imposible de emparejar con el resto del mundo y se auto aislaría.



<strong>Cuando la administración pública maneja los datos de los ciudadanos con Tecnologías de la Información debe asegurarse de respetar 3 principios.</strong>

<h3>(1) Seguridad</h3>

Debe asegurarse de que nadie que no tenga el derecho de hacerlo acceda o altere los datos. También debe asegurarse de que nadie pueda evitar que los ciudadanos tengan acceso a esos datos.

<h3>(2) Persistencia</h3>

Debe tener en cuenta la persistencia de la información. Hay información que debe guardarse por 15, 50 o incluso 100 años. Tal vez no existe información que <em>debamos</em> guardar por tanto tiempo, pero de todas formas tenemos que poder hacerlo si así lo queremos, para utilizarla por ejemplo con fines estadísticos.



Tengamos en cuenta que estamos hablando de guardar información por más tiempo que el que la computación lleva existiendo.

<h3>(3) Transparencia</h3>

Cuando la administración pública usa software, lo está haciendo para implementar mandatos de la Ley. Y debe implementarla de una forma que pueda ser verificada por los ciudadanos. Ellos deben poder asegurarse de que la la ley se está siguiendo correctamente. Esto es fácil de hacer cuando se usas procedimientos manuales, pero cuando estos procedimientos son implementados parcial o totalmente en software, se necesita saber <em>que</em> hace el software. Si no se sabe, puede suceder que el software esté haciendo cosas en contra de la ley sin que nos enteremos. Si de alguna forma nos damos cuenta de que algo se está haciendo en contra de la ley, tampoco podríamos cambiarlo!

<h2>Justificación</h2>

De los 3 principios <strong>Persistencia</strong> es el único que podría cumplirse usando Software Privativo. Podría cumplirse solo si quien produce el software se compromete a adherirse a estándares libres, almacenando los datos que manejan exclusivamente con formatos considerados estándares libres y comunicándolos exclusivamente con protocolos considerados estándares libres. Solo en este caso el uso de Software Privativo podría no objetarse (para el cumplimiento de este principio), pero.. ¿hay algún Software Privativo que haga esto? ¿Algún productor de Software Privativo nunca cayó en la tentación de imponer su propio estándar?



Si bien sería teóricamente posible utilizar Software Privativo y cumplir con este principio, todavía existen otros 2 principios que se deben respetar.



Con Software Libre siempre se conoce la forma en que los datos son almacenados y comunicados.



<strong>Seguridad</strong>. Si bien el Software Libre no es naturalmente más seguro que el Software Privativo (ambos pueden tener <em>bugs</em>, los errores de programación simplemente suceden) insertar vulnerabilidades en forma intencional es mucho más difícil hacerlo en el primero.



En el Software Libre el código fuente está disponible para ser examinado por cualquiera que quiera hacerlo y esto es justamente lo que hace que sea en extremo difícil, sino imposible, esconder en él instrucciones maliciosas como sería una puerta trasera. En la práctica esta dificultad aumenta a medida que el software en cuestión tiene más usuarios y desarrolladores. La <a href="http://es.wikipedia.org/wiki/Ley_de_Linus" title="Ley de Linus" target="_blank">Ley de Linus</a> enuncia que <em>Dados muchos ojos, todos los errores serán obvios.</em>



El tercer principio, <strong>Transparencia</strong>,  SI es inherente al Software Libre y está relacionado con el principio anterior. La segunda libertad consiste en poder estudiar cómo el software está hecho. Esto permite a los usuarios del software, a los responsables de su funcionamiento (en este caso el Estado) o a quienes son afectados por este (los ciudadanos) auditar cómo se esta implementando la ley. Si alguien detecta un error puede corregirlo y verificar que el error ha desaparecido (si no posee las habilidades necesarias para corregirlo puede contratar a alguien que lo haga por él, pero no esta limitado de otra forma). Eventualmente la mejora podrá ser incorporada al software original.



Otras razones pueden darse para justificar el uso de Software Libre en el Estado y estas mismas pueden desarrollarse con más profundidad. Mucha documentación al respeto está disponible en Internet. Pero creo que estos 3 puntos son claves y es importante que los tengamos presente.

<h2>Una cuarta razón</h2>

No todos los países son monoculturales, y esto es especialmente cierto en América Latina. Hay países que se han comprometido en mantener la cultura de sus pueblos originarios. Una forma de hacer esto es manteniendo los registros públicos en las lenguas nativas del país (lenguas sin importancia comercial, pero muy importantes para el país). No hay esperanza de que las empresas de Software Privativo den soporte a estas lenguas, pero si se usa Software Libre los propios países pueden soportarlas.

<h2>Fuente e ideas</h2>

Este artículo está basado en un <a href="http://ia300115.us.archive.org/2/items/3_do_t1_20h_3-Silveira/3_do_t1_20h_3-Silveira_hi.mp4" title="Video Federico Heiz" target="_blank">video en el que habla Federico Heinz</a>. El video es referenciado desde <a href="http://en.wikipedia.org/wiki/Federico_Heinz" title="Federico heinz" target="_blank">wikipedia en inglés</a>.



En el video se mencionan los 3 principios pero no le dieron tiempo a Fede para justificar los 3. Para completar la información utilicé partes de <a href="http://www.proposicion.org.ar/doc/razones.html" title="Razones" target="_blank">este artículo</a>.



Más información al respecto puede encontrarse en el <a href="http://www.vialibre.org.ar/category/activismo/software-libre-en-administracion-publica/" title="FVL" target="_blank">sitio web de Fundación Vía Libre</a>.</body></html>