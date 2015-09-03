<html><body><p>En el archivo de configuración <code>settings.py</code> de un proyecto Django, por lo general tenemos que setear variables como <code>MEDIA_ROOT</code> o <code>STATIC_DOC_ROOT.</code> Su contenido en una instalación Windows suele ser algo como: <code>'C:\Windows\camino\hasta\mi\projecto'</code>. Y en Linux:<code> '/home/usuario/camino/a/mi/proyecto'</code>. El problema surge cuando el proyecto es desarrollado en varias máquinas a la vez, y con distintos sistemas operativos. Más aún, si hacemos lo anterior, seguramente versionaremos el proyecto y con él, al archivo de configuración. No sería raro que tras una actualización, el archivo se actualice con los valores que puso algún compañero de trabajo.



Mi solución es definir primero una variable para el proyecto:

</p><pre>PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))</pre>

Luego podemos usarla para definir el path absoluto a la carpeta con archivos de media:

<pre>MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')</pre>

nuestros templates:

<pre>TEMPLATE_DIRS = (

# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".

# Always use forward slashes, even on Windows.

# Don't forget to use absolute paths, not relative paths.

os.path.join(PROJECT_PATH, 'templates')

)</pre>

o cualquier otra variable de configuración que requiere una ruta de directorios.



Con esta solución podemos cambiar el proyecto de carpeta, disco o computadora y seguirá funcionando.</body></html>