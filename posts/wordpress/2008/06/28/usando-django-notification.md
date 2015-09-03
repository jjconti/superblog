<html><body><a href="http://code.google.com/p/django-notification" target="_blank">django-notification</a> es una aplicación para Django que permite al resto de las aplicaciones de un proyecto enviar notas a los usuarios. Así, cuando la aplicación Stock detecta que el número de bulones que hay en el depósito es menor límite de reposición puede enviar una nota de tipo "Avisos prioritarios" al usuario responsable del depósito. Esta nota puede ser recibida por mail, feed o mostrarse en el sistema cuando el usuario inicia su sesión.



El siguiente es un artículo del proyecto que hemos traducido yo y Cecilia.



<!--more-->

<h2>Integrar Notification</h2>

Integrar notification a tu aplicación es un proceso simple de dos pasos.

<ol>

	<li>crear tus tipos de notas (Notice Type)</li>

	<li>enviar notificaciones</li>

</ol>

<h3>Crear tipos de notas (Notice Type)</h3>

Debes ejecutar <code>create_notice_type(label, display, description)</code> una vez para crear los tipos de notas para tu aplicación en la base de datos. <code>label</code> es un nombre interno, corto, que será usado para el tipo, <code>display</code> es lo que el usuario verá como el nombre del tipo de nota y <code>description</code> es una descripción corta.



Por ejemplo:

<pre>

from django.dispatch import dispatcher

from django.db.models import signals



try:

    from notification import models as notification



    def create_notice_types(app, created_models, verbosity, **kwargs):

        notification.create_notice_type("invitacion_amigo", u"Invitación recibida",

                                                     u"has recibido una invitación")

        notification.create_notice_type("invitacion_aceptada", u"Invitación aceptada",

                                                     u"una invitación que enviaste fue aceptada")



    dispatcher.connect(create_notice_types, signal=signals.post_syncdb, sender=notification)

except ImportError:

    print "No se encontró la aplicación notification, no se crearán objetos del tipo NoticeTypes"</pre>

Notar que el código está envuelto con un try para que si django-notification no está instalado, tu aplicación funcione de todas formas.

<h3>Enviar notificaciones</h3>

Para enviar mensajes se usa <code>send(users, notice_type_label, message_template, object_list, issue_notice)</code> dónde <code>object_list</code> y <code>issue_notice</code> son opcionales.



<code>users</code> es una lista de usuarios que deben recibir la nota. <code>notice_type_label</code> es la etiqueta que usaste en el paso previo para identificar un tipo de nota. <code>message_template</code> es solo un string, aunque si <code>object_list</code> no está vacía, entonces <code>message_template</code> debe contener tantos <code>%s</code> como objetos en <code>object_list</code>. Entonces serán reemplazados con referencias a los correspondientes objetos de <code>object_list</code>.



Por ejemplo:

<pre>

notification.send([to_user], "invitacion_amigo", "%s solicita ser tu amigo.", [from_user])</pre>

enviará una nota de tipo <code>invitacion_amigo</code> a <code>to_user</code> con el mensaje <code>XXX solicita ser tu amigo.</code> dónde XXX es una referencia al objeto <code>from_user</code>. Dependiendo del medio de notificación, esta referencia será un link o solo texto plano.



<code>issue_notice</code> es <code>True</code> por defecto pero se puede cambiar a <code>False</code> si querés que una notificación se envíe pero no se persista como un objeto de tipo <code>Notice</code> en la base de datos.



Para permitir que tu aplicación funcione sin notification, podés envolver el import en un try y testear si el módulo fue cargado antes de enviar la nota.



Por ejemplo:

<pre>

try:

    from notification import models as notification

except ImportError:

    notification = None</pre>

y luego:

<pre>

if notification:

    notification.send([to_user], "invitacion_amigo", "%s solicita ser tu amigo.", [from_user])</pre></body></html>