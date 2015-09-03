<html><body><p>Uso <a href="http://www.swi-prolog.org/" target="_blank">SWI-Prolog</a>, una de las implementaciones más potentes y populares del lenguaje. Para Windows, está disponible un <a href="http://lakk.bildung.hessen.de/netzwerk/faecher/informatik/swiprolog/indexe.html" target="_blank">entorno de desarrollo</a> compuesto básicamente por:

</p><ul>

	<li>Un panel dónde escribir código con resaltado de sintáxis.</li>

	<li>Botones para hacer cosas como consultar el archivo que estamos editando (esto es compilarlo y cargarlo en memoria para poder hacer consultas sobre él).</li>

	<li>Un panel dónde realizar consultas.</li>

</ul>

En los sistemas operativos basados en Linux (como Ubuntu) no existe un entorno similar. Los programadores full-time Prolog <a href="http://lakk.bildung.hessen.de/netzwerk/faecher/informatik/swiprolog/indexe.html" target="_blank">deben tener su forma de solucionarlo</a>. Yo encontré la mía. Puede no ser la mejor, pero es más cómoda que tipear por un lado, tener el intérprete abierto por otro e ir consultando luego de cada modificación.



De hecho, la misma implementación trae algunas primitivas útiles que se pueden usar desde el lenguaje. Por ejemplo:

<pre lang="prolog">?- consult('cats.pdb').

% cats.pdb compiled 0.01 sec, 1,664 bytes

true.</pre>

compilará el archivo cats.pdb y los hechos y reglas definidos en él estarán disponibles para nuestras consultas. Si modificamos el archivo fuente, luego debemos hacer:

<pre lang="prolog">?- reconsult('cats.pdb').

% cats.pdb compiled 0.00 sec, 0 bytes

true.</pre>

para que las modificaciones tengan efecto. Encontré otro predicamo muy útil:

<pre lang="prolog">?- edit('cats.pdb').

% Waiting for editor ...

% Running make to reload modified files

% /home/juanjo/prolog/cats.pdb compiled 0.00 sec, 124 bytes

% Scanning references for 1 possibly undefined predicates

true.</pre>

Abrirá el editor por defecto configurado en la computadora, nos permitirá editar el archivo y cuando lo guardemos retorna true al intérprete. Ahora lo que antes hacíamos a mano, podemos hacerlo desde el intérprete. Un avance, pero se pone mejor: podemos usar estos predicados Prolog para escribir una regla que haga todo por nosotros. Yo uso:

<pre lang="prolog">myedit(File) :-

edit(File), reconsult(File).

myedit(File) :-

edit(file(File)), reconsult(File).</pre>

¿Cómo funciona? Primero notemos que son dos reglas. La primera recibe un nombre de archivo e intenta editarlo, si el archivo existe se abre el editor, editamos, cuando lo guardamos edit(File) evalúa true y se pasa al siguiente hecho que reconsulta el archivo y listo.



Si el archivo no existe, la primer regla no termina y se pasa a la segunda. file(File) se encarga de crearlo y edit podrá editarlo, trabajamos y todo termina como en el caso anterior.



Podemos escribir este código en el archivo .plrc de nuestra home para que sea cargado al iniciar el intérprete. Finalmente si utilizamos la extensión .pdb, vim se encarga de cargar el resaltado correspondiente a la sintácis de Prolog.</body></html>