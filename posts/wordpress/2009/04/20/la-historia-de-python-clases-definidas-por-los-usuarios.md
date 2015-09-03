<html><body><em>El siguiente texto es una traducción del artículo Adding Support for User-defined Classes de Guido van Rossum publicado en <a href="http://python-history.blogspot.com/" target="_blank">http://python-history.blogspot.com/</a>.</em>

<!--more-->

<h2>﻿Añadir clases definidas por los usuarios</h2>

Crease o no, las clases fueron un añadido tardío durante el primer año del desarrollo de Python, todavía en el CWI, aunque bastante antes de la primera versión pública. En cualquier caso, para entender como se añadieron las clases, ayuda saber un poco más sobre los detalles de implementación de Python.



Python está escrito en C en forma de un intérprete de código intermedio o pseudo-binario (bytecode), usando la clásica estructura de pila, junto con una colección de tipos primitivos, también implementados en C. La arquitectura subyacente usa "objetos", pero como C no soporta objetos directamente, se implementan usando estructuras de objetos y punteros a funciones. La máquina virtual Python define docenas de operaciones estándar que cada objeto debe o puede implementar (por ejemplo, <i>get_attribute</i>, <i>add</i> y <i>call</i>). 



Un objeto se representa mediante una estructura estática que contiene una serie de punteros a funciones, uno para cada operación estándar. Estos punteros son inicializados normalmente con referencias a funciones estáticas. Pero algunas operaciones son opcionales y un objeto puede dejar esas entradas apuntando a <em>NULL</em> si decide no implementar la función. En este caso, la máquina virtual o bien genera un error en tiempo de ejecución o, en determinadas circunstancias, puede que proporcione una implementación por defecto de la operación. La estructura C contiene también varios campos de datos, uno de los cuales es una referencia a la lista de métodos adicionales que son únicos para ese tipo de datos, representada como una matriz de estructuras que constan de un texto (el nombre del método) y un puntero a una función (la implementación). El enfoque a la introspección de

Python deriva de esta habilidad de hacer que la propia estructura del tipo sea accesible en tiempo de ejecución, como cualquier otro objeto.  

Un aspecto importante de esta implementación es que está completamente centrada en el lenguaje C. De hecho, todas las operaciones y los métodos estándar están implementados por funciones en C. En un principio, el interprete de <em>bytecode</em> solo soportaba llamadas a funciones escritas en Python puro y funciones o métodos implementados en C. Creo que fue mi colega Siebren van der Zee el primero en sugerir que Python debería permitir definiciones de clases similares a las de C++, que permitieran al programador crear objetos propios.



Para poder implementar estos objetos de usuario, me ceñí al diseño más simple que pude imaginar: un esquema donde los objetos de usuario se representarían por nuevos objetos que almacenarían una referencia de clase que apuntaría a un "objeto clase" compartido por todas las instancias de la misma clase, y un diccionario, bautizado "diccionario de instancia", que contendría las variables particulares de cada instancia.



En esta implementación, el diccionario de la instancia contendría los valores de las variables de cada instancia, mientras que el objeto clase contendría la información que fuera compartida entre todas las instancias de la misma clase, especialmente, los métodos. Al implementar la clase objeto opté de nuevo por el diseño más sencillo posible; el conjunto de métodos de la clase se almacenaría en un diccionario, cuyas claves serían los nombres de los métodos, con lo que se creó el diccionario de la clase. Para implementar la herencia, los objetos clase almacenarían opcionalmente una referencia a los objetos clase correspondientes a las clases base. En esa época era bastante ingenuo en lo que se refería a las clases, pero sabía que existía la herencia múltiple, que C++ había incorporado recientemente. Decidí que si iba a implementar la herencia, bien podría implementar una versión simplificada de la herencia múltiple, de forma que una clase pudiera derivar de más de una clase base.



En esta implementación, los mecanismos subyacentes que gestionaban los objetos eran en realidad muy simples. Cualquier cambio hecho a las variables, ya sea de clase o de instancia, se verían reflejados en el objeto diccionario respectivo.

Por ejemplo, asignar un valor a una variable de una instancia actualizaría su diccionario local. De igual forma, cuando buscáramos el valor de una variable de instancia de un objeto, simplemente miramos en el diccionario subyacente. Si la variable no se encuentra allí, las cosas se ponen un poco más interesantes. En ese caso, las búsquedas deben realizarse en el diccionario asociado a la clase, y si tampoco se encontrara allí, en los diccionarios de cada clase de la que derive.



Es más habitual ver este mecanismo de búsqueda de atributos en la clase del objeto, así como en sus clases antecesoras, en el caso de la búsqueda de métodos. Como se ha mencionado anteriormente, los métodos se almacenan en el diccionario de la clase, por lo que son compartidos por todas las instancias de objetos pertenecientes a dicha clase. Así, cuando se invoca un método, lo normal es que no lo encuentres en el diccionario local del objeto. En vez de eso, se busca el método en la clase del objeto, y de no encontrarse, su busca sistemáticamente por todas las clases de las que deriva hasta encontrarlo. Cada una de las clases básicas implementa el mismo algoritmo recursivo. Esto se conoce habitualmente como la regla de primero en profundidad, luego de derecha a izquierda, y ha sido el método de ordenación y selección de métodos (MRO - <em>Method Resolution Order</em>) usado por Python en la mayoría de sus versiones.

Las versiones más modernas han adoptado un MRO más sofisticado, que se discutirá en un futuro artículo de esta serie.



Al implementar las clases, uno de mis objetivos fue mantener las cosas sencillas. Así, Python no realiza comprobaciones de errores ni comprueba inconsistencias a la hora de localizar métodos. Por ejemplo, si una clase sobreescribe un método definido en una clase antecesora, no se realiza ninguna comprobación para verificar que el método redefinido tenga el mismo número de argumentos, ni que puede ser llamada de la misma manera que el método original. El algoritmo de resolución y localización de métodos se limita a devolver el primer método que encuentre, y lo ejecuta con cualesquiera argumentos que haya indicado el usuario.



A partir de este diseño emergieron otras características. Por ejemplo, aunque el diccionario de clase se pensó inicialmente como un repositorio de métodos, no existía ninguna razón que le impidiera contener también otros tipos de objetos.

Así, objetos como números enteros o cadenas de texto podían ser almacenados en el diccionario de la clase, lo que los convertía a todos los efectos en variables de clase; variables que son compartidas por todas las instancias de una determinada clase, en vez de estar almacenadas localmente.



Aunque la implementación era sencilla, también proporcionaba un alto grado de flexibilidad. Por ejemplo, la implementación hacía que las propias clases fueran objetos, en pie de igualdad con cualquier otro objeto (objetos de primera clase, o <em>first-class objects</em>, como se les suele describir en la documentación), lo que significaba que podían ser inspeccionadas de forma introspectiva en tiempo de ejecución, e incluso ser modificadas inámicamente. Se podían añadir o modificar métodos simplemente actualizando el diccionario de la clase, una vez que la clase hubiera sido creada (*). La naturaleza dinámica de Python significaba que esos cambios tendrían un efecto inmediato en todas las instancias de esa clase o de sus clases derivadas. De igual manera, se podía modificar dinámicamente objetos individuales añadiendo, modificando o borrando variables de instancia (una característica que, como comprendí posteriormente, hacía que la implementación de clases y objetos de Python fuera más permisiva que la de Smalltalk, que restringía el conjunto de atributos a aquellos especificados en el momento de la creación).



<h3>Desarrollo de la sintaxis de clases</h3>



Habiendo diseñado las representaciones en tiempo de ejecución para las clases definidas por el usuario, mi siguiente tarea era diseñar la sintaxis para las definiciones de clases, y en particular, para las definiciones de métodos dentro de la clase. Había una restricción fuerte y era que yo no quería que la sintaxis para definir métodos fuera distinta de la sintaxis para definir funciones.



Reconstruir la gramática y el generador de <em>bytecode</em> para manejar estos dos casos tan similares de forma diferente fue una tarea ardua. Aun así, aunque conseguí mantener la gramática igual, aún tenía que encontrar la manera de tratar con las variables de instancia. Inicialmente había esperado emular las variables de instancia implícitas que podemos ver, por ejemplo, en C++. En ese lenguaje, las clases se definen con un código como el siguiente:

<pre lang="cpp">

    class A {

    public:

       int x;

       void spam(int y) {

            printf("%d %d\n", x, y);

       }

    };

</pre>

En esta clase se ha declarado la variable de instancia <i>x</i>. En los métodos, las referencias a <i>x</i> se refieren implícitamente a la variable de instancia.



Por ejemplo, en el método <i>spam()</i>, no se declara la variable <i>x</i> ni como parámetro, ni como variable local, pero como la clase ha declarado una variable de instancia del mismo nombre, se asume que las referencias a <i>x</i> se refieren a dicha variable. Aunque deseaba proporcionar a Python algo similar, pronto me di cuenta de que esta aproximación sería imposible, ya que, en un lenguaje que carece de declaración de variables, no habría una manera elegante de distinguir las variables de instancia de las variables locales.



En teoría, obtener el valor de las variables de instancia debería ser bastante fácil. Python ya disponía de un orden de búsqueda predefinido para nombres de variables no cualificados: locales, globales e internas (<em>built-ins</em>).

Cada una de estas áreas estaba representada por un diccionario que mapeaba los nombres de las variables con sus valores. Cada referencia a una variable se convertía, así, en una serie de búsquedas en diccionarios que concluía cuando se encontrada el nombre de la variable. Por ejemplo, durante la ejecución de una función con una variable local <i>p</i> y una variable global <i>q</i>, en una sentencia como, por ejemplo, <i>print p, q</i> buscaría <i>p</i> en el primer diccionario, el de las variables locales, y lo encontraría. Luego buscaría <i>q</i> en ese mismo diccionario y no lo encontraría, por lo que continuaría la búsqueda por el segundo diccionario, el de las variables globales, hasta encontrarlo.



Habría sido muy fácil añadir el diccionario de instancia del objeto actual al principio de esta lista de diccionarios a la hora de ejecutar un método. De esa forma, en un método de un objeto con una variable de instancia <i>x</i> y una variable local <i>y</i>, una sentencia como <i>print x,y</i> encontraría <i>x</i> en el diccionario de la instancia (el primer diccionario según la nueva ordenación), e <i>y</i> en el diccionario de variables locales (el segundo

diccionario).



El problema con esta estrategia es que fracasa al intentar declarar los valores de las variables de instancia. La asignación en Python no busca el nombre de la variable en los diccionarios, sino que se limita a añadir o reemplazar la variable en el primer diccionario de la lista, normalmente el de variables locales. Esto provoca que las variables siempre se creen en el ámbito local, si no se especifica nada (aunque hay que hacer notar que existe una “declaración global" que invalida este comportamiento para una variable dentro de una función).



Si no cambiamos esta aproximación minimalista a la asignación, el que el diccionario de la instancia fuera el primero en la lista de búsqueda haría 

imposible asignar valores a las variables locales dentro de un método. Porejemplo, si tuviéramos un método así:

<pre>

    def spam(y):

        x = 1       

        y = 2       

</pre>

Las asignaciones a <i>x</i> e <i>y</i> sobreescribirían el valor de la variable de instacia <i>x</i> y crearían una nueva variable de instancia <i>y</i>, que impediría acceder al valor de la variable local <i>y</i>. Cambiar el orden de los diccionarios (pasar el de instacia al segundo lugar y que el diccionario 

local se convirtiera en el primero) simplemente la daría la vuelta al problema, haciendo imposible realizar asignaciones a variables de instancia.



Tampoco funcionaría cambiar la semántica de las asignaciones para usar una variable de instancia, si existe alguna, o usar una variable local en caso contrario, porque esto nos crearía un problema de auto-referencias: ¿cómo crearíamos una variable de instancia, en primer lugar? Una posible solución  podría ser obligar a declarar explícitamente las variables de instancia, de forma similar a la usada para declarar variables globales, pero no quería añadir una característica como esta, habiendo llegado tan lejos como había llegado sin requerir ninguna declaración de variables. Además, la especificación extra para indicar una variable global era un caso especial que apenas se usaba en la mayoría del código. La declaración explícita de variables de instancia, por otro lado, tendría que ser usada en prácticamente cualquier definición de clase. Otra posible solución era distinguir lexicamente las variables de instancia. Por ejemplo, usando un símbolo especial como el caracter @ (una aproximación tomada por ruby) o usando alguna convención de nombres que implicara prefijos o un uso particular de mayúsculas y minúsculas. Ninguna de estas opciones me agradaba (y sigue sin hacerlo).



En vez de esto, decidí abandonar la idea de referencias implícitas a las variables de instancia. Los lenguajes como C++ permiten escribir cosas como <i>this-&gt;foo</i>, para señalar explícitamente que la variable <i>foo</i> es de instancia, distinguiéndola así de una posible variable local <i>foo</i>. Decidí,

por tanto, hacer que la única manera de acceder a las variables de instancia fueran estas referencias explícitas. Además, tomé la decisión de que <i>this</i>, la variable que representaba al objeto actual, no fuera una palabra clave, simplemente haría que <i>this</i> (o su equivalente) fuera un primer argumento de cada método. Las variables de instancia sería siempre atributos de ese argumento.



Usando referencias explícitas, no había ninguna necesidad de tener una sintaxis especial para la definición de métodos, ni tenía uno que complicarse con semánticas adicionales para la búsqueda de variables. En vez de eso, simplemente se definía una función, sabiendo que el primer argumento correspondería con el objeto instanciado. Por convención, se suele dar a este primer argumento el nombre de <i>self</i>. Por ejemplo:

<pre>

    def spam(self,y):

        print self.x, y

</pre>



Esta aproximación recuerda algo a Modula-3, que ya me había proporcionado la sintaxis para las importaciones y para el manejo de excepciones. Modula-3 no tenía clases, pero permitía definir tipos estructurados que podían contener punteros a funciones, que eran inicializadas por defecto con funciones definidas previamente y añadía azúcar sintáctico para que, si <i>x</i> era una estructura de ese tipo y <i>m</i> un puntero a una función almacenada en dicho registro, inicializado a una función <i>f</i>, entonces llamar a <i>x.m(args)</i> equivalía a llamar a <i>f(x, args)</i>. Esto se ajusta a la implementación de objetos y métodos, y hace posible equiparar las variables de instancia con atributos del primer argumento.



El resto de los detalles de la sintaxis de Python para clases se derivan de este diseño o de las demás restricciones impuestas por la implementación. Siguiendo con mis aspiraciones de sencillez, imaginaba la sentencia <i>class</i> como una serie de definiciones de métodos, que son sintácticamente iguales a las definiciones de funciones, aun cuando se estableciera por convención que todas deberían tener un primer argumento llamado <i>self</i>. Además, en vez de desarrollar una nueva sintaxis para los métodos especiales (como los constructores y los destructores), tomé la decisión de que estos casos se resolverían obligando al usuario a utilizar nombres especiales, como <i>__init__</i>, <i>__del__</i> y demás. Esta convención de nombres se tomó del lenguaje C, en el que los identificadores que empezaban con el caracter guión bajo estaban reservados para el compilador y tenían, a menudo, significados especiales (por ejemplo, macros como __FILE__ en el preprocesador de C).



Así, la visión que tenía del código para definir una clase era esta:

<pre>

    class A:

         def __init__(self,x):

             self.x = x

         def spam(self,y):

            print self.x, y

</pre>    

También quería seguir reutilizando la máxima cantidad posible de código.

Normalmente, una definición de una función es una sentencia ejecutable que, simplemente, realiza una asignación; asigna a una variable, en el espacio de nombres local, el objeto función (el nombre de la variable será, por tanto, el nombre de la función). Se me ocurrió que, en vez de inventar una solución distinta, era razonable hacer la misma interpretación para las definiciones de métodos dentro del cuerpo de la clase, simplemente usando como espacio de

nombres un nuevo diccionario. Este nuevo diccionario sería entonces tratado y usado para inicializar el diccionario de la clase, creando de esa forma una nueva clase. Detrás de escena, la estrategia que se implementó fue convertir el cuerpo de la clase en una función anónima, que ejecutaba todas las sentencias de definición de métodos que encontrara en el cuerpo de la clase, y que terminaba devolviendo un diccionario con todas las variables/métodos definidas. Este diccionario se pasaba a una función auxiliar, que creaba la clase en sí. Finalmente, el objeto que definía la propia clase se almacenaba en una variable en el entorno local, siendo su nombre el mismo que el de la clase. 

Los usuarios de Python a menudo se sorprenden al comprender que cualquier sentencia válida de Python puede aparecer en el cuerpo de una clase. Esta característica era en realidad una extensión de mi deseo de mantener la sintaxis lo más limpia posible, a la vez que trataba de no limitar artificialmente aquellas cosas que pudieran resultar útiles.



Un detalle final acerca de la sintaxis usada para instanciar objetos de una clase. Otros lenguajes, como C++ o Java, usan para crear objetos un operador

especial, <i>new</i>. En C++ esta opción es defendible, porque los nombres de las clases tienen un estatus especial para el analizador, pero en Python eso no era así. Como el analizador de Python no se preocupa en absoluto por el tipo de objeto que esta llamando, hacer que la propia clase fuera ejecutable era la solución correcta, "mínima" en el sentido de que no requería una nueva sintaxis.

Creo que me adelanté un poco a los tiempos aquí; a día de hoy, el “patrón de diseño Factory” es a menudo el sistema más empleado para la creación de instancias y lo que yo hice fue simplemente convertir cada clase en su propia fábrica (Factory).



<h3>Métodos especiales</h3>



Como decía en la última sección, uno de los objetivos que perseguía era que la implementación de las clases fuera sencilla. En los demás lenguajes orientados a objetos, normalmente existe una diversidad de métodos y operadores especiales que sólo se aplican a las clases. Por ejemplo, en C++, hay una sintaxis especial para definir constructores y destructores, diferente de la usada para definir funciones o métodos normales.



En realidad, no quería introducir una nueva sintaxis para manejar las operaciones especiales con los objetos. Así que me las arreglé para mapear los

operadores específicos con un conjunto de nombres especiales de métodos, como <i>__init__</i> y <i>__del__</i>. Los usuarios podrían definir su propio código asociado a la creación y destrucción de objetos, simplemente definiendo métodos con estos nombres especiales.



Usé la misma técnica para permitir a los usuarios redefinir el comportamiento de los operadores de Python. Como ya se ha dicho, Python está escrito en C y usa tablas que contienen punteros a funciones para implementar diferentes capacidades de los objetos internos (por ejemplo, <i>get attribute</i>, <i>add</i> y <i>call</i>). Para permitir que el usuario pudiera definir estas mismas  capacidades en sus clases, mapeé los punteros a diferentes funciones con nombres especiales como <i>__getattr__</i>, <i>__add__</i> y <i>__call__</i>. 

Existe una correspondencia directa entre estos nombres y las tablas de punteros de funciones que uno tiene que definir cuando se implemente un nuevo tipo de objeto en C.



(*) Eventualmente, el nuevo estilo de clases hace que sea necesario controlar los cambios en el __dict__ de la clase; aún se puede modificar dinámicamente las clases, pero se debe utilizar asignación de atributos en lugar de la  variable __dict__ directamente.



<em>Traducido por Juan I. Rodriguez.

Revisado por Juan José Conti y César Portela.

Si encontrás errores en esta traducción, por favor reportalos en un comentario y los corregiremos a la brevedad.</em>

Todas las traducciones de esta serie pueden encontrarse en <a href="/categoria/aprendiendo-python/historia/" target="_self">La historia de Python</a>.</body></html>