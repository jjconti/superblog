<html><body><a href="http://zombie.firebirds.com.ar" title="TZ en googlecode" target="_blank">Twisted Zombie</a>, el juego que desarrollamos en una semana para la <a href="http://www.pyweek.org/5" title="PyWeek 5" target="_blank">quinta edición del concurso PyWeek</a> ya funciona en Windows. Está escrito en <a href="http://www.python.org" title="Python" target="_blank">Python</a>, un lenguaje multiplataforma, y hemos tenido en cuenta <a href="http://www.juanjoconti.com.ar/2007/01/31/python-multiplataforma-ospathjoin/" title="os.path.join" target="_blank">algunas consideraciones</a> para que funcione sin problemas en distintos sistemas operativos. Incluso lo hemos probado en un par.



Pero para usarlo en Windows necesitás tener instalado <a href="http://www.python.org/ftp/python/2.5.1/python-2.5.1.msi" title="Python 2.5 para Windows" target="_blank">Python</a> y <a href="http://pygame.org/ftp/pygame-1.7.1release.win32-py2.5.exe" title="PyGame 1.7.1 para Windows" target="_blank">Pygame</a>.



El siguiente es un paquete con todo lo necesario para correr el juego si necesidad de instalar nada más: <a href="http://twistedmold.googlecode.com/files/Twisted-Zombie-1-Win.zip" title="Windows self contained package" target="_blank">Twisted-Zombie-1-Win.zip</a>



<!--more-->Este es el código fuente del archivo setup.py que utilicé para crear el paquete:

<pre># setup.py es usado para generar un paquete autocontenido

# para Windows. Incluye el interprete de Python, PyGame

# y otros modulos utilizados en el juego.

# Uso: C:Python25python.exe stup.py py2exe

# Version de py2exe: 0.66

# Nota: en run_game.pyw cambiar os.path.dirname(__file__)

# por la ruta al directorio donde esten los fuentes del

# juego. Ej: 'C:tz'



from distutils.core import setup

import py2exe

import os



options = {

    "py2exe": {

        #"compressed": 1,

        #"optimize": 2,

        #"excludes": excludes,

        "includes": ["pygame", "pygame.locals", "random", "pickle"],

    }

}



data_files = [ (x, [os.path.join(x, e) for e in z]) for d in ("lib", "data")

               for x,y,z in os.walk(d) if not ".svn" in x ] + [ "README.txt"]



setup( console=["run_game.pyw"], data_files=data_files, options=options)</pre></body></html>