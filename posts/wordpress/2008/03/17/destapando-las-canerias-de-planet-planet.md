<html><body><p>Palabras claves: planet-planet exception KeyError



Antes de venirme para Pellegrini recibí algunos avisos de que los planetas de <a title="PyAr" href="http://pyar.firebirds.com.ar/" target="_blank">PyAr</a> y <a title="TecnoFe" href="http://blogs.firebirds.com.ar/" target="_blank">TecnoFe</a> no se estaban actualizando. Estos dos sitios corren sobre dos instalacions de <a title="PP" href="http://www.planetplanet.org/" target="_blank">planet-planet</a>, un agregador de feeds escrito en Python. El programa consiste en un script que cada vez que se ejecuta genera páginas html, actualizando su contenido entre corrida y corrida si corresponde.



Mediante reglas de <a title="Cron" href="http://es.wikipedia.org/wiki/Cron_(unix)" target="_blank">cron</a> hago que estos scripts corran cada 15 minutos, buscando novedades en los blogs agregados.



Mi primer intento de saber qué estaba pasando fue revisar crontab, pero no encontré nada raro allí. Lo siguiente fue ejecutar a manos los scripts en cuestión. Ambos tiraban exepciones similares:



<!--more--><code>Traceback (most recent call last):

File "planet.py", line 167, in ?

main()

File "planet.py", line 160, in main

my_planet.run(planet_name, planet_link, template_files, offline)

File "/home/.orithyia/jjconti/pyar.firebirds.com.ar/planet-2.0/planet/__init__.py", line 240, in run

channel = Channel(self, feed_url)

File "/home/.orithyia/jjconti/pyar.firebirds.com.ar/planet-2.0/planet/__init__.py", line 527, in __init__

self.cache_read_entries()

File "/home/.orithyia/jjconti/pyar.firebirds.com.ar/planet-2.0/planet/__init__.py", line 569, in cache_read_entries

item = NewsItem(self, key)

File "/home/.orithyia/jjconti/pyar.firebirds.com.ar/planet-2.0/planet/__init__.py", line 845, in __init__

self.cache_read()

File "/home/.orithyia/jjconti/pyar.firebirds.com.ar/planet-2.0/planet/cache.py", line 74, in cache_read

self._type[key] = self._cache[cache_key + " type"]

File "/usr/lib/python2.3/bsddb/__init__.py", line 116, in __getitem__

return self.db[key]

KeyError: 'tag:www.taniquetil.com.ar,2007-08-31:285 author type'

</code>

Este software tiene un cache de informacion para guardar los feeds que parsea. Basicamente es un directorio llamado cache con un archivo por cada feed agregado.



Solucioné el problema -más por instinto que por pericia- borrando, para ambos sitios, el archivo correspondiente al blog con problemas. Les dejo el tip por si les sucede en alguna instalación de planet-planet. Prometo que si me vuelve a pasar voy a investigar un poquito más para descubrir la razón del problema :)</p></body></html>