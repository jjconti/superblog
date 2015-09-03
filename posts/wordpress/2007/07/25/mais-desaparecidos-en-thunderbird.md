<html><body><p>Inicias te tu cliente de correo electrónico <a href="http://www.mozilla-europe.org/es/products/thunderbird/" title="Thunderbird" target="_blank">Thunderbird</a> y te encontraste con que faltaban muchos o todos los mails de una de tus carpetas (en mi caso concreto faltaban todos los mails de los últimos 2 años en la carpeta Inbox).



Es muy probable que te haya pasado lo mismo que a mí. Si fue así, estás de suerte, y podés solucionarlo rápidamente. Los índices de las carpetas en Thunderbird son guardados en archivos .msf. Si la salida de Thunderbird es forzada puede corromperse el archivo .msf correspondiente a la carpeta en la que estabamos parados.



¿Cómo recuperarlo?

</p><ol>

	<li>Cerrar Thunderbird (si estaba abierto)</li>

	<li>Borrar el archivo .msf corrupto (o sospechoso de serlo)</li>

	<li>Iniciar Thunderbird (los índices borrados se volverán a crear)</li>

</ol>

Nota



Los archivos .msf se encuentran en:



PROFILE/xxxxxx/Mail/cuenta/*.msf

<ul>

	<li>PROFILE es para mi /home/juanjo/.mozilla-thunderbird/</li>

	<li>xxxxxx es una combinación de letras y números</li>

	<li>cuenta es por ejemplo pop.gmail.com</li>

</ul>

Cuando tuve el problema el archivo corrupto era .mozilla-thunderbird/3o7f7mtq.default/Mail/pop.gmail.com/Inbox.msf, pero de todas formas no eran mostrados los mails de otras cuentas.



Si esto no les sirvió (sorry), pueden econtrar más pistas en <a href="http://kb.mozillazine.org/Disappearing_mail" title="MozillaZine" target="_blank">http://kb.mozillazine.org/Disappearing_mail</a></body></html>