<html><body><p>La siguiente es la mejor forma que encontré de tomar todos los archivos models.py de las aplicaciones que componen un proyecto Django y generar un diagrama de clases completo, listo para exportar cómo imagen. Utilizo un comando incluido en <a href="http://code.google.com/p/django-command-extensions/">django-command-extensions</a>.

<!--more-->

</p><h2>Obtener e instalar django-extensions</h2>

Para Django 1.0 hay que bajar la última versión del svn:

<code>

svn checkout http://django-command-extensions.googlecode.com/svn/trunk/ django-command-extensions

</code>

E instalarlo ejecutando el script de instalación:

<code>

cd django-command-extensions

sudo python setup.py install

</code>

Podemos probar si se instaló correctamente abriendo una consola Python y ejecutando:

<code>

&gt;&gt;&gt; import django_extensions

</code>

Para que este disponible en nuestro proyecto debemos agregar la aplicación a <code>settings.py</code>:

<code>

INSTALLED_APPS = (

...

'django_extensions'

)

</code>

Cuando ejecutemos:

<code>

python manage.py help

</code>

veremos una lista de los nuevos comandos disponibles.

<h2>Generar archivo .dot</h2>

Uno de ellos es graph_models el cual nos permitirá generar un archivo en formato .dot:

<code>

python manage.py graph_models -a &gt; mi_proyecto.dot

</code>

<h2>Generar archivo .png</h2>

O una imagen png:

<code>

python manage.py graph_models -a -g -o mi_proyecto.png

</code>

Para que el anterior comando funcione, necesitamos tener instalado <a href="https://networkx.lanl.gov/wiki/pygraphviz/">pygraphviz</a>. En mi Ubuntu no tenía el paquete python-pygraphviz por lo que tuve que bajarlo desde su página web. Para instalarlo requiere tener instalados los paquetes graphviz y graphviz-dev.

<h2>Ejemplo</h2>

El siguiente comando genera el diagrama de clases para auth, la popular aplicación que viene con Django y sirve como ejemplo de cómo generar el diagrama para solo una aplicación del proyecto:

<code>

python manage.py graph_models auth -g -o mi_proyecto_auth.png

</code>

<a href="/wp-content/uploads/2008/10/mi_proyecto_auth.png"><img class="aligncenter size-full wp-image-766" title="mi_proyecto_auth" src="/wp-content/uploads/2008/10/mi_proyecto_auth.png" alt="" width="475" height="880"></a>

<h2>Nota</h2>

Les recomiendo bajar la versión de pygraphviz empaquetada de Cheeseshop en lugar de la del svn, ya que con esta el comando de django-extensions lanza una excepción. Correguí el programa, <a href="http://code.google.com/p/django-command-extensions/issues/detail?id=66">abrí un ticket y envié un parche</a>. Para cuando leas esto probablemente ya se haya incorporado a trunk.</body></html>