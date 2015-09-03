<html><body><p>Esta es una traducción al español Argentino del famoso artículo de Peter Norvig <a href="http://norvig.com/21-days.html" target="_blank">Teach Yourself Programming in Ten Years</a>. Hay una versión en <a href="http://loro.sf.net/notes/21-dias.html" target="_blank">español de España</a> pero está desactualizada. Creo que es un artículo que cualquiera que gusta de la programación debería leer.

</p><h1>Aprendé a programar en diez años</h1>

<strong>Por Peter Norvig.  <a href="http://norvig.com/21-days.html">Teach Yourself Programming in Ten Years</a></strong>.



Traducción libre al español Argentino por Juan José Conti - actualizado con el original a Diciembre de 2009

Originalmente basado en la versión de <a href="http://loro.sf.net" target="_blank">Calos Rueda</a>

<h2>¿Por qué están todos tan apurados?</h2>

Entrá a cualquier librería y vas a encontrar  <em>Aprende Java en 7 Días</em> y demás variaciones interminables ofreciendo enseñar Visual Basic, Windows, Internet, etc., en unos pocos días u horas. Yo hice la siguiente búsqueda avanzada (<a href="http://www.amazon.com/exec/obidos/tg/browse/-/468558/104-5938873-6579160">power search</a>) en <a href="http://www.amazon.com">Amazon.com</a> :

<pre style="text-align: center;"><a href="http://www.amazon.com/exec/obidos/search-handle-url/ix=books&amp;rank=%2Bfeaturedrank&amp;fqp=power%01pubdate%3A%20after%201992%20and%20title%3A%20days%20and%0D%20%28title%3A%20learn%20or%20title%3A%20teach%20yourself%29&amp;sz=25&amp;pg=1/ref=s_b_np">pubdate: after 1992 and title: days and </a><a href="http://www.amazon.com/exec/obidos/search-handle-url/ix=books&amp;rank=%2Bfeaturedrank&amp;fqp=power%01pubdate%3A%20after%201992%20and%20title%3A%20days%20and%0D%20%28title%3A%20learn%20or%20title%3A%20teach%20yourself%29&amp;sz=25&amp;pg=1/ref=s_b_np">(title: learn or title: teach yourself)</a></pre>

y obtuve 248 ítems de resultado. Los primeros 78 fueron libros de computación (el número 79 era <em>Aprende Bengali en 30 días</em> --<em><a href="http://www.amazon.com/exec/obidos/ASIN/0781802245/"> Learn Bengali in 30 days</a></em> ). Remplacé "days" (días) por <a href="http://www.amazon.com/exec/obidos/search-handle-url/ix=books&amp;rank=%2Bfeaturedrank&amp;fqp=power%01pubdate%3A%20after%201992%20and%20title%3A%20hours%20and%0D%20%28title%3A%20learn%20or%20title%3A%20teach%20yourself%29&amp;sz=25&amp;pg=3/ref=s_b_np">"hours"</a> (horas) y sorprendentemente obtuve resultados similares: 253 libros más, con 77 libros de computación seguidos de <em>Aprende Gramática y Estilo en 24 horas</em> (<em><a href="http://www.amazon.com/exec/obidos/ASIN/0028638999/">Teach Yourself Grammar and Style in 24 Hours</a></em>) en el número 78. Del total de los primeros 200, el  96% fueron libros de computación.



La conclusión es que, o bien la gente está muy apurada por saber de computadoras, o bien las computadoras son algo fabulosamente fácil de aprender, más que cualquiera otra cosa. No hay libros sobre cómo aprender Beethoven, o Física Cuántica, o incluso Estética Perruna en pocos días. Felleisen <em>et al.</em> asienten esta tendencia en su libro <em><a href="http://www.ccs.neu.edu/home/matthias/HtDP2e/index.html">How to Design Programs</a></em>, cuando dicen "La programación mala es fácil. Los <em>idioitas</em> pueden aprenderla en 21 días, incluso si son <em>tontos</em>" (original: "Bad programming is easy. <em>Idiots</em> can learn it in <em>21 days</em>, even if they are <em>dummies</em>.)



Analicemos lo que podría significar un título como <em>Aprende C++ en Tres Días </em>(<em><a href="http://www.amazon.com/Learn-C-Three-Days-Rachele/dp/1556227078">Learn C++ in Three Days</a></em>):

<ul>

	<li> <strong>Aprende:</strong> En 3 días no vas a tener tiempo de escribir varios programas significativos, y de aprender de tus aciertos y errores con ellos. No vas a tener tiempo de trabajar con un programador experimentado y entender lo que es vivir en un ambiente de C++. En resumen, no vas a tener tiempo de aprender mucho. Así que esos libros sólo podrán lograr una familiaridad superficial, no un entendimiento profundo. Como dijo Alexander Pope, poco aprendizaje es una cosa peligrosa.</li>

	<li> <strong>C++</strong><strong>:</strong> En 3 días puedes aprender la sintaxis de C++ (si ya sabés otro lenguaje), pero no vas a poder aprender mucho sobre cómo usar el lenguaje. En síntesis, si fueras, digamos, un programador Basic, podrías aprender a escribir programas en el estilo de Basic usando la sintaxis de C++, pero no aprenderías para qué C++ es realmente bueno (o malo). Entonces ¿cuál es el punto? <a href="http://www-pu.informatik.uni-tuebingen.de/users/klaeren/epigrams.html">Alan Perlis</a> dijo alguna vez: "Un lenguaje que no afecte tu manera de pensar acerca de la programación, no merece ser aprendido". Un objetivo posible es que tienes que aprender un poco de C++ (o más probablemente, algo como Visual Basic o JavaScript) porque necesitas tener una interface con una herramienta existente para realizar una cierta tarea. Pero entonces no estás aprendiendo cómo programar; estás aprendiendo

cómo realizar esa tarea.</li>

	<li> <strong>en Tres Días:</strong> Desafortunadamente, no son suficientes, como se describe en la siguiente sección.</li>

</ul>

<h2><!--more-->Aprendé a programar en diez años</h2>

Algunos investigadores (<a href="http://www.amazon.com/exec/obidos/ASIN/034531509X/">Bloom (1985)</a>, <a href="http://norvig.com/21-days.html#bh">Bryan &amp; Harter (1899)</a>, <a href="http://www.amazon.com/exec/obidos/ASIN/0805803092">Hayes (1989)</a>, <a href="http://norvig.com/21-days.html#sc">Simmon &amp; Chase (1973)</a>) han mostrado que toma aproximadamente diez años desarrollar habilidades en cualquiera de una amplia variedad de áreas,  incluyendo jugar al  ajedrez, componer música, pintar, tocar el piano, operar un telégrafo, nadar, jugar al tenis, u investigar en neurosicología y topología. La clave es la práctica <em>deliberada</em>: no solo hacerlo una y otra vez, sino desafiarte con una tarea que es un poco más dificil que tu habilidad actual, intentando, analizando tu performance mientras lo hacés y corrigiendo cualquier error. Luego repetir. Y volver a repetir. Parece no haber atajos: incluso a Mozart, prodigio musical a los 4 años, le tomó 13 más empezar a producir música de calidad mundial. En otro género, parece que los Beatles llegan a escena apareciendo en el espectáculo de Ed Sullivan en 1964. Pero ellos habían estado tocando desde 1957, y aunque tenían una masa de seguidores desde antes, su primer gran éxito, <em>Sgt. Peppers</em>, apareció en 1967. <a href="http://www.amazon.com/Outliers-Story-Success-Malcolm-Gladwell/dp/0316017922">Malcolm Gladwell</a> reportó que un estudio en la Academia de Música de Berlín separó a los mejores, los del meido y los peores de la clase y les preguntó cuánto practicaban:

<blockquote>Todas las personas, las de los tres grupos, empezar a tocar casi al mismo tiempo (alrededor de la edad de 5 años). En esos primeros pocos años, todos practicaron casi la misma cantidad (dos o tres horas por semana). Pero a la edad de ocho, empezaro a surgir las verdaderas diferencias. Los estudiantes que terminarían en el mejor tercio de la clase empezaron a practicar más que los demás: seis horas a la semana a los nueve, ocho a los 12, 16 a los 14, y más y más hasta que a la edad de 20, los músicos elite alcanzaraon las 10000 horas de práctica en el curso de sus vidas. Los estudiantes que solo eran buenos sumaron 8000 horas y los futuros profesores de música solo 4000.</blockquote>

Entonces, deben ser esas 10000 horas, no los 10 años, el número mágico. Samuel Johnson (1709-1784) pensaba que llevaba más: "La excelencia en cualquier área solo puede lograrse con la labor de toda la vida; no debe ser comprada a un precio menor" . Y Chaucer (1340-1400) se quejaba de que  "la vida era muy corta, y el trabajo largo de aprender". Hipócrates (c. 400BC) es conocido por la frase "ars longa, vita brevis", qué es parte de una cita más larga: "Ars longa, vita brevis, occasio praeceps, experimentum periculosum, iudicium difficile", que significa algo como "La vida es corta, el trabajo largo, la oportunidad fugaz, experimentar es traicionero, el juicio dificil". Aunque en Latin, <em>ars</em> puede significar tanto arte como trabajo, en el original griego "techne" solo puede significar "destreza", no "arte".



Aquí está mi receta para el éxito en programación:

<ul>

	<li> Interesate en la programación y programá, porque es divertida. Asegúrate de que siga siendo divertida, tanto que podrías invertir diez años haciéndolo.</li>

	<li> Habla con otros programadores. Lee otros programas. Esto es más importante que cualquier libro o curso.</li>

	<li> Programa. El mejor tipo de aprendizaje es <em>aprender haciendo</em> (<a href="http://www.engines4ed.org/hyperbook/nodes/NODE-120-pg.html">learning by doing)</a> . Para decirlo más técnicamente, "El máximo nivel de desempeño de los individuos en un dominio dado, no se logra automáticamente como función de experiencia extendida, sino que el nivel de desempeño puede incrementarse incluso en individuos altamente experimentados como resultado de esfuerzos deliberados por mejorar."<a href="http://www2.umassd.edu/swpi/DesignInCS/expertise.html">(p.

366)</a> y "el aprendizaje más efectivo requiere una tarea bien definida con un apropiado nivel de dificultad acorde con el individuo, retroalimentación informativa, y oportunidades de repetición y corrección de errores." (p. 20-21) El libro <em><a href="http://www.amazon.com/exec/obidos/ASIN/0521357349">Cognition in Practice: Mind, Mathematics, and Culture in Everyday Life</a> </em>es una interesante referencia sobre este punto de vista.</li>

	<li> Si querés, dedica cuatro o cinco años en una universidad (o más en una escuela de graduados). Esto te dará acceso a algunos posiciones que requieren credenciales, y te dará un entendimiento más profundo del campo, pero si no disfrutas la escuela, puedes (con algo de dedicación) obtener una experiencia similar trabajando. Como sea, la lectura de libros por sí sola no será suficiente. "La educación en computación no puede hacer a nadie un experto programador más que el estudio de pinceles y pigmentos puede hacer a alguien un pintor experto" dice Eric Raymond, autor de <em>The New Hacker's Dictionary</em>. Unos de los mejores programadores que yo haya contratado alguna vez tenía sólamente un grado de bachiller (High School); pero ha producido una gran cantidad de <a href="http://www.xemacs.org">excelentes</a> <a href="http://www.mozilla.org">programas</a> , tiene su propio grupo de noticias (news <a href="http://groups.google.com/groups?q=alt.fan.jwz&amp;meta=site%3Dgroups">group)</a> , y sin duda es mucho más rico de lo que yo llegue a ser.</li>

	<li> Trabajá en proyectos con otros programadores. Sé el mejor programador en algunos proyectos; sé el peor en otros. Cuando sos el mejor, ponés a prueba tus habilidades para liderar un proyecto y para inspirar a otros con tu visión. Cuando sos el peor, aprendés lo que los maestros hacen, y aprendes lo que a ellos no les gusta hacer (ya que te ponen a hacerlo a vos).</li>

	<li> Trabajá en proyectos <em>después</em> de otros programadores. Proponete entender un programa escrito por otra persona. Mirá cuánto toma entenderlo y hacele correcciones cuando los programadores originales no estén allí. Pensá cómo diseñar tus programas para facilitarles el trabajo a los que deban mantenerlo después de vos.</li>

	<li> Aprende por lo menos una media docena de lenguajes de programación.mIncluye uno con soporte para abstracciones de clases (como Java o C++),

uno que dé soporte a la abstracción funcional (como Lisp o ML), uno que dé soporte a la abstracción sintáctica (como Lisp), uno que dé soporte a especificationes declarativas (como Prolog o plantillas C++), uno que dé soporte a corutinas (como Icon o Scheme), y uno que dé soporte al paralelismo (como Sisal).</li>

	<li> Recordá que hay una "computadora" en "ciencia de la computación". Conoce cuánto le toma a tu computadora ejecutar una instrucción, alcanzar una palabra de la memoria (con y sin cache), leer palabras consecutivas del disco, y ubicar una nueva localización en disco. (Respuestas más abajo)</li>

	<li> Participá de un plan de estandarización de algún lenguaje. Podría ser en el mismo comité ANSI C++, o podría ser simplemente decidir si tu estilo de codificación tendrá niveles de identación de 2 ó 4 espacios. Como sea, averiguá lo que les gusta a otras personas en un lenguaje, cómo lo perciben, y quizá incluso un poco de por qué lo perciben como lo hacen.</li>

	<li> Tené el buen juicio para lanzar el plan de estandarización del lenguaje tan pronto como sea posible.</li>

</ul>

Con todo lo anterior en mente, es cuestionable qué tan lejos puedes llegar sólo leyendo libros. Antes de que naciera mi primer hijo, leí todos los libros <em>Aprende a </em>(<em>How To</em>), y sin embargo me sentía como un tonto principiante. 30 meses después, cuando nació mi segundo hijo, ¿acaso regresé a los libros? No.



Al contrario, me apoyé en mi experiencia personal, que me resultó mucho más útil y confiable que las miles de páginas escritas por los expertos.



Fred Brooks, en su ensayo <em><a href="http://citeseer.nj.nec.com/context/7718/0">No Silver Bullets</a></em>, identificó un plan de tres partes para encontrar grandes diseñadores de programas:

<ol>

	<li> Sistemáticamente identificar a los diseñadores líderes lo más pronto posible.</li>

	<li> Asignar un tutor de carrera para que sea responsable del desarrollo del prospecto y mantené un cuidadoso registro de todo.</li>

	<li> Ofrecer oportunidades a los diseñadores en crecimiento para que interactúen y se motiven mutuamente.</li>

</ol>

Esto asume que algunas personas ya tienen las cualidades necesarias para ser grandes diseñadores; la tarea es persuadirlos apropiadamente.

<a href="http://www-pu.informatik.uni-tuebingen.de/users/klaeren/epigrams.html">Alan Perlis</a> lo dice de manera más sucinta: "A cualquiera se le puede enseñar a esculpir: A Miguel Angel habría que habérsele enseñado cómo no hacerlo. Así pasa con los grandes programadores".



Así que adelante, compra ese libro de Java; probablemente obtendrás algo de él. Pero no cambiará tu vida o tus verdaderas habilidades como programador en 24 horas, días o incluso meses.

<h2>Referencias</h2>

Bloom, Benjamin (ed.) <em><a href="http://www.amazon.com/exec/obidos/ASIN/034531509X">Developing Talent in Young People</a></em>, Ballantine, 1985.



Brooks, Fred, <em><a href="http://citeseer.nj.nec.com/context/7718/0">No Silver Bullets</a></em>, IEEE Computer, vol. 20, no. 4, 1987, p. 10-19.



Hayes, John R., <em><a href="http://www.amazon.com/exec/obidos/ASIN/0805803092">Complete Problem Solver</a></em> Lawrence Erlbaum, 1989.



Lave, Jean, <em><a href="http://www.amazon.com/exec/obidos/ASIN/0521357349">Cognition in Practice: Mind, Mathematics, and Culture in Everyday Life</a></em>, Cambridge University Press, 1988.

<h2>Respuestas</h2>

Tiempos de demora de varias operaciones en una PC típica de 1GHz, verano de 2001:

<table border="1" cellspacing="2" cellpadding="2">

<tbody>

<tr>

<td>execute single instruction</td>

<td>1 nsec = (1/1,000,000,000) sec</td>

</tr>

<tr>

<td>fetch word from L1 cache memory</td>

<td>2 nsec</td>

</tr>

<tr>

<td>fetch word from main memory</td>

<td>10 nsec</td>

</tr>

<tr>

<td>fetch word from consecutive disk location</td>

<td>200 nsec</td>

</tr>

<tr>

<td>fetch word from new disk location (seek)</td>

<td>8,000,000nsec = 8msec</td>

</tr>

</tbody>

</table>

<h2>Apéndice: Elección del lenguaje</h2>

Muchas personas me preguntaron qué lenguaje de programación deberían aprender primero. No hay una única respuesta, pero considerá estos puntos:

<ul>

	<li><em>Usá a tus amigos.</em> Cuando me preguntan "qué sistema operativo debería usar, Windows, Unix, o Mac", mi respuesta suele ser : "usá lo que tus amigos usen".  La ventaja que tenés de aprender de tus amigos compensará cualquier diferencia intrínsica entre  entre sistemas operativos o entre lenguajes de programación. También considerá a tus futuros amigos: la comunidad de programadores de la que vas a ser parte si continuás. ¿Tu lenguaje elejido tiene una comunidad amplia y en crecimiento o una pequeña y agonizante? ¿Hay libros, sitios web y foros en línea de dónde obtener respuestas? ¿Te caen bien las personas en esos foros?</li>

	<li><em>Mantenelo simple</em>. Los lenguajes de programación como C++  y Java están diseñados para que desarrollen grandes equipos de programadores profesionales preocupados por la eficiencia en  tiempo de ejecución de su código. Como resultado, estos lenguajes tienen partes complicadas diseñadas para estas circunstancias. Vos estás preocupado en aprender a programar.  No necesitás esas complicaciones. Querés un lenguaje diseñado para ser fácil de aprender y recordar para un programador nuevo.</li>

	<li><em>Jugá.</em> ¿De qué forma preferirías aprender a tocar el piano: de la forma normal, interactiva, en la que escuchás cada nota inmediatamente después de apretar una tecla, o en modo "batch", solo escuchando las notas después de terminar de teclear una canción entera? Claramente, el modo interactivo hace que el aprendizaje de tocar el piano sea más fácil; también de la programación. Intentá con lenguajes que tengan un modo interactivo y usalo.</li>

</ul>

Con estos criterios, mis recomendaciones para un promer lenguaje de programacion serían <strong><a href="http://python.org/">Python</a></strong> o <strong><a href="http://www.schemers.org/">Scheme</a></strong>.Pero tus circunstancias pueden variar, y hay otras buenas opciones. Si tu edad es de un solo dígito, tal vez prefieras <a href="http://alice.org/">Alice</a> o <a href="http://www.squeak.org/">Squeak</a> (aprendices mayores también apreciarían este). Lo importante es que hagas la elección y empieces.

<h2>Apéndice: Libros y otros recursos</h2>

Varias personas me preguntaron qué libros y páginas web utilizar para su aprendizaje. Repito que el aprendizaje solitario con un libro no es suficiente, pero puedo recomendar los siguientes:

<ul>

	<li> <strong>Scheme:</strong> <a href="http://www.amazon.com/gp/product/0262011530">Structure and Interpretation of Computer Programs (Abelson &amp; Sussman)</a> es probablemente la mejor introducción a la ciencia de la computación, y también enseña programación. Podés ver <a href="http://www.swiss.ai.mit.edu/classes/6.001/abelson-sussman-lectures/">videos en línea de las clases</a> basadas en el libro, así como el <a href="http://mitpress.mit.edu/sicp/full-text/book/book.html">texto completo en línea</a>. El libro es desafiante y puede desanimar a personas que podrían tener éxito con otro enfoque.</li>

	<li> <strong>Scheme:</strong> <a href="http://www.amazon.com/gp/product/0262062186">How to Design Programs (Felleisen <em>et al.</em>)</a> es uno de los mejores libros sobre cómo realmente diseñar programas de forma elegante y funcional.</li>

	<li> <strong>Python:</strong> <a href="http://www.amazon.com/gp/product/1887902996">Python Programming: An Intro to CS (Zelle)</a> es una buena introducción utilizando Python.</li>

	<li> <strong>Python:</strong> Varios <a href="http://wiki.python.org/moin/BeginnersGuide">tutoriales</a> en línea disponibles en <a href="http://python.org/">Python.org</a>.</li>

	<li> <strong>Oz:</strong> <a href="http://www.amazon.com/gp/product/0262220695">Concepts, Techniques, and Models of Computer Programming (Van Roy &amp; Haridi)</a> es visto por varios como el sucesor moderno al libro de Abelson &amp; Sussman. Es un tour por las grandes ideas de la programación, cubriendo un rango más amplio que Abelson &amp; Sussman a la vez que es tal vez más fácil de leer y seguir. Usa Oz, un lenguaje que no es ampliamente conocido pero sirve de base para aprender otros lenguajes.</li>

</ul>

<h2>Notas</h2>

T. Capey señala que la página <a href="http://www.amazon.com/exec/obidos/ASIN/0805803092">Complete   Problem Solver</a> en Amazon hoy tiene a los libros "Teach Yourself   Bengali in 21 days" y "Teach Yourself Grammar and Style" bajo la sección "Los clientes que compraron este item, también compraron estos items". Supongo que una gran cantidad de personas que miran ese libro vienen de esta página. Gracias a Ross Cohen por ayudar con Hipócrates.



<a href="http://norvig.com/index.html"><em>Peter Norvig</em> (Copyright 2001)</a></body></html>