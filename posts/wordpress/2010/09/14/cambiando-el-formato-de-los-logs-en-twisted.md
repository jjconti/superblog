<html><body><p>En Twisted <a href="http://twistedmatrix.com/documents/current/core/howto/logging.html" target="_blank">se puede tener un log</a> de todo lo que pasa en un programa de forma bastante fácil:

</p><pre lang="python">from twisted.python import log

from twisted.python.logfile import DailyLogFile



log.startLogging(DailyLogFile('log.txt', LOGDIR))</pre>

Todos los <strong>prints</strong> que anden dando vuelta ahora son entradas en el log y de yapa estoy usando DailyLogFile en lugar de un archivo común y corriente para que al final del día rote a un nuevo archivo en disco. Hay varias opciones, esta es la que me sirve a mí.



Por defecto los logs se ven algo así:

<pre lang="bash">2010-05-28 07:41:00-0500 [__main__.TModBusFactory] Nuevo cliente: 190.136.29.16:12101

2010-05-28 07:41:00-0500 [__main__.TModBusFactory] Total: 1

2010-05-28 07:41:01-0500 [TModBus,0,190.136.29.16] G24 dice:  :0090SFE00

2010-05-28 07:41:01-0500 [TModBus,0,190.136.29.16] SITIO SFE

2010-05-28 07:41:01-0500 [TModBus,0,190.136.29.16] Nuevo sitio registrado en MBProxy SFE

2010-05-28 07:45:49-0500 [__main__.TModBusFactory] Nuevo cliente: 190.136.29.16:30519

2010-05-28 07:45:49-0500 [__main__.TModBusFactory] Total: 2

2010-05-28 07:45:49-0500 [TModBus,1,190.136.29.16] G24 dice:  :0090SFE00

2010-05-28 07:45:49-0500 [TModBus,1,190.136.29.16] SITIO SFE

2010-05-28 07:45:49-0500 [TModBus,1,190.136.29.16] SFE ya estaba conectado. Borrando anterior.

2010-05-28 07:45:51-0500 [TModBus,1,190.136.29.16] Nuevo sitio registrado en MBProxy SFE</pre>

¿Cómo podemos cambiar el formato de salida? Algunos tips.



Para cambiar el formato de la fecha y hora:

<pre lang="python">log.FileLogObserver.timeFormat = '%Y-%m-%d %H:%M:%S'</pre>

Para cambiar lo que aparece entre corchetes: utilizar log.msg y el keyword system:

<pre lang="python">log.msg("Nuevo cliente: %s:%d" % (self.peer.host, self.peer.port), system=' - ')</pre>

Con estos dos cambios se puede tener un log como este:

<pre lang="bash">2010-05-28 07:41:00 [ - ] Nuevo cliente: 190.136.29.16:12101

2010-05-28 07:41:00 [ - ] Total: 1

2010-05-28 07:41:01 [SFE] G24 dice:  :0090SFE00

2010-05-28 07:41:01 [SFE] SITIO SFE

2010-05-28 07:41:01 [SFE] Nuevo sitio registrado en MBProxy SFE

2010-05-28 07:45:49 [ - ] Nuevo cliente: 190.136.29.16:30519

2010-05-28 07:45:49 [ - ] Total: 2

2010-05-28 07:45:49 [ - ] G24 dice:  :0090SFE00

2010-05-28 07:45:49 [SFE] SITIO SFE

2010-05-28 07:45:49 [SFE] SFE ya estaba conectado. Borrando anterior.

2010-05-28 07:45:51 [SFE] Nuevo sitio registrado en MBProxy SFE</pre>

Para cambiar aún más el formato de la salida, la única forma que encontré es extender <strong>FileLogObserver</strong> y sobreescribir su método <strong>emit</strong>. Discutimos un poco esto <a href="http://stackoverflow.com/questions/3700955/how-to-format-twisted-logs" target="_blank">en StackOverflow.</a>



<strong>nota:</strong> En Twisted también podemos usar el <a href="http://docs.python.org/library/logging.html" target="_blank">sistema de logging de Python</a>, esto tiene la ventaja de que podemos trabajar con niveles de log y controlar mejor el formato y la forma en que se generan los logs, pero el problema de que no está preparado para funcionar en forma asincrónica y esto puede traer algunos problemas con Twisted.</body></html>