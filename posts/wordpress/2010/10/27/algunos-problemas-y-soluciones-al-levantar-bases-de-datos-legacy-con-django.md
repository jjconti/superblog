<html><body><a href="http://docs.djangoproject.com/en/dev/howto/legacy-databases/" target="_blank">Con Django</a> podemos levantar una <a href="http://stackoverflow.com/questions/939465/what-does-the-term-legacy-database-mean" target="_blank">base de datos <em>legacy</em></a> en lugar de definir nuestro modelo de datos y arrancar una aplicación desde cero. No es necesariamente una base de datos vieja, sino una base de datos heredada de otro sistema; puede ser de un sistema anterior que se está reemplazando o incluso de otro sistema que queremos usar de forma paralela.



Luego de configurar nuestra base de datos y ejecutar:

<pre>python manage.py inspectdb &gt; models.py</pre>

obtenemos una definición de modelos basada en en las tablas de la base de datos. Lo siguiente es ver si anda.



Lo más probable es que obtengamos un <a href="http://docs.python.org/library/exceptions.html#exceptions.NameError" target="_blank">NameError</a>. Esto pasa cuando en la definición de alguno de los modelos se hace referencia a otro modelo aún no definido! La solución indicada es empezar a reordernar los modelos, pero una forma más fácil es cambiar los nombres por strings. Un ejemplo:

<pre>jefe = models.ForeingKey(Empleado)

</pre>

por

<pre>jefe = models.ForeingKey('Empleado')

</pre>

Otra queja que nos puede hacer Django es que tengamos atributos llamados <strong>id</strong> que no sean <em>primary key</em>. Solución: les cambiamos el nombre.



Eventualmente vamos a necesitar habilitar la aplicación <a href="http://docs.djangoproject.com/en/dev/ref/contrib/admin/" target="_blank"><strong>admin</strong></a> (ya que estamos usando Django para levantar datos, nada mejor que usar su ABM estrella para ahorrarnos mucho trbajo). Los pasos para hacer con éxito son:

<ol>

	<li>Habilitar la aplicaccion admin en <code>settings.py</code>.</li>

	<li>Ejecutar <code>syncdb</code> para que se creen las tablas de esta aplicación.</li>

	<li>Agregar los modelos de la base de datos heredada al archivo <code>admin.py</code> de la aplicación.</li>

</ol>

Por supuesto, si los nuevos modelos son cientos, es bastante engorroso hacer esto a mano. Les paso un hack; así luce mi <code>admin.py</code>:

<pre>from django.contrib import admin

from django.db.models import base

from my_app.models import *



for k,v in locals().items():

    if isinstance(v, base.ModelBase):

        admin.site.register(v)</pre>

Tip final. Si obtenemos un error de este tipo:

<pre lang="bash">OperationalError at /admin/mango/datapointusers/

(1054, "Unknown column 'dataPointUsers.id' in 'field list'")

</pre>

es por que alguna de las tablas levantadas no tenía una columna que sea clave primaria. Django necesita esto para poder distinguir los objetos entre si. Para cada tabla dónde tengamos este problema, podemos ejecutar el siguiente comando SQL para agregarle una columna llamada id; clave primaria y auto numérico.

<pre lang="sql">ALTER TABLE `dataPointUsers` ADD `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY;

</pre></body></html>