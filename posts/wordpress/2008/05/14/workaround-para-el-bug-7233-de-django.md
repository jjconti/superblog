<html><body><p>El bug se describe en <a href="http://code.djangoproject.com/ticket/7233" title="7233" target="_blank">http://code.djangoproject.com/ticket/7233</a>, pero básicamente consiste en la imposibilidad de guardar objetos de tipo <a href="http://www.djangoproject.com/documentation/request_response/#querydict-objects" title="QueryDict" target="_blank">QueryDict</a> en una <a href="http://www.djangoproject.com/documentation/sessions/" title="sessions" target="_blank">sesión</a>. Los usuarios de Django suelen toparse con el problema al intentar guardar en la sesión el objeto request.POST, yo lo hago de esta forma:



<code>request.session['POST'] = dict(request.POST.items())</code>



No sirve si se tienen múltiples valores para una clave porque <code>items</code> devuelve para cada clave el último valor almacenado.



En este caso, se puede usar <code>lists</code>:



<code>request.session['POST'] = dict(request.POST.lists())</code></p></body></html>