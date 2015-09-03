<html><body><h2>PLY</h2>

<em>The asteroid to kill this dinosaur is still in orbit.

- Lex Manual Page </em>



PLY o python-ply (cómo se llama su paquete en <a title="PLY en Debian" href="http://packages.debian.org/etch/python-ply" target="_blank">Debian</a>) es una implementación de las herramientas <a title="Lex and Yacc" href="http://dinosaur.compilertools.net/" target="_blank">lex y yacc</a> para análisis léxico y sintáctico. Está enteramente escrito en <a title="Sitio oficial" href="http://www.python.org" target="_blank">Python</a> y su primera versión fue desarrollado por <a title="Autor" href="http://www.dabeaz.com/" target="_blank">David Beazley</a> en el año 2001 para ser usado en un curso de Introducción a los Compiladores.

<h3>Lex</h3>

Lex es una creador de analizadores léxicos (<em>lexers</em>). La función principal de un <em>lexer</em> es tomar un flujo de caracteres entrada y devolver un flujo de <em>tokens</em> como salida. Ejemplos de <em>tokens </em>en un programa escrito en algún lenguaje de programación podrían ser: un número, un paréntesis, un identificador o una palabra clave. Por ejemplo: <code>17,  ), miVarible, if</code>.



Para definir los tokens utilizamos <a title="RE" href="http://es.wikipedia.org/wiki/Expresi%C3%B3n_regular" target="_blank">expresiones regulares</a>.

<h3>Yacc</h3>

Yacc, <em>Yet Another Compilers Compiler</em>,  nos permitirá crear un programa que tome un flujo de <em>tokens</em> como entrada y reconozca a partir de ellos un lenguaje. Notemos por ejemplo que si bien <code>if { 555 ;; for printf i++[]</code> es un flujo de tokens válidos de C, no es una sentencia válida del lenguaje como si lo es <code>for(i=0; i&lt;5; i++){}</code>.



Para definir la gramática de un lenguaje de programación vamos a usar una notación conocida como <a title="BNF" href="http://es.wikipedia.org/wiki/Backus-Naur_form" target="_blank">BNF</a> (Backus–Naur form).

<!--more-->

<h2>MiniLisp</h2>

Intérpretes de lenguajes de programación como Python o PHP son escritos en C por razones de eficiencia. ¿Vamos a usar Python para escribir uno? Bueno.. ¿por qué no? La filosofía de Python consiste en escribir rápido una solución para un problema y poder probarla enseguida. En el tiempo en que implementás en C una idea podes escribir 3 soluciones diferentes en Python, probarlas y elegir con cual continuar. En caso de que en algún momento se detecte que el programa resultante corre lento (más lento de lo necesario), siempre podés:

<ul>

	<li>realizar optimizaciones en el código Python</li>

	<li>reescribir en C alguna parte critica del mismo.</li>

</ul>

El intérprete que voy a construir para aprender ply va a tener sabor a <a title="Lisp" href="http://en.wikipedia.org/wiki/Lisp_programming_language" target="_blank">Lisp</a> y va a ser <em>muy sencillo</em>. Va a ser un MiniLisp! En particular:

<ul>

	<li>Usará notación prefija mediante paréntesis de la forma <code>(fun-name arg [arg])</code>. Esto significa que el intérprete podrá resolver expresiones como <code>(+ 1 1)</code> y responderá <code>2</code>, <code>(= 1 1)</code> y responderá <code>#t</code> (la forma en que voy a representar el valor de verdad True), pero también <code>(+ 1 2 3 4 5)</code> que da como resultado <code>15</code> y <code>(or #t #f #f)</code> que da como resultado <code>#t</code>.</li>

	<li>Permitirá resolver expresiones anidadas. Esto significa que además de las expresiones anteriores, podrá resolver expresiones como <code>(+ 1 (+ 2 2) (- 5 4) 10)</code> que da como resultado <code>16</code>, <code>(and (= 1 1) #t)</code> que da como resultado <code>#t</code> y <code>(and (or (= (+ 10 10) 20) #f (= #t #f)) (= 13 (+ 10 1 1 1 1 (- 2 1))))</code> cuyo resultado se deja a cargo del lector para que vaya entrando en clima :)</li>

	<li>Contará con funciones de manejo de listas típicas en Lisp como car, cdr y cons:

<ul>

	<li><code>(car '(1 2 3))</code> obtiene el primer elemento (o cabeza) de la lista <code>'(1 2 3)</code>: <code>1</code></li>

	<li><code>(cdr '(1 2 3))</code> obtiene la cola de la lista <code>'(1 2 3)</code>: <code>(2 3)</code></li>

	<li><code>(cons 0 '(1 2 3))</code> crea una nueva lista con 0 como cabeza y <code>'(1 2 3)</code> como cola:<code> (0 1 2 3)</code></li>

	<li>Notar que <code>(cons '(1 2) '(3 4))</code> da como resultado una lista cuya cabeza es la lista <code>'(1 2)</code> y su cola <code>'(3 4)</code>: <code>((1 2) 3 4)</code></li>

	<li>También se podrá usar <code>(concat '(1 2) '(3 4))</code> para obtener una lista que sea la concatenación de ambas: <code>(1 2 3 4)</code></li>

	<li>y <code>(list 1 2 3 4)</code> para crear una lista de elementos: <code>(1 2 3 4)</code></li>

</ul>

</li>

	<li>La implementación tiene solo fines didácticos así que solo trabajará con enteros aunque añadir soporte para números reales (floats) debería ser fácil.</li>

	<li>No tendrá un manejo de errores muy completo.</li>

	<li>Pensé varias formas de implementar la función <code>define</code> pero no conseguí que funcione del todo bien :(, así que quité la funcionalidad.</li>

	<li>Otra función común en las implementaciones de Lisp con la que contará MiniLisp es cond, la cual evalúa su primer argumento y si es verdadero retorna el segundo. Esta función puede usarse para implementar construcciones de control de flujo más complejas como if-else, while o for. Eso si en MiniLisp se pudieran definir funciones :(

<ul>

	<li><code>(cond (= 1 1) 7)</code> retorna <code>7</code></li>

	<li>pero <code>(cond (= 1 2) 7)</code> no retorna nada.</li>

</ul>

</li>

</ul>

<h2>Manos a la obra</h2>

PLY  consiste en un paquete que contiene los módulos ply y yacc.

En Debian/Ubuntu podemos instalarlo con el comando (como root o mediante sudo)



<code>apt-get install python-ply</code>

<h3>lex.py</h3>

Al programa que generará un analizador léxico lo llamé <code>lex.py</code> y consiste en:



<code>import ply.lex as lex</code>



Debemos crear una tupla con todos los nombres de los tokens a reconocer (por convención escribimos los nombres en mayúsculas):



<pre>tokens = ('QUOTE', 'SIMB', 'NUM', 'LPAREN', 'RPAREN', 'NIL', 'TRUE', 'FALSE', 'TEXT')

</pre>



Un diccionario en el cual la clave es una palabra reservada y el valor uno de los tokens de la tupla anterior:



<pre>reserved = {

'nil' : 'NIL',

}</pre>



En este ejemplo prácticamente no hay palabras reservadas, otros lenguajes podría haber palabras como <code>if</code>, <code>while</code>, <code>for</code> o <code>return</code>.



Lo siguiente es definir las expresiones regulares para cada <em>token</em>. Existen dos formas de hacerlo, mediante strings o mediante funciones.

El primer caso se usa cuando el <em>token </em>no requiere ningún tipo de procesamiento luego de ser econtrado:



<pre>t_LPAREN = r'\('

t_RPAREN = r'\)'

t_QUOTE = r'\''

t_TRUE = r'\#t'

t_FALSE = r'\#f'</pre>



Notar que se usan raw strings de Python para escribir las expresiones regulares que posteriormente serán compiladas y usadas (PLY utiliza el módulo re en su análisis léxico).



Para los tokens correspondientes a números podemos querer hacer alguna verificación antes de devolverlo, en ese caso la especificación del token puede hacerse mediante una función:

<pre>def t_NUM(t):

    r'd+'

    try:

        t.value = int(t.value)

    except ValueError:

        print "Line %d: Number %s is too large!" % (t.lineno,t.value)

        t.value = 0

    return t</pre>

Notar que en el docstring de la función se debe colocar la expresión regular correspondiente al <em>token</em>.



Otro ejemplo de esto se da para el <em>token</em> SIMBOL, pero con una particularidad. Este <em>token</em> se usa para los nombres de funciones o variables. <code>car</code>, <code>cdr</code> o <code>and</code> son ejemplos de símbolos en MiniLisp.

<pre>def t_SIMB(t):

    r'[a-zA-Z_+=*-][a-zA-Z0-9_+*-]*'

    t.type = reserved.get(t.value,'SIMB')    # Check for reserved words

    return t</pre>

Luego de encontrar una secuencia de caracteres que corresponda con la expresión regular de los símbolos, nos fijamos que no sea una palabra reservada. Si lo es, en t.type se guardará el nombre de token correspondiente, por ejemplo 'NIL', caso contrario 'SIMB'.



Si hubiesemos especificado <code>t_NIL = r'nil'</code> en lugar de usar el diccionario <code>reserved</code>, cadenas de caracteres como <code>nillave</code> (un símbolo válido) serían interpretadas como <code>NIL</code> seguido del símbolo <code>lave</code>.



El orden en que estas definiciones son usadas es el siguiente: primero los strings en orden descendiente de la longitud de la expresión regular y luego las funciones en el orden que fueron escritas.



Archivo completo: <a title="lex" href="http://www.juanjoconti.com.ar/files/python/mini-lisp/lex.py.html" target="_blank">lex.py</a>

<h3>yacc.py</h3>

El código en el que se define la gramática del lenguaje lo puse en un archivo llamado<code> yacc.py</code>. El siguiente BNF expresa la gramática de MiniLisp (las palabras en mayúsculas representan símbolos terminales y las palabras en minúsculas símbolos no terminales), a la izquierda de la regla siempre va un único elemento y el símbolo ::= puede leer se como 'es':

<pre>exp ::= atom

exp ::= quoted_list

exp ::= call

quoted_list ::= QUOTE list

list ::= LPAREN items RPAREN

items ::= item items

items ::=

item ::= atom

item ::= list

item ::= quoted_list

item ::= call

call ::= LPAREN SIMB items RPAREN

atom ::= SIMB

atom ::= bool

atom ::= NUM

atom ::= TEXT

atom ::=

bool ::= TRUE

bool ::= FALSE

atom ::= NIL</pre>

y lo siguiente es cómo queda la gramática expresa en código. Se debe definir una función por cada una de las reglas previas (el docstring de la función corresponde a la regla). Cada función recibe como parámetro un objeto iterable (muy parecido a una lista, pero que no se comporta totalmente como tal, así que cuidado con los subíndices negativos) que contiene los valores de cada símbolo de la regla.

<pre># BNF



def p_exp_atom(p):

    'exp : atom'

    p[0] = p[1]



def p_exp_qlist(p):

    'exp : quoted_list'

    p[0] = p[1]



def p_exp_call(p):

    'exp : call'

    p[0] = p[1]



def p_quoted_list(p):

    'quoted_list : QUOTE list'

    p[0] = p[2]



def p_list(p):

    'list : LPAREN items RPAREN'

    p[0] = p[2]

    f = p[2][0]



def p_items(p):

    'items : item items'

    p[0] = [p[1]] + p[2]



def p_items_empty(p):

    'items : empty'

    p[0] = []



def p_empty(p):

    'empty :'

    pass



def p_item_atom(p):

    'item : atom'

    p[0] = p[1]



def p_item_list(p):

    'item : list'

    p[0] = p[1]



def p_item_list(p):

    'item : quoted_list'

    p[0] = p[1]



def p_item_call(p):

    'item : call'

    p[0] = p[1]



def p_call(p):

    'call : LPAREN SIMB items RPAREN'

    if DEBUG: print "Calling", p[2], "with", p[3]

    p[0] = lisp_eval(p[2], p[3])



def p_atom_simbol(p):

    'atom : SIMB'

    p[0] = p[1]



def p_atom_bool(p):

    'atom : bool'

    p[0] = p[1]



def p_atom_num(p):

    'atom : NUM'

    p[0] = p[1]



def p_atom_word(p):

    'atom : TEXT'

    p[0] = p[1]



def p_atom_empty(p):

    'atom :'

    pass



def p_true(p):

    'bool : TRUE'

    p[0] = True



def p_false(p):

    'bool : FALSE'

    p[0] = False



def p_nil(p):

    'atom : NIL'

    p[0] = None</pre>

En <a title="yacc" href="http://www.juanjoconti.com.ar/files/python/mini-lisp/yacc.py.html" target="_blank">yacc.py</a> pueden verse todos los detalles de implementación que logran hacer que esta estructura arbórea que podemos armar con yacc pueda manipularse para trabajar como un intérprete de Lisp. La implementación concreta fue hecha mediante funciones sencillas escritas en Python. Traté de mantener el <em>engine </em>del lenguaje lo más simple posible ya que el objetivo principal fue trabajar en el analizador léxico/sintáctico del mismo.



En particular destaco el uso de las listas de Python (una estructura de datos muy poderosa) como componente fundamental de este pequeño Lisp.

<h3>mini-lisp.py</h3>

Finalmente utilicé el módulo cmd (parte de la librería estándar de Python) para crear la interfaz de línea de comandos del intérprete:

<pre># -*- coding: utf-8 -*-

from yacc import yacc, lisp_str

import cmd



class MiniLisp(cmd.Cmd):

    """

    MiniLisp evalúa expresiones sencillas con sabor a lisp,

    más información en http://www.juanjoconti.com.ar

    """



    def __init__(self):

        cmd.Cmd.__init__(self)

        self.prompt = "ml&gt; "

        self.intro  = "Bienvenido a MiniLisp"



    def do_exit(self, args):

        """Exits from the console"""

        return -1



    def do_EOF(self, args):

        """Exit on system end of file character"""

        print "Good bye!"

        return self.do_exit(args)



    def do_help(self, args):

        print self.__doc__



    def emptyline(self):

        """Do nothing on empty input line"""

        pass



    def default(self, line):

        """Called on an input line when the command prefix

           is not recognized.

           In that case we execute the line as Python code.

        """

        result = yacc.parse(line)

        s = lisp_str(result)

        if s != 'nil':

            print s



if __name__ == '__main__':

        ml = MiniLisp()

        ml.cmdloop()</pre>

Con esto se logra tener algunas funcionalidades útiles como poder usar las flechas izquierda y derecha del teclado para movernos por la línea que estamos escribiendo y las flechas arriba y abajo para movernos por la historia de las expresiones que fuimos introduciendo.

<h2>Resultado</h2>

En las siguientes capturas de pantalla se ven ejemplos de MiniLisp en acción:



<em>Operaciones básicas</em>



<img src="/wp-content/uploads/2007/11/ml1a.png" alt="Minilisp 1">



<em>Manejo de listas</em>



<img src="/wp-content/uploads/2007/11/ml2a.png" alt="Minilisp 2">



<em>Ejercicio planteado al lector</em>



<img src="/wp-content/uploads/2007/11/ml3a.png" alt="Minilisp 3">



El código fuente completo de MiniLisp está empaquetado en: <a title="mini-lisp tar ball" href="http://www.juanjoconti.com.ar/files/python/mini-lisp/mini-lisp-0.1.tgz" target="_blank">mini-lisp-0.1.tgz</a>



También puede navegarse en: <a title="MiniLisp" href="http://www.juanjoconti.com.ar/files/python/mini-lisp/" target="_blank">http://www.juanjoconti.com.ar/files/python/mini-lisp/</a>

<h2>Conclusión</h2>

Si bien la implementación lograda dista mucho (en su funcionalidad) de una implementación real de Lisp, su sintaxis (aunque simple como la del propio Lisp) es lo que quería lograr y me sirvió para hacer muchas pruebas (algunos de sus resultados son reflejados en este artículo).



El objetivo de este desarrollo fue aprender PLY para poder utilizarlo en un proyecto que si bien no es un lenguaje de programación, se le parece en la necesidad de realizar un análisis léxico/sintáctico: un probador de teoremas (<a title="ATP" href="http://en.wikipedia.org/wiki/Automated_theorem_proving" target="_blank">ATP</a>).

<h2>Referencias</h2>

Desde el <a title="PLY home" href="http://www.dabeaz.com/ply/" target="_blank">sitio web de ply</a> se puede acceder a su <a title="PLY doc" href="http://www.dabeaz.com/ply/ply.html" target="_blank">documentación</a>.



Sobre compiladores: <a title="Compiladores" href="http://en.wikipedia.org/wiki/Compilers:_Principles,_Techniques,_and_Tools" target="_blank">Compiladores: técnicas, principios y herramientas</a>.



<h2>Update: unas palabras sobre reducción</h2>

Supongamos que la expresión que se analizará sintácticamente (ya pasó por el analizador léxico, es decir que consiste de tokens válidos) es: (= (+ 1 1) 2).



En base a las reglas BNF definidas, esta expresión puede verse como el siguiente árbol:



<center>

<img src="/wp-content/uploads/2007/11/mlexpr2.png">

</center>



La expresión se va resolviendo de abajo hacia arriba en el árbol (o lo que es lo mismo de adentro hacia afuera en la expresión) mediante la aplicación de las funciones definidas. </body></html>