<html><body><p>Mientras estudié el tema para hacer un experimento, traduje el 80% de la <a href="http://docs.djangoproject.com/en/dev/topics/http/middleware/" target="_blank">documentación oficial</a>. La dejo aquí más algunos condimentos personales.

</p><h2>Middleware</h2>

Es un sub framework que permite modificaciones al sistema de procesamiento de request/response de Django. Es un sistema de plugins liviano y de bajo nivel que permite alterar globalmente las entradas y salidas de Django.



Cada componente middleware es responsable de hacer alguna función específica.

<h3>Activar componentes middleware</h3>

Para hacerlo, añadirlo a la lista MIDDLEWARE_CLASSES en la configuración de Django (settings.py). En esta lista, cada componente se representa por un string: el camino completo al nombre de la clase. Por ejemplo:

<pre>MIDDLEWARE_CLASSES = (

'django.middleware.common.CommonMiddleware',

'django.contrib.sessions.middleware.SessionMiddleware',

'django.contrib.auth.middleware.AuthenticationMiddleware',

)</pre>

En el tratamiento de requests y la generación de responses, existen dos faces:



1) Fase Request (se llama a los métodos process_request() y process_view())

2) Fase Response (se llama a los métodos process_response() y process_exception())



En la primera, las clases son aplicadas desde la primera a la última, según el orden de la lista mencionada. En la segunda fase, se aplican en orden inverso; podemos pensarlo como una cebolla:

<p style="text-align: center;"><img class="aligncenter size-full wp-image-1740" title="middleware" src="/wp-content/uploads/2009/08/middleware.png" alt="middleware" width="502" height="417"></p>



Una instalación de Django puede funcionar sin ningún middleware, pero esto no es recomendado.

<h3>Para escribir middleware propios</h3>

Cada componente es una clase Python, que no tiene que extender a ninguna clase en particular y debe definir uno o más de los siguientes métodos.

<pre>process_request(self, request)</pre>

request es un objeto HttpRequest. El método es llamada por cada request, antes de que Django decida que vista ejecutar.



Debe retornar None o un objeto HttpResponse. Si retorna None, Django seguirá procesando el request, ejecutando los otros middlewares y luego la vista apropiada. Si retorna un objeto HttpResponse, Django no hará nada más, solo retornar ese objeto.

<pre>process_view(self, request, view_func, view_args, view_kwargs)</pre>

request es un objeto HttpRequest. view_func es la función Python que Django está por usar. (Es el objeto function, no el nombre de la función en un string). view_args es un alista de argumentos posicionales que serán pasados a la vista. Y view_kwargs es un diccionario de argumentos de palagra clave que serán pasados a la vista. Ni view_args ni view_kwargs incluye al primer argumento de la vista (request).



process_view() es llamado antes de que Django ejecute la vista. Debe retornar None o un objeto HttpResponse. Si retorna None, Django seguirá procesando el request, ejecutando otros process_view() y luego la vista apropiada. Si retorna un objeto HttpResponse, Django no hará nada más, solo retornar ese objeto.

<pre>process_response(self, request, response)</pre>

request es un objeto HttpRequest. response es un objeto HttpResponse retornado por una vista de Django.



process_response() debe retornar un objeto HttpResponse. Puede altener el objeto response dado o puede crear uno nuevo.



A diferencia de proces_request() y process_view(), este siempre es ejecutado.

<pre>process_exception(self, request, exception)</pre>

request es un objeto HttpRequest. exception es un objeto Exception lanzado por la vista.



Django llama a process_exception() cuando la vista lanza una excepción. process_exception() debe retornar None o un objeto HttpResponse. Si retorna un objeto HttpResponse, la respuesta es devuelta al navegador. De lo contrario, el sistema por defecto para manejo de excepciones entra en acción.

<pre>__init__</pre>

Por lo general estas clases no tienen estado; simplemente contienen a los anteriores métodos. Se puede usar el método __init__ pero se debe tener en cuenta que Django inicializa estas clases sin argumentos y que el método __init__ es llamado solo una vez, cuando el servidor web arranca.

<h2>Experimento</h2>

Con lo anterior en mente, me quedaron algunas dudas al respecto:

<ul>

	<li>si modifico los argumentos de view_func en process_view y retorno None, ¿estos son pasados modificados a la vista?</li>

	<li>si lo anterior es falso, puedo lograr el mismo efecto haciendo:



<pre>def process_view(self,request, view_func, view_args, view_kwargs):

    # modificar request, view_args y view_kwargs

    return view_func(request, view_args, view_kwargs)</pre>

?</li>

	<li>¿puedo definir process_response de tal forma que examine response?</li>

</ul></body></html>