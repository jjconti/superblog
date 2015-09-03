<html><body><p>Hace unos años escuché una charla de <a href="http://pupeno.com/" target="_blank">Pupeno</a> titulada "Lips, un lenguaje diferente". Fue una charla muy interesante y realmente logró sorprender a muchos de la audiencia con distintas características de Lisp.



Sin embargo, creo que <a href="http://www.lisp.org" target="_blank">Lisp</a> no es <em>tan</em> diferente a otros lenguajes. Ok, se basa en un paradigma (el <a href="http://en.wikipedia.org/wiki/Functional_programming" target="_blank">funcional</a>) distinto al que se basa la mayoría (lideran los rankings el <a href="http://en.wikipedia.org/wiki/Procedural_programming" target="_blank">paradigma procedural</a> y el <a href="http://en.wikipedia.org/wiki/Object-oriented_programming" target="_blank">paradigma orientado a objetos</a>). Pero aún así, no está tan lejos. De hecho, muchos lenguajes de programación <a title="ver sección What Made Lisp Different" href="http://www.paulgraham.com/icad.html" target="_blank">tienden a Lisp</a>.



Prolog es el lenguaje más conocido, y otros prácticamente no se mencionan, del <a href="http://en.wikipedia.org/wiki/Logic_programming" target="_blank">paradigma lógico</a>. No es un paradigma imperativo (como los anteriormente mencionados) en el cual debemos decirle a la computadora <em>cómo</em> resolver un problema (poné en esta variable este valor multiplicado por dos, iterá hasta que n sea igual a 10, etc...) sino que es un paradigma declarativo: simplemente se plantean afirmaciones sobre los objetos y sus relaciones.



Un programa Prolog está compuesto de dos partes: una base de conocimiento + consultas contra esta. Ambas partes se escriben utilizando la misma sintaxis. Una vez que se tiene escrita la base de conocimientos, esta es compilada o interpretada y ya está lista para qué se realicen consultas contra ella.



Los siguientes son 3 ejemplos básicos de programas Prolog.

</p><h3>Base de conocimiento familiar</h3>

Vamos a utilizar Prolog para armar una base de conocimiento con relaciones familiares. Empezamos con hechos; se expresan las relaciones <code>padre</code> y <code>madre</code>:

<pre lang="prolog">padre(raul, juanjo).

padre(raul, marisu).

madre(susana, juanjo).

madre(susana, marisu).

madre(nieve, raul).</pre>

Y una regla, que se lee: X es abuela de Y si X es madre de Z y Z es madre de Y ó X es padre de Y.

<pre lang="prolog">abuela(X, Y) :- madre(X, Z), madre(Z, Y).

abuela(X, Y) :- madre(X, Z), padre(Z, Y).</pre>

Con esta base definida, podemos compilarla y hacerle consultas. ¿De quiénes es padre raul?

<pre lang="prolog">?- padre(raul, X).

X = juanjo ;

X = marisu.</pre>

¿Quién es abuela de quién?

<pre lang="prolog">?- abuela(X,Y).

X = nieve,

Y = juanjo ;

X = nieve,

Y = marisu.</pre>

<em>nota: por lo general, la interfaz de Prolog nos da la primer respuesta que encuentra y con <code>;</code> le pedimos la siguiente.</em>

<h3>Factorial</h3>

Definir un predicado que calcule el factorial de un número es bastante directo en Prolog. Si tenés que explicar la función factorial a alguien le decís: el factorial de 0 es 1. El factorial de N es N por el factorial de N - 1. Escribimos eso en Prolog:

<pre lang="prolog">factorial(0, 1) :- !.

factorial(N, F) :- N1 is N - 1, factorial(N1, F1), F is N*F1.</pre>

Con este programa compilado, podemos hacer las siguientes consultas:

<pre lang="prolog">?- factorial(0, N).

N = 1.

?- factorial(6, N).

N = 720.

?- factorial(6, 555).

false.</pre>

Podemos pedir el factorial de un número e indicar la variable dónde obtener la respuesta o consultar con un predicado sin variables (ground) y obtener como respuesta el valor de verdad de la misma.

<h3>Concatenar listas</h3>

Un tipo de dato poderoso que incorpora Prolog son las listas. Podemos definir un predicado que concatene listas. Lo vamos a llamar concatenar y tendrá 3 argumentos: las dos listas a concatenar y el resultado de la operación. Luego podremos usar el predicado de esta forma:

<pre lang="prolog">?- concatenar([1,2], [4,5,6], L).

L = [1, 2, 4, 5, 6].



?- concatenar(X, Y, [4,5,6]).

X = [],

Y = [4, 5, 6] ;

X = [4],

Y = [5, 6] ;

X = [4, 5],

Y = [6] ;

X = [4, 5, 6],

Y = [] ;

false.</pre>

Definir este predicado en Prolog es muy sencillo:

<pre lang="prolog">concatenar([],L,L).

concatenar([X|L1],L2,[X|L3]):-concatenar(L1,L2,L3).</pre>

Tiene dos partes y se lee así:

Concatenar la lista vacía con L, da como resultado L.

Concatenar una lista cuya cabeza es X y cola L1 con L2, da como resultado la lista de cabeza X y cola L3 SI el resultado de concatenar L1 con L2 es L3.

<h3>Fin del tour</h3>

Este fue un tour acelerado por Prolog, tuvo como objetivo mostrárselo a quienes no lo conocen, dejarles el gusto en la boca y ganas de mas. ¿Lo logré? ¿No conocías Prolog? ¿Qué pensás ahora?

<h3>Tutoriales y otros enlaces</h3>

<ul>

	<li><a href="http://www.cse.unsw.edu.au/~billw/prologdict.html">Prolog Dictionary</a></li>

	<li><a href="http://www.amzi.com/AdventureInProlog/a1start.htm" target="_blank">Aprendé Prolog programando un juego!</a></li>

	<li><a href="http://www.csupomona.edu/~jrfisher/www/prolog_tutorial/" target="_blank">Un gran tutorial</a></li>

</ul>

<h3>Notas</h3>

<ul>

	<li>Conocí Prolog cursando Paradigmas de Programación, una materia de segundo año de Ingeniería en Sistemas de Información</li>

	<li>Este no es mi primer post exclusivo sobre Prolog, de hecho <a href="http://www.juanjoconti.com.ar/2005/09/24/el-capitan-julio-cesar/" target="_blank">es el segundo</a>.</li>

	<li>Podés conocer más sobre Prolog <a href="http://stackoverflow.com/questions/tagged/prolog" target="_blank">leyendo preguntas y respuestas en StackOverflow.com</a></li>

</ul></body></html>