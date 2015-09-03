<html><body><em>El siguiente texto es una traducción del artículo Personal History - part 2, CNRI and beyond de Guido van Rossum publicado en <a href="http://python-history.blogspot.com/" target="_blank">http://python-history.blogspot.com/</a>.</em>



<!--more-->

<h2>Historia Personal - parte 2, CNRI y más</h2>

Luego del workshop de Python (ver artículo anterior) obtuve una oferta de trabajo para venir a trabajar en agentes móviles en el CNRI (Corporation for National Research Initiatives). CNRI es un laboratorio de investigación sin fines de lucro en Reston, Virginia. Me uní en abril de 1995. El director del CNRI, Bob Kahn, fue el primero en señalarme cuánto tenía Python en común con Lisp, a pesar de ser completamente diferentes en un nivel superficial (sintaxis). El trabajo en Python en el CNRI fue financiado indirectamente por un subsidio de DARPA para investigación en agentes móviles. A pesar de que había apoyo de DARPA para proyectos que usaban Python, no había mucho apoyo directo para el desarrollo del lenguaje en si.



En el CRNI, lideré y ayudé a contratar a un pequeño grupo de desarrolladores para construir un agente móvil enteramente en Python. Los miembros iniciales del equipo fueron Roger Masse y Barry Warsaw, quienes habían sido mordidos por el bichito de Python en el Python workshop del NIST.  Además, contratamos a los miembros de la comunidad de Python Ken Manheimer y Fred Drake. Jeremy Hylton, un graduado del MIT contratado originalmente para trabajar en recuperación de texto, también se unió al equipo. Este fue dirigido originalmente por Ted Strollo y luego por Al Vezza.



El equipo me ayudó a crear y mantener elementos adicionales de la infraestructura de la comunidad de Python como el sitio web python.org, el servidor CVS y las listas de correo para varios grupos de intereses especiales en Python. Las versiones de la 1.3 a 1.6 fueron publicados desde el CNRI. Por muchos años, Python 1.5.2 fue la versión más popular y estable.



GNU mailman también nació aquí: originalmente usábamos una herramienta escrita en Perl llamada Majordomo, pero Ken Manheimer encontró que era inmantenible y buscó una solución en Python. Encontró algo escrito en Python por John Viega y tomo su mantenimiento. Cuando Ken dejó el CNRI para ir a Digital Creations, Barry Warsaw lo tomó y convenció a la Free Software Foundation de adoptarlo como su herramienta oficial para listas de correo. Barry entonces la licenció bajo la GPL (GNU Public License).



El Python workshops continuó, al principio dos veces al año, pero debido al crecimiento y los esfuerzos en logística cada vez mayores pronto se convirtió en un evento anual. Estos era llevados a cabo al principio por cualquiera que quería alojarlos, como el NIST (el primero), USGS (el segundo y el tercero) y LLNL (el cuarto y el comienzo de la serie anual). Eventualmente, CNRI tomó la organización, y luego (junto a las conferencias de la WWW y de IETF) se separó como una iniciativa comercial, Fortec. La audiencia pronto llegó a varios miles. Cuando Fortec se desvaneció un poco después de que dejé el CNRI, la Python Conference empezó a desarrollarse dentro de OSCON (O'Reilly's Open Source Conference), pero al mismo tiempo la Python Software Foundation (ver abajo) empezó una nueva serie de conferencias populares llamada PyCon.



También creamos la primer (hoy inexistente) organización alrededor de Python en el CNRI. En respuesta a los esfuerzos de Mike McLay y Paul Everitt de crear una "Python Foundation", que terminó en las arenas movedizas de borradores de estatutos, Bob Kahn se ofreció a crear la "Python Software Activity", que no sería una entidad legal independiente, sino simplemente un grupo de personas trabajando bajo el paraguas legal (sin fines de lucro) del CNRI. La PSA tuvo éxito en congregar la energía de un grupo grande de usuarios de Python comprometidos, pero su falta de independencia limitó su efectividad.



CNRI también usaba dinero de DARPA para financiar el desarrollo de JPython (luego acortado a Jython), una implementación de Python en y para Java. Jim Hugunin creó originalmente JPython mientras hacía su trabajo para graduarse en el MIT. Luego convenció al CNRI de que lo contrate para completar el trabajo (o tal vez el CNRI lo convenció a Jim para que se una --  sucedió mientras estaba de vacaciones). Cuando Jim dejó el CNRI menos de dos años después para unirse al proyecto AspectJ en Xerox PARC, Barry Warsaw continuó el desarrollo de JPython. (Mucho después,  Jim también crearía IronPython, la versión de Python para la plataforma .NET de Microsoft. Jim también escribió la primera versión de Numeric Python).



Otros proyectos en el CNRI también empezaron a usar Python. Muchos de los nuevos desarrolladores principales de Python salieron de allí, en particular Andrew Kuchling, Neil Schemenauer, y Greg Ward, que trabajaron para el proyecto MEMS Exchange. (Andrew contribuyó con Python incluso antes de unirse al CNRI; su primer proyecto grande fue el Python Cryptography Toolkit, una librería de terceros que ponía a disposición de los usuarios de Python muchos de los algoritmos criptográficos fundamentales).



Cuando Python estaba empezando a tener éxito, CNRI intentó encontrar un modelo para financiar su desarrollo más directamente que a través del subsidio de investigación de DARPA. Creamos el Python Consortium, modelado luego del X Consortium, con un costo de inscripción mínimo de u$s 20.000. Sin embargo, excepto por un grupo en Hewlett-Packard, no conseguimos muchos adherentes y eventualmente el consorcio murió de anemia. Otro intento de encontrar fondos fue Computer Programming for Everybody (CP4E), que recibió algún financiamiento de DARPA. Si embargo, el mismo no era suficiente para todo el equipo <span style="background: white none repeat scroll 0% 0%;">y resultó que había toda una red de viejos miembros queriendo obtener más dinero del que habíamos obtenido del dinero durante esos años. Eso no fue algo que me agradace, y empecé a buscar otras opciones.</span>



Eventualmente, al principio del 2000, el boom de las las .com, que no había colapsado aún, me convenció a mi y a otros tres miembros del equipo de Python en el CNRI (Barry Warsaw, Jeremy Hylton y Fred Drake) de unirnos a BeOpen.com, una startup en California que estaba reclutando desarrolladores de código abierto. Tim Peters, un miembro clave de la comunidad de Python, también se nos unió.



Anticipándonos a la transición a BeOpen.com, una cuestión difícil fue la propiedad futura de Python. CNRI insistió en cambiar la licencia y pidió que distribuyéramos Python 1.6 con una nueva versión de la misma. La vieja licencia, usada mientras aún estaba en CWI, era una versión de la licencia MIT. Las versiones previas hechas en CNRI usaban una versión ligeramente modificada de esa licencia, básicamente con una sentencia agregada en la que el CNRI se liberaba de la mayoría de las responsabilidades. Sin embargo, la licencia de la versión 1.6 era un montón de palabras en lenguaje técnico escrita por los abogados del CNRI.



Tuvimos varios largos forcejeos con Richard Stallman y Eben Moglen de la Free Software Foundation sobre algunas partes de esta nueva licencia. Se temían que sería incompatible con la GPL, y por lo tanto amenazaba la viabilidad de GNU mailman que se había convertido en una herramienta esencial para la FSF. Con la ayuda de Eric Raymond, se hicieron cambios en la licencia para Python del CNRI que satisficieron tanto a la FSF como al CNRI, pero el lenguaje resultante no es fácil de entender. La única cosa buena que puedo decir sobre esto es que (otra vez gracias a la ayuda de Eric Raymond) tenía el sello de aprobación de la Open Source Initiative como una licencia open source genuina. Solo pequeños cambios se hicieron en el texto de la licencia para reflejar los dos siguientes cambios de propiedad, primero para BeOpen.com y luego para la Python Software Foundation, pero en esencia, el trabajo de los abogados del CNRI todavía perdura.



Como tantas startups de ese entonces, el plan de negocio de BeOpen.com falló espectacularmente. Dejó atrás una gran deuda, algunas serias dudas sobre el rol jugado por algunos administradores de la compañía y algunos muy desilusionados desarrolladores además de mi propio equipo.



Afortunadamente mi equipo, conocido como Python Labs, era bastante reciente y fuimos contratados como una unidad de Digital Creations, una de las primeras compañías en usar Python (Ken Manheimer nos había precedido varios años antes). Digital Creations pronto cambió su nombre a Zope Corporation por su principal producto open source, el sistema web de manejo de contenidos Zope. Los fundadores de Zope, Paul Everitt y Rob Page, asistieron al primer Python workshop en NIST en 1994, como lo hizo su CTO, Jim Fulton.



La historia podría haber sido diferente: además de Digital Creations, también consideramos ofertas de VA Linux and ActiveState. VA Linux era la nueva estrella naciente del mercado de acciones,  pero eventualmente el precio de las mismas (que había hecho multi-millonario a Eric Raymond en los papeles) colapsó más que dramáticamente. Mirando hacia atrás, pienso que ActiveState no hubiera sido una mala elección, a pesar de la controversial personalidad de su fundador Dick Hardt, si no hubiera estado ubicada en Canadá.



En el 2001 creamos la Python Software Foundation, una organización sin fines de lucro, que tuvo como miembros iniciales a los principales desarroladores de Python de ese entonces. Eric Raymond fue uno de los miembros fundadores. Tengo que escribir más sobre este período en otro momento.



<em>Traducido por Juan José Conti.

Revisado por César Portela.

Si encontrás errores en esta traducción, por favor reportalos en un comentario y los corregiremos a la brevedad.</em>

Todas las traducciones de esta serie pueden encontrarse en <a href="/categoria/aprendiendo-python/historia/" target="_self">La historia de Python</a>.</body></html>