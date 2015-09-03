<html><body><p>Esta semana se publicó la versión beta del sitio web <a href="https://thewalnut.io/" target="_blank">thewalnut.io</a> (creado por amigos de <a href="http://www.machinalis.com/" target="_blank">#machinalis</a>). El sitio permite visualizar graficamente algoritmos y compartirlos con otros usuarios. Es una herramienta de aprendizaje y de comunicación. Una puede comunicar una idea de forma gráfica más fácil que con palabras o pseudocódigo. Y puede basarse en lo que otro construyó para experimentar, modificando, y así crear conocimiento.

</p><h2>En concreto</h2>

Ir de cero a la visualización de un algoritmo cualquiera no es trivial; es necesario llevar a cabo cuatro pasos:

<ol>

	<li><a href="https://thewalnut.io/doc/environment-design/#defworlds" target="_blank">Describir un mundo</a>: esto se hace mediante un DSL y require definir el estado del mundo (se hace con el keyword <strong>state</strong> y puede ir desde una variable booleana a una estructura de datos compleja), definir los roles para los agentes que interactuarán con el mundo (se hace con el keyword <strong>role</strong>, definiendo un sensor y actuadores), definir una función performance (no la estuve usando) y una función de fin de condición (le di el valor False porque quería hacer una simulación sin fin).</li>

	<li><a href="https://thewalnut.io/doc/agent-design/" target="_blank">Escribir un agente</a> que interactúe con ese mundo: se puede hacer con Python3 o JavaScript. <strong>En el agente va la lógica para definir qué actuador se ejecuta ante cierta percepción del mundo</strong>.</li>

	<li>Plantear problemas para ese agente: se hace mediante una interfaz gráfica. Esto incluye principalmente el estado inicial del mundo.</li>

	<li><a href="https://thewalnut.io/doc/visualization-definition-language/" target="_blank">Escribir un visualizador</a>: al igual que el mundo, se describe mediante un DSL propio.</li>

</ol>

Para lograr entender lo anterior, hice mi propio ejemplo desde cero. El objetivo era entender todas las partes y completarlo en un día.

<h2>El juego de la vida</h2>

1) Creé un <a href="https://thewalnut.io/simulations/edit_world/293/" target="_blank">mundo genérico para autómatas celulares</a>.



2) Escribí un <a href="https://thewalnut.io/simulations/edit_agent/347/" target="_blank">agente</a> (no muy optimizado) que implemente el algoritmo del Juego de la vida de Conway (usando Python3; también se puede usar JavaScript).



3) Planteé el problema más sencillo que se me ocurrió, <a href="https://thewalnut.io/simulations/edit_problem/348/" target="_blank">Blinker (Parpadeador)</a>.



4) Escribí un <a href="https://thewalnut.io/simulations/edit_visualization/969/" target="_blank">visualizador</a> para <a href="https://thewalnut.io/visualizer/visualize/3397/969/" target="_blank">visualizarlo</a>.



Logre hacerlo funcionar luego de varias iteraciones.



Con esto andando, implementar cualquier patrón fue fácil.

<ul>

	<li><a href="https://thewalnut.io/simulations/edit_problem/359/" target="_blank">Toad (Sapo)</a> - <a href="https://thewalnut.io/visualizer/visualize/3402/969/" target="_blank">visualizarlo</a></li>

	<li><a href="https://thewalnut.io/simulations/edit_problem/360/" target="_blank">Glider (Deslizador)</a> - <a href="https://thewalnut.io/visualizer/visualize/3417/969/" target="_blank">visualizarlo</a></li>

</ul>

<img class="aligncenter size-full wp-image-5367" src="/wp-content/uploads/2015/07/conwayglider.gif" alt="Gilder" width="622" height="622">



Lo siguiente fue jugar cambiando las reglas originales creando un <a href="https://thewalnut.io/simulations/edit_agent/361/" target="_blank">nuevo agente</a>:



<a href="/wp-content/uploads/2015/07/celularautomata.gif"><img class="aligncenter size-full wp-image-5366" src="/wp-content/uploads/2015/07/celularautomata.gif" alt="celularautomata" width="622" height="622"></a>

<h2>Fork</h2>

El círculo se completó cuando alguien (<span class="s1"><a href="https://twitter.com/rodolfoedelmann" target="_blank">redelmann</a></span>) hizo un <a href="https://thewalnut.io/simulations/edit_world/306/" target="_blank">fork de mi mundo</a>, planteó un <a href="https://thewalnut.io/simulations/edit_problem/381/" target="_blank">nuevo problema</a>, cambió el agente para que tenga una <a href="https://thewalnut.io/simulations/edit_agent/363/" target="_blank">nueva propiedad</a> y escribió un <a href="https://thewalnut.io/simulations/edit_visualization/984/" target="_blank">nuevo visualizador</a> (<a href="https://thewalnut.io/visualizer/visualize/3507/984/" target="_blank">visualizarlo</a>):



<a href="/wp-content/uploads/2015/07/celularautomata2.gif"><img class="aligncenter size-full wp-image-5371" src="/wp-content/uploads/2015/07/celularautomata2.gif" alt="Forkeado" width="622" height="622"></a>En este momento, en el sitio es un poco confusa la forma de correr simulaciones y forkear mundos y termina habiendo muchas copias con con nombres repetidos, pero confío en que el caos se va a ordenar pronto.</body></html>