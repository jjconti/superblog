<html><body><p>Hola! mi nombre es Juanjo Conti y tal vez me recuerden de críticas a libros de <a href="http://www.danbrown.com/" title="Sitio del autor" target="_blank">Dan Brown</a> como <em>El Código Da Vinci no compila</em>.



En esta ocasión me gustaría comentar detalles que se presentan cuando uno lee su primera novela <strong>La Fortaleza Digital</strong>, algunos incluso centrales en la trama (?).



Antes de empezar les cuento que, más allá del chiste inicial, éste es el primer libro que leo de este autor. Sé que existen otros llamados La Conspiración y Ángeles y Demonios y también sé que no pienso gastar mi tiempo con El Código Da Vinci.



Cuando terminé de leer el libro busqué en Internet algunas críticas, lo siguiente si bien no hace referencia a cuestiones técnicas (éstas fueron las que más me llamaron la atención) es una buena introducción para derrumbar La Fortaleza Digital.

<!--more-->

</p><blockquote>En principio, podríamos decir que "Fortaleza Digital" no es <em>una</em> novela de Dan Brown. Es <em>la</em> novela de Dan Brown. Quiero decir que cualquier lector que haya sufrido las restantes obras del autor encontrará en "Fortaleza Digital" exactamente lo mismo. Y no me refiero a que sus personajes sean tan estereotipados como siempre, sus situaciones igual de forzadas, o sus tramas lo mismo de previsibles, no. Quiero decir que son <em>exactamente los mismos</em> que en las anteriores novelas.



De modo que si usted ha leído ya algo de Dan Brown sabrá sin necesidad de abrir el libro, por ejemplo, cómo son los personajes. Exacto: los buenos son un hombre y una mujer jóvenes, altos, guapos e inteligentísimos. Los malos se dividen, como no podía ser menos, en un casi anciano jefe, que asume un papel aparentemente protector hacia la chica pero que resulta ser un malvado de tomo y lomo -aunque por una buena causa, eso sí- y un asesino sin escrúpulos que, para no variar, sufre una tara física (en este caso es sordo). Y a su alrededor, como también es costumbre de la casa, pululan una serie de personajes para los que Brown no parece decidirse a otorgarles un papel protagonista o secundario, pero que también responden fielmente a los tópicos más tontos que podamos imaginar: el "gurú" informático, devorador compulsivo de pizzas e incapaz de someterse a disciplina alguna; la jefe de seguridad, de constancia implacable e instinto infalible; el asistente del Director de la NSA, indeciso y timorato... Da la impresión de que Dan Brown tuviese acceso a la papelera a donde van a parar los personajes que, por tópicos, planos o absurdos, no quieren emplear los novelistas de verdad.



Pero el hecho de que los personajes sean tópicos y sencillotes no quiere decir que Brown sea capaz de manejarlos con habilidad. Más bien todo lo contrario. Para mostrarnos cómo es la protagonista, Susan Fletcher, Brown hace que un guardia de seguridad, contemplando sus piernas, murmure para sí

<blockquote>"Es difícil creer que tengan encima un coeficiente intelectual de 170".</blockquote>

La frase, a primera vista, parece sugerirnos tan sólo que Susan es guapa y es inteligente, cualidades que por lo visto a Brown le parecen raramente compatibles. Pero basta avanzar un poquito en el libro para darnos cuenta de la profunda verdad que encierran esas palabras: en efecto, el comportamiento de Susan hace difícil de imaginar que tenga un CI de 170, o de 17, y a veces no parece ni llegar a 1,7. A lo largo del libro, la extraordinaria criptóloga de la NSA que pretende vendernos la novela se nos revela como una pobre tonta incapaz de darse cuenta de una trama que el lector va adivinando sin ningún esfuerzo. Eso sí, la chica muestra una gran capacidad de asombro, repitiéndose a sí misma tres veces las cosas para recalcarnos lo sorprendentes que resultan esos giros argumentales que vemos venir desde hace ocho capítulos. Y si como detective no es gran cosa, como criptóloga tampoco crean que es nada del otro mundo: las últimas páginas son un suplicio para el lector, que ve cómo transcurren los párrafos sin que la experta en claves sea capaz ni siquiera de reconocer las que cualquiera ha podido comprender y descifrar al primer vistazo.</blockquote>

<p align="right">Fuente: <a href="http://yamato1.blogspot.com/2006/02/fortaleza-digital.html" title="Fuente 1" target="_blank">http://yamato1.blogspot.com/2006/02/fortaleza-digital.html</a></p>



<h2>Edición</h2>

<p align="left">Las siguientes observaciones están basadas en la edición en español de la <a href="http://www.umbrieleditores.com/" title="La editorial" target="_blank">editorial Umbriel</a>, ISBN 84-89367-01-9.</p>



<h2>Combinaciones</h2>

En el capítulo 4, página 36 del libro el autor dice que <em>en los años 90 las claves de acceso tenían más de 50 caracteres de longitud y empleaban 256 caracteres ASCII (letras, números y símbolos)</em>. Completa diciendo que <em>las posibilidades diferentes se acercan a 10<sup>120</sup> </em>y aclara: <em>10 seguido de 120 ceros</em>.



Vamos por partes:

<ul>

	<li>El número de claves de (digamos) 56 caracteres que se pueden generar con  256 caracteres es 256<sup>56</sup> y es mucho mayor a 10<sup>120</sup> como mi computadora puede demostrar:

<pre>

&gt;&gt;&gt; 256**56

726838724295606890549323807888004534353641

360687318060281490199180639288113397923326

191050713763565560762521606266177933534601628614656L

&gt;&gt;&gt; 256**56 - 10**120

726838724295605890549323807888004534353641

360687318060281490199180639288113397923326

191050713763565560762521606266177933534601628614656L

&gt;&gt;&gt; 10**120

100000000000000000000000000000000000000000

000000000000000000000000000000000000000000

0000000000000000000000000000000000000L

&gt;&gt;&gt; a = 256**56

&gt;&gt;&gt; b = 10**120

&gt;&gt;&gt; a &lt; b

False

&gt;&gt;&gt; a &gt; b

True

&gt;&gt;&gt; mil = range(0,1000)

&gt;&gt;&gt; for n in mil:

        if a &lt; 10**n:

                print n

                break

135</pre>

256<sup>56</sup> está entre 10<sup>134</sup> y 10<sup>135</sup>.</li>

	<li>10<sup>120</sup> no es 10 seguido de 120 ceros, sino 10 seguido de 119 ceros. Así como 10<sup>1</sup> es 10 seguido de 0 ceros y 10<sup>2</sup> es 10 seguido de 1 cero. Regla general: 10<sup>n</sup> es 10 seguido de n-1 ceros.</li>

</ul>

<h2>Algoritmos de encriptación</h2>

En el capítulo 5, página 45 bajo el título Algoritmos de encriptación se menciona:

<ul>

	<li>IDEA: ok, algoritmo de llave privada.</li>

	<li>El Gamal: ok, algoritmo de llave pública.</li>

	<li>PGP: sistema de encriptación (no es un algoritmo) <a href="http://en.wikipedia.org/wiki/Pretty_Good_Privacy" title="PGP" target="_blank">[a]</a></li>

	<li>Diffie-Hellman: es un protocolo criptográfico <a href="http://en.wikipedia.org/wiki/Diffie-Hellman" title="DH" target="_blank">[b]</a> <a href="http://en.wikipedia.org/wiki/Cryptographic_protocol" title="Cryptographic protocol" target="_blank">[c]</a></li>

	<li>ZIP: es un algoritmo pero no de encriptación, sino de compresión. <a href="http://en.wikipedia.org/wiki/ZIP_%28file_format%29" title="ZIP" target="_blank">[d]</a></li>

</ul>

<h2>Josef Harne y la función de texto llano rotatorio</h2>

La base de toda la novela es un supuesto código indescifrable. La historia lo sustenta mencionando a un oscuro matemático y un oscuro <em>paper</em> en un oscuro congreso. Nada de esto existe. Una discusión al respecto en <a href="http://www.derkeiler.com/Newsgroups/sci.crypt/2005-08/0049.html" title="Harne?" target="_blank">http://www.derkeiler.com/Newsgroups/sci.crypt/2005-08/0049.html</a>

<h2>Cifrado de Julio César</h2>

<blockquote>

<p align="left">Julio César, explicó, fue el primer escritor de códigos secretos de la historia. Cuando sus emisarios empezaron a caer en emboscadas, y sus mensajes comenzaron a ser robados, diseñó un método rudimentario de codificar sus órdenes. Reordenó el texto de sus mensajes de manera que la correspondencia parecía absurda. No lo era, claro está. Cada mensaje contenía siempre un número de letras que constituía un cuadrado perfecto (dieciséis, veinticinco, cien), en función de lo que Julio César necesitara decir. Avisó en secreto a sus oficiales de que, cuando recibieran un mensaje absurdo, debían copiar el texto en una tabla con rejilla cuadriculada. Si lo hacían así, y leían de arriba abajo, aparecería un mensaje secreto como por arte de magia.</p>

</blockquote>

Esto me sorprendió porque no recordaba que a esto en particular se lo conociera como el <a href="http://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar" title="César" target="_blank">Cifrado del César</a>. Por suerte una búsqueda en Wikipedia me confirmó lo que sospechaba.

<blockquote>En criptografía, un cifrado César, también conocido como cifrado por desplazamiento, es una de las técnicas de codificación más simples y más usadas. Es un tipo de cifrado por sustitución en el que una letra en el texto original es reemplazada por otra letra que se encuentra en una posición que está un número determinado de espacios más adelante en el alfabeto. Por ejemplo, con un desplazamiento de 3, la A sería reemplazada por la D (situada 3 lugares a la derecha de la A ), la B sería reemplazada por la E, etcétera. Este método debe su nombre a Julio César, que lo usaba para comunicarse con sus generales.</blockquote>

<h2><span class="mw-headline">NSA </span></h2>

Me llamó la atención como a lo largo del libro se subestima a la agencia norteamericana: contraseñas de 5 caracteres? un piso completo de gente y nadie sabe cuestiones básicas sobre los <a href="http://es.wikipedia.org/wiki/Tabla_peri%C3%B3dica_de_los_elementos" title="Tabla periódica" target="_blank">elementos químicos</a>? toda un área está por explotar y nadie se entera? Acceso <a href="http://es.wikipedia.org/wiki/File_Transfer_Protocol" title="Protocolo no seguro" target="_blank">FTP</a> a su banco de datos secreto? No puede ser.

<h2><span class="mw-headline">EFF</span></h2>

Como en la novela NSA son los buenos, <a href="http://www.eff.org/" title="EFF" target="_blank">EFF</a> (Electronic Frontier Foundation), una organización sin ánimo de lucro con sede en Estados Unidos con el objetivo declarado de dedicar sus esfuerzos a conservar los derechos de libertad de expresión en el contexto de la era digital actual, aparece en todo el libro como una <em>molestia</em>. Tal vez lo sea para ellos, pero los usuarios de Internet tenemos que estarle agradecidos. Por favor considerá hacer <a href="https://secure.eff.org/site/SPageServer?pagename=DON_splash" title="support EFF" target="_blank">una donación</a> para apoyarla.

<h2><span class="mw-headline">Citas</span></h2>

<h3>Hackers</h3>

<blockquote>Los <em>hackers,</em> al igual que las hienas, formaba una gran familia, siempre ansiosos por correr la voz de que había una nueva presa.</blockquote>

Y en otra parte son pintados como <em>tiburones que huelen sangre en el agua</em>. Eso no se parece en nada a lo que es un <a href="http://www.catb.org/jargon/html/H/hacker.html" title="Hacker " target="_blank">hacker</a>. Muy por el contrario coincide más con la definición de <a href="http://www.catb.org/jargon/html/C/cracker.html" title="Cracker" target="_blank">cracker</a>.

<h3>Browsers</h3>

<blockquote>- Necesito acceder a Internet. ¿Qué navegadores tienen instalados?

- El mejor es Netscape - dijo Soshi

Susan le agarro la mano.

- Vamos a navegar</blockquote>

Se ve que para el tiempo en que fue escrita la novela no existía <a href="http://www.mozilla-europe.org/es/products/firefox/" title="El premdiado navegador web" target="_blank">FireFox</a> :)

<h2>Bug en el código final</h2>

Al final del libro, luego del Epílogo se presenta un código. En mi libro era:

<code>

128 - 10 - 93 - 85 - 10 - 128 - 98 - 112 - 6 - 25 - 126 - 39 - 1 - 68 - 78</code>



Lo primero que hice fue contar los números. 15. Me llamó la atención que la cantidad no fuera un cuadrado perfecto para así aplicar la técnica de armar un cuadrado con los caracteres planteada en el libro.  Leyendo <a href="http://es.wikipedia.org/wiki/La_fortaleza_digital#Resolucion_del_codigo_final" title="Fortaleza Digital en Wikipedia" target="_blank">en Wikipedia</a> encontré la solución al código:

<blockquote> Luego de finalizar el libro aparece impreso el siguiente codigo: <code>128 - 10 - 93 - 85 - 10 - 128 - 98 - 112 - 6 - 6 - 25 - 126 - 39 - 1 - 68 - 78 </code>. Para resolverlo solo debemos anotar la primera letra (de la Edición en Inglés) del capitulo indicado. El código resultante es el siguiente: <code>WECGEWHYAAIORTNU</code>



Que casualmente forma un cuadrado perfecto si lo colocamos de esta forma:

<pre>   W E C G

   E W H Y

   A A I O

   R T N U</pre>

si lo leemos como indica en el propio libro (de arriba a abajo):

<pre>   WEAREWATCHINGYOU</pre>

que forma la frase: <em>We are watching you</em>. Te estamos mirando, referido al lema de la NSA que lo controla todo.</blockquote>

¿¿Se dieron cuenta del error?? En mi libro falta un 6!

<h2><span class="mw-headline">Y hay mucho más</span></h2>

No dejen de leer el libro, a pesar de ser técnicamente insustentable me entretuvo mucho. Lean con atención y encontrarán muchas otras fallas. No dejen de comentarlas en este <em>post</em>!

<h2><span class="mw-headline">Críticas en España</span></h2>

<blockquote>Esta novela ha sido criticada por cometer una serie de errores en la ambientación y en la descripción de Sevilla, además de ofrecer una imagen tercermundista de España.



Por ejemplo, se dice que el zumo de arándanos es <em>typical spanish</em>, que la policía española es fácilmente sobornable, que los hospitales sevillanos huelen a orina y los enfermos están en catres en vez de en camas, que a la Giralda se sube por escaleras en vez de por rampas, etc.



En la edición para España, Dan Brown afirma que estuvo un año como estudiante en la Universidad de Sevilla. Sin embargo, esta institución afirma que Dan Brown no figura en ningún registro y que, si estuvo en esta Universidad, fue acaso en algún curso de verano.</blockquote>

<p align="left">Leer más en <a href="http://blogs.periodistadigital.com/periodismo.php/2006/02/10/ies_dan_brown_un_mentiroso_compulsivo" title="PD" target="_blank">PeriodistaDigital</a>.</p>



<h2>Versión en inglés</h2>

Al finalizar este artículo encontré uno en inglés que resalta algunos errores que aquí destaco y otros que son exclusivos de la versión en esa lengua :) <a href="http://becomingparanoid.com/2006/03/13/digital-fortress-what-dan-brown-got-wrong/" title="BecamingParanoid" target="_blank">http://becomingparanoid.com/2006/03/13/digital-fortress-what-dan-brown-got-wrong/</a>

<blockquote></blockquote></body></html>