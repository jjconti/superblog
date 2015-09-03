<html><body><p>MyTwitGroup o <a href="http://www.mytwitgroup.com/" target="_blank">www.mytwitgroup.com</a> es un servicio que implementamos con dos compañeras hace unos 6 meses. Uno de los objetivos del proyecto era ver como funcionábamos como equipo, si podíamos construir y entregar software en tiempo y forma. Nos fue bastante bien.

</p><h2>El servicio</h2>

La idea del servicio surgió de una necesidad real. En la cátedra de Comunicaciones somo 4 personas que usamos Twitter y queríamos usar esa herramienta para comunicarnos con los alumnos, pero no queríamos obligarlos a que nos sigan a cada uno.



<strong>MyTwitGroup revisa periódicamente el timeline de cada uno de los miembros y si encuentra un tweet con el hashtag </strong><strong>#com lo publica utilizando la cuenta de la cátedra.</strong>



El servicio lo pueden usar desde empresas hasta bandas de rock. Yo creo que es útil, pero para entenderlo realmente tenés que usarlo. Si tenés una "cuenta grupal" probalo, no te cuesta nada.

<h2>Fallas</h2>

Cuando implementamos la primera versión del sistema, utilizamos la forma básica de autenticación de Twitter: era fácil de implementar y funcionaba. Tenía un problema, el grupo que creaba una cuenta en el sitio debía dejar la contraseña de la cuenta del grupo para que luego se puedan hacer las publicaciones automáticas. Tuvimos resistencia de usuarios por esto. Intentamos solucionarlo obteniendo un certificado que podamos usar para enviar la información por HTTPS. Los certificados son caros. Usamos uno gratuito unos meses, pero luego caducó. Esta fue la falla 1.



Falla 2. Hace menos de un mes Twitter decidió apagar su sistema de autenticación básico y nuestro servicio dejó de andar. Algo corto de tiempo por otros proyectos y obligaciones, con la ayuda de <a href="http://fisadev.blogspot.com/" target="_blank">fisa</a> migramos a la nueva forma de autenticación: OAuth.



OAuth en Twitter <a href="http://arstechnica.com/security/guides/2010/09/twitter-a-case-study-on-how-to-do-oauth-wrong.ars/" target="_blank">está mal implementado</a> e hizo renegar a muchas personas; por semanas, populares clientes no funcionaron y a los paranoicos de la seguridad no les termina de cerrar la implementación OAuth de Twitter. Pero a nosotros nos vino bien! <strong>Usando OAuth dejamos de pedirle  la password al usuario y muchos que no hubiesen probado el servicio, tal vez lo hagan.</strong> También dejamos de necesitar un costoso certificado.

<h2>Bugs fixing</h2>

Cambiamos de hosting y salió a la cancha, pero con algunos temitas que fui corrigiendo <em>on demand</em>. Cambié la BD de SQLite a PostgreSQL. Cambié el máximo tamaño para el hashtag de 10 a 20 (gracias walteralini por probarlo). No funcionaba la página "contact us" por que arrastré la configuración del viejo hosting.



Tengo que arreglar algunas cosas de usabildad todavía, el workflow logearse/editar puede ser engorroso, pero ya son detalles sutiles.



<a href="http://www.mytwitgroup.com/" target="_blank">El sitio queda on line</a> y ya tenemos algunos felices usuarios de esta nueva era. ¿Ideas o sugerencias? Dejalas en los comentarios!</body></html>