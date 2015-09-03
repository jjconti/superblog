<html><body><p>El viernes por la tarde salí del trabajo y me fuí a escuchar la charla de <a href="http://ballardini.com.ar/blog/" target="_blank">César Ballardini</a>, <em>El modelo de objetos de Ruby, reflexiones sobre la reflexión</em>. La daba en el marco del evento <strong>acts_as_rubylit</strong>, el cual se llevó a cabo en la <a title="FICH" href="http://fich.unl.edu.ar/" target="_blank">Facultad de Ingeniería y Ciencias Hídricas, Universidad Nacional del Litoral</a> de la ciudad de Santa Fe.



Nunca antes vi nada de Ruby. Bueno, <a href="http://www.juanjoconti.com.ar/2008/11/30/primer-experiencia-con-ruby/" target="_blank">casi</a>, pero la última vez no pasé <a href="http://www.holamundo.es/lenguaje/ruby/">del Hola Mundo</a>!<img class="alignright size-medium wp-image-1965" title="juanjo_ruby_800" src="/wp-content/uploads/2009/12/juanjo_ruby_800-300x225.jpg" alt="juanjo_ruby_800" width="300" height="225">



César empezó su charla explicando la <a href="http://c2.com/cgi/wiki?BlubParadox" target="_blank">Paradoja de Blub</a>, de <a href="http://www.paulgraham.com/avg.html" target="_blank">Paul Graham</a>. Blub es un lenguaje de programación hipotético. No es el lenguaje de programación más poderoso, pero tampoco es Cobol o lenguaje de máquina. Un programador Blub está parado más o menos en el medio de la ladera de una montaña; hacia abajo están los lenguajes menos poderosos que Blub, él se da cuenta de esto, por supuesto, a todos esos lenguajes le faltan distintas características que nuestro programador usa en Blub para resolver sus problemas. En cambio, cuando mira para arriba (y ve lenguajes más poderosos que Blub), en realidad no se da cuenta que está mirando <em>hacia arriba</em>, simplemente piensa que está mirando a unos locos, hippies de pelos parados haciendo cosas raras. Cuando los programadores que están más arriba en la montaña miran hacia Blub se pregunta, ¿cómo puede alguien estar usando Blub? Ni siquiera tiene la funcionalidad X tan útil para resolver Y!



Por inducción se concluye que solo el programador que esté en la punta de la montaña, es decir el que conoce el lenguaje más poderoso, es capaz de distinguir las distintas posibilidades que se tienen con diferentes lenguajes. El programador Blub no puede verlo, por lo que solo sabe pensar en Blub, no se a enfrentado a problemas que le permitan pensar diferente.



La moraleja de la historia es que uno debería aprender lenguajes que lo obliguen a cambiar su forma de pensar y de resolver problemas (<a title="Epigram 19" href="http://www-pu.informatik.uni-tuebingen.de/users/klaeren/epigrams.html" target="_blank">Alan J. Perlis</a>).



Con esto terminó la primera parte de la charla, luego César hizo una explicación de pizarrón sobre qué es la<a href="http://en.wikipedia.org/wiki/Object-oriented_programming" target="_blank"> Programación Orientada a Objetos</a> ( y escribió con su fibrón: un objeto tiene Identidad, encapsula Estado y define Comportamiento). Según César, es un error que en la enseñanza de la POO se empiece por las Clases. ¿En qué parte de "Programación Orientada a Objetos" dice "Clase"? Las clases son <strong>solo una forma</strong> de crear objetos, pero hay muchas otras. Por ejemplo, <a href="http://en.wikipedia.org/wiki/Prototype-based_programming#Languages" target="_blank">existen muchos lenguajes OO basados en prototipos</a>, como JavaScript.



<strong>Después de haber shockeado a la audiencia desarrollando estas dos ideas en un tono casi de declaración de principios, estábamos listos para ver cómo el Modelo de Objetos de Ruby podía cambiar nuestra forma de pensar.</strong>

Lo que sigue no son los ejemplos exactos que desrrolló César con su notebook, solo los que recuerdo. Mezclo los recuerdos de su sesión interactiva de Ruby con mi propio camino de aprendizaje, que arranca ni siquiera teniendo el intérprete instalado :)

<!--more-->

Para empezar los ejemplos, tipeó en la terminal

</p><pre lang="bash">irb</pre>

. Hice lo mismo, pero no estaba instalado, por lo que instalé ese paquete y presté atención a sus dependencias:

<code>juanjo@fenix:~$ irb

<strong>El programa «irb» no está instalado actualmente</strong>.  Puede instalarlo escribiendo:

sudo apt-get install irb

bash: irb: orden no encontrada

juanjo@fenix:~$ <strong>sudo apt-get install irb</strong>

[sudo] password for juanjo:

Leyendo lista de paquetes... Hecho

Creando árbol de dependencias

Leyendo la información de estado... Hecho

Se instalarán los siguientes paquetes extras:

  irb1.8 libreadline-ruby1.8 <strong>ruby1.8</strong>

Paquetes sugeridos:

  ruby1.8-examples rdoc1.8 ri1.8

Se instalarán los siguientes paquetes NUEVOS:

  irb irb1.8 libreadline-ruby1.8 ruby1.8

0 actualizados, 4 se instalarán, 0 para eliminar y 0 no actualizados.

Necesito descargar 119kB de archivos.

Se utilizarán 664kB de espacio de disco adicional después de esta operación.

¿Desea continuar [S/n]?

Des:1 http://ar.archive.ubuntu.com jaunty-updates/main ruby1.8 1.8.7.72-3ubuntu0.1 [24,0kB]

Des:2 http://ar.archive.ubuntu.com jaunty-updates/universe libreadline-ruby1.8 1.8.7.72-3ubuntu0.1 [10,4kB]

Des:3 http://ar.archive.ubuntu.com jaunty-updates/universe irb1.8 1.8.7.72-3ubuntu0.1 [79,1kB]

Des:4 http://ar.archive.ubuntu.com jaunty/universe irb 4.2 [5138B]

Descargados 119kB en 2s (58,0kB/s)

Seleccionando el paquete ruby1.8 previamente no seleccionado.

(Leyendo la base de datos ...

248649 ficheros y directorios instalados actualmente.)

Desempaquetando ruby1.8 (de .../ruby1.8_1.8.7.72-3ubuntu0.1_i386.deb) ...

Seleccionando el paquete libreadline-ruby1.8 previamente no seleccionado.

Desempaquetando libreadline-ruby1.8 (de .../libreadline-ruby1.8_1.8.7.72-3ubuntu0.1_i386.deb) ...

Seleccionando el paquete irb1.8 previamente no seleccionado.

Desempaquetando irb1.8 (de .../irb1.8_1.8.7.72-3ubuntu0.1_all.deb) ...

Seleccionando el paquete irb previamente no seleccionado.

Desempaquetando irb (de .../apt/archives/irb_4.2_all.deb) ...

Procesando disparadores para man-db ...

Procesando disparadores para menu ...

Configurando ruby1.8 (1.8.7.72-3ubuntu0.1) ...

Configurando libreadline-ruby1.8 (1.8.7.72-3ubuntu0.1) ...

Configurando irb1.8 (1.8.7.72-3ubuntu0.1) ...



Configurando irb (4.2) ...

Procesando disparadores para menu ...</code>NAME

       irb1.8 - interactive ruby



SYNOPSIS

       irb [options]



DESCRIPTION

<strong>       irb stands for ‘interactive ruby’. irb is a tool to execute interactively ruby expressions read from stdin.  Use of irb is easy if

       you know ruby.  Executing irb, prompts are displayed as follows. Then, enter expression of ruby. A input is executed  when  it  is

       syntacticaly completed</strong>.

Ahora si puedo empezar!

<h2>Objetos y mensajes</h2>

Un lenguaje OO consta de objetos y mensajes entre objetos. Algunas veces los mensajes están un poco camuflados, pero siempre están ahí:

<pre lang="ruby" escaped="true">irb(main):001:0&gt; 1 + 2

=&gt; 3

irb(main):002:0&gt; 1.+ 2

=&gt; 3

irb(main):003:0&gt; 1.+(2) # para los lisperos que extrañan los paréntesis

=&gt; 3</pre>

<h2>Identidad</h2>

Enviando el mensaje

<pre>object_id</pre>

, podemos preguntarle su identidad a un objeto:

<pre lang="ruby" escaped="true">irb(main):001:0&gt; 1.object_id

=&gt; 3

irb(main):002:0&gt; "hola".object_id

=&gt; -605926728</pre>

<h2>Clases</h2>

Enviando el mensaje

<pre lang="ruby" escaped="true">class</pre>

a un objeto, podemos preguntarle quién es su clase:

<pre lang="ruby" escaped="true">irb(main):005:0&gt; 1.class

=&gt; Fixnum

irb(main):006:0&gt; 1.class.class

=&gt; Class

irb(main):007:0&gt; 1.class.class.class

=&gt; Class</pre>

Podemos ver que la clase Fixnum es una instancia de la clase Class; y la clase Class también es instancia de la clase Class.

Enviando el mensaje

<pre lang="ruby" escaped="true">superclass</pre>

a una clase, podemos saber cual es su superclase, es decir, qué clase extiende.

<pre lang="ruby" escaped="true">irb(main):010:0&gt; 1.class.superclass

=&gt; Integer

irb(main):011:0&gt; 1.class.superclass.superclass

=&gt; Numeric

irb(main):012:0&gt; 1.class.superclass.superclass.superclass

=&gt; Object</pre>

Luego, la clase de Object es obviamente Class, pero... ¿cuál es su superclase?

<pre lang="ruby" escaped="true">irb(main):019:0&gt; 1.class.superclass.superclass.superclass

=&gt; Object

irb(main):020:0&gt; 1.class.superclass.superclass.superclass.superclass

=&gt; nil</pre>

Creo recordar que en SmallTalk también era así. Parece un chiste de los diseñadores :) nil ni siquiera es una clase:

<pre lang="ruby" escaped="true">irb(main):021:0&gt; 1.class.superclass.superclass.superclass.superclass.superclass

NoMethodError: undefined method `superclass' for nil:NilClass

	from (irb):21

	from :0

irb(main):022:0&gt; 1.class.superclass.superclass.superclass.superclass.class

=&gt; NilClass

irb(main):023:0&gt; 1.class.superclass.superclass.superclass.superclass.class.superclass

=&gt; Object

irb(main):024:0&gt; 1.class.superclass.superclass.superclass.superclass.class.class

=&gt; Class</pre>

y la jerarquía de clases se cierra. Es para leer tranquilo y pensarlo.



El resto de la charla abarcó varias cosas más, pero creo que sería demasiado para desarrollarlo en un post y lo que mostré ya es suficiente para abrirle el apetito a los que estén buscando algún lenguaje para aprender y les produzca un cambio en su forma de pensar :). Si César postea sus ejemplos, los voy a estar referenciando desde aquí o voy a intentar hacer uno o dos posts más.



Gracias al <a href="http://www.rubylit.com.ar" target="_blank">Grupo de Usuarios de Ruby del Litoral</a> por organizar el evento!</body></html>