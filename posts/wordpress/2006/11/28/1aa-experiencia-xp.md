<html><body><h2>Métodos Ágiles</h2>

Métodos Ágiles para el Desarrollo de Software es una materia electiva del segundo cuatrimestre de 4º año de Ingeniería en Sistemas de Información en la la facultad dónde estudio (<a href="http://www.frsf.utn.edu.ar">UTN-FRSF</a>). Yendo al grano: estudia los llamados <a href="http://www.agile-spain.com/agilev2/manifiesto_agil">Métodos Ágiles</a>, en particular <a href="http://www.extremeprogramming.org/">eXtreme Programming</a>.



La idea de estas metodologías, a diferencia de las tradicionales es evitar la tortuosa y burocrática documentación, a la vez que se enfocan en las personas y en los resultados.

<h2>XP: Programación eXtrema</h2>

Dentro de este contexto, la Programación eXtrema (una de las metodologías más exitosas del rubro) se presenta como una diciplina de desarrollo de software basada en valores como <em>simplicidad</em>, <em>comunicación</em>, <em>retroalimentación</em> y <em>valor.</em> Trabaja poniendo a todo el equipo ante práctica simples, con suficiente retroalimentación para permitirle ver dónde está y cómo encarar un problema particular.



En XP, cada contribuidor al proyecto es una parte integral del <em>Equipo.</em> El equipo se forma al rededor de un representante del negocio, llamado <em>El Cliente</em>, el cual se sienta y trabaja con el equipo diariamente (cliente <em>in-situ</em>).

<!--more-->

Nuestro trabajo práctico consistía en desarrollar la primer versión de un sistema de gestión de socios de un club en base a una lista de <em>historias</em> provistas por la prfesora. Las <a href="http://www.extremeprogramming.org/rules/userstories.html">historias</a> son la forma en la que XP define los requisitos para el sistema.



Para realizarlo llevamos a cabo algunas de las prácticas que XP propone (las escribo sin un orden específico), <strong>bold</strong> significa que aplicamos conscientemente la práctica:

<ul>

	<li>Cliente in-situ</li>

	<li><strong>Juego de la planificación</strong></li>

	<li>Metáfora</li>

	<li>40 hs semanales</li>

	<li><strong>Diseño sencillo</strong></li>

	<li><strong>Recodificación</strong></li>

	<li><strong>Programación en parejas</strong></li>

	<li><strong>Pruebas</strong></li>

	<li>Versiones cortas</li>

	<li><strong>Propiedad colectiva</strong></li>

	<li><strong>Estándares de codificación</strong></li>

	<li><strong>Integración continua</strong></li>

</ul>

Puede ser que el listado de prácticas no sea novedoso para algunos, de hecho son todas prácticas existentes. XP lleva su nombre por llevar todas estas prácticas al extremo. Si hacer  pruebas es bueno, se escribirán pruebas para todos los métodos que lo ameriten y luego se escribirá el código que pase esas pruebas. Si integrar es bueno, se integrará continuamente. Si la retroalimentación del cliente es buena, se sumará este al equipo de desarrollo.



Se puede leer más sobre XP en:

<ul>

	<li><a href="http://www.xprogramming.com">xprogramming.com</a></li>

	<li><a href="http://www.extremeprogramming.org">www.extremeprogramming.org</a></li>

</ul>

<h2>Programación en parejas</h2>

Una de las prácticas que conscientemente llevamos a cabo fue la de programar en parejas. En el grupo eramos 4 y tuvimos la suerte de trabajar siempre en una casa con dos computadoras, por lo que las parejas podían ir rotando y hacerse consultas entre ellas. A mi parecer es una de las prácticas más importantes de XP, y es un tema tan amplio que hasta tiene su <a href="http://www.pairprogramming.com/">propio sitio web</a>:



<img id="image183" src="/wp-content/uploads/2006/11/parproglogo.gif" alt="pair programming">

<img id="image184" src="/wp-content/uploads/2006/11/pairprogrammers.gif" alt="pair programmers">

<h2>Pruebas (de unidad)</h2>

El lenguaje de programación utilizado fue <a href="http://java.sun.com">Java</a>. También usamos un framework para mapear objetos en memoria a una base de datos relacional (<a href="http://www.hibernate.org/">Hibernate</a>) y uno para generar reportes (<a href="http://jasperreports.sourceforge.net/">JasperReports</a>). Elegimos estas herramientas por que ya las habíamos usado para un trabajo práctico previo, lo que nos permitió poner foco en la metodología y no en la herramienta.



Para trabajar con pruebas, también utilizamos un framework (<a href="http://www.junit.org/">JUnit</a>), desarrollado originalmente por Erich Gamma y Kent Beck (creador de XP). Trabajar de esta forma nos gustó muchos a todos los miembros de grupo, saber que luego de ese cambio el software sigue pasando las pruebas es alentador y refuerza uno de los valores de XP, la valentía.



Básicamente lo que hacíamos era:



1) Pensar en un método que se necesitaba.

2) Crear una prueba para ese método.

3) Correr la prueba. Fallaba.

4) Escribir código que haga pasar la prueba.

5) Correr la prueba. Si fallaba volvíamos al punto 4.



JUnit te provee de métodos parecidos a:

<code>

assertEquals(valorEsperado, valorCalculado);

</code>



Esa última línea puede fallar o puede pasar. A la vez se crea un árbol de pruebas con todas las que hallamos escrito y cuando lo ejecutamos, a medida que las pruebas van pasando una barra verde se va completando.  Si la barra se completa de color verde significa que todas las pruebas pasaron. Si alguna prueba falla, la barra se vuelve roja.



Una de las prácticas es la <strong>recodificación</strong> (esta nos ayuda a mantener un <strong>diseño simple</strong>), pero.. como recodificar y saber que no hemos cometidos errores? Luego de realizar un cambio corremos nuevamente las pruebas. Si obtenemos una barra verde estamos listos para el siguiente cambio. Rigurosamente la barra verde nos indica que el sistema sigue pasando las pruebas que antes pasaba, no que no tenga errores, pero en la práctica parece ser una buena aproximación.



<img id="image185" src="/wp-content/uploads/2006/11/junitlogo.gif" alt="JUnit">



<img id="image186" src="/wp-content/uploads/2006/11/keep.gif" alt="keep de bar green">

<img id="image187" src="/wp-content/uploads/2006/11/frogmov.gif" alt="Frog">

<h2>ClubXP</h2>

Además, como refuerzo para la <strong>Integración continua</strong> utilizamos <a href="http://subversion.tigris.org/">Subversion</a> para mantener ordenas las revisiones que ibamos haciendo del código: <a href="http://code.google.com/p/clubxp/">clubxp en code.Google</a>.

<h2>Saludo</h2>

Bueno, fue algo de lo que quería contar. En estas fechas de finalización de cursado no escribo casi nada en el blog, así que les dejo un saludo y <strong>Hasta la próxima!</strong></body></html>