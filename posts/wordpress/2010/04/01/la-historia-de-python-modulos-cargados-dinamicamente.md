<html><body><em>El siguiente texto es una traducción del artículo Dynamically Loaded Modules de Guido van Rossum publicado en <a href="http://python-history.blogspot.com/" target="_blank">http://python-history.blogspot.com/</a>.</em>

<!--more-->

<h2>Módulos cargados dinámicamente</h2>

La arquitectura de Python permitió, desde un principio, escribir módulos de extensión escritos en C de una forma sencilla.  Sin embargo, en los primeros días, la tecnología de carga dinámica era tan oscura que las extensiones tenían que ser enlazadas estáticamente en el interprete de Python, en tiempo de compilación. Para hacer esto, lo módulos de extensión tenían que ser agregados a un script de shell  que era usado para generar el Makefile para Python y todos su módulos de extensión.



Aunque este enfoque funcionaba para pequeños proyectos, la comunidad de Python comenzó a producir nuevos módulos de extensión a un ritmo no esperado, y demandaban que los módulos pudiesen ser compilados y cargados en forma separada. Poco después, las interfaces a las APIs de enlace dinámico, propias de cada plataforma, permitieron que la declaración import busque una biblioteca compartida en disco, de forma similar que un archivo ".py". La primera mención de la carga dinámica en los logs del CVS, data de enero de 1992 y el soporte para la mayoría de las plataformas llego a fines de 1994.



El soporte de enlace dinámico probó ser muy útil, pero fue una pesadilla de mantener. Cada plataforma usaba una API diferente y algunas plataformas tenían adicionales. En enero de 1995, el soporte para enlace dinámico fue reestructurado, de forma tal que todo el código fue concentrado en un solo archivo fuente. Sin embargo, este enfoque resulto en un largo archivo abarrotado de directivas condicionales de compilación (#ifdef). En diciembre de 1999, fue reestructurado de nuevo, con la ayuda de Greg Stein, para que el código correspondiente a cada plataforma quede ubicado en un archivo específico para cada una (o familia de estas).



Aunque Python soportaba la carga dinámica de módulos, el procedimiento para construirlos, a menudo seguía siendo un misterio para muchos usuarios. Un número cada vez más grande de usuarios fueron construyendo módulos, especialmente con la introducción de herramientas como SWIG. No obstante, un usuario deseoso de distribuir un modulo de extensión enfrentaba grandes obstáculos para lograr que el modulo compile en todas las combinaciones de plataformas, compiladores y linkers. En el peor escenario posible, un usuario tenía que escribir su propio Makefile y script de configuración para establecer los flags correctos para el compilador y el linker. Además, requería que los usuarios finales tuviesen una distribución de Python con el código fuente.



Finalmente, se creo una herramienta para construir las extensiones, llamada distutils, que permitió construir e instalar los módulos de extensión en cualquier plataforma. Las opciones necesarias para el linker y el compilador están escritas desde el makefile de Python a un archivo de datos, que es consultado por distutils cuando construye módulos de extensión. Escrito en gran parte por  Greg Ward, las primeras versiones de distutils fueron distribuidas en forma separada, para dar soporte a versiones viejas de Python. Desde Python 1.6 está integrado en las distribuciones, como un modulo de la biblioteca estándar.



Cabe destacar que distutils hace mucho mas que simplemente construir módulos de extensión desde código fuente en C. Puede también instalar módulos y paquetes de Python puro, crear instaladores ejecutables para Windows y correr herramientas de terceros como SWIG. Desgraciadamente, su complejidad ha causado que sea maldecida por mucha gente y no reciba la atención que se merece a la hora de mantenerla. Como resultado, recientemente, las alternativas de terceros ( especialmente ez_install, también llamada "eggs") se hicieron mas populares, desgraciadamente causando fragmentación en la comunidad de desarrolladores, así como quejas cuando no funcionan. Parece que el problema en toda su generalidad es inherentemente difícil.

<em>Traducido por <a href="http://www.joaclandia.com.ar/" target="_blank">Joaquín Sorianello</a>.

Revisado por Juan José Conti.

Si encontrás errores en esta traducción, por favor reportalos en un comentario y los corregiremos a la brevedad.</em>

Todas las traducciones de esta serie pueden encontrarse en <a href="/categoria/aprendiendo-python/historia/" target="_self">La historia de Python</a>.</body></html>