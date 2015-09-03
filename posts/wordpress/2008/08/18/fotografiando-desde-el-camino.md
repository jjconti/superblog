<html><body><a href="/wp-content/uploads/2008/08/200808160019221_3426132759.jpg"><img class="alignright size-medium wp-image-515" title="200808160019221_3426132759" src="/wp-content/uploads/2008/08/200808160019221_3426132759-225x300.jpg" alt="" width="135" height="180"></a>Hace unos días empecé a publicar fotos <strong>instantáneas </strong>en mi blog. Basándome en el servicio gratuito de Personal puedo tener en mi blog, en menos de un minuto, fotos que tome con mi celular.



<a title="Album" href="http://album.personal.com.ar" target="_blank">Album Personal</a> es un servicio que te permite subir sin cargo fotos desde tu celular a un espacio privado en la web. Una vez que las fotos están ahí puedo jalarlas (<em>pool</em>) al servidor dónde está alojado mi blog.



Este procesos de pooling es llevado a cabo mediante un script escrito en Python (sirviéndome de las librerías <a title="BeautifulSoup" href="http://www.crummy.com/software/BeautifulSoup/download/BeautifulSoup.py" target="_blank">BeautifulSoup</a>, <a title="urllib2" href="http://www.python.org/doc/lib/module-urllib2.html" target="_blank">urllib2</a> y <a title="cookielib" href="http://www.python.org/doc/lib/module-cookielib.html" target="_blank">cookielib</a>) que puedo ejecutar directamente desde mi celular utilizando <a title="SSH" href="http://www.xk72.com/midpssh/" target="_blank">MidpSSH</a> (un cliente ssh escrito en <a title="Java ME" href="http://java.sun.com/javame/index.jsp" target="_blank">Java</a> para celulares).

<p style="text-align: center;"><a href="/wp-content/uploads/2008/08/200808171445262_3426132759.jpg"><img class="size-medium wp-image-516 aligncenter" title="200808171445262_3426132759" src="/wp-content/uploads/2008/08/200808171445262_3426132759-225x300.jpg" alt="" width="135" height="180"></a></p>

<p style="text-align: left;">Por ahora solo se visualiza la última foto que subo en la página principal del blog. Pronto voy a implementar un álbum desde el cual  ver también las fotos anteriores.<a href="/wp-content/uploads/2008/08/200808171623181_3426132759.jpg"><img class="size-medium wp-image-517 aligncenter" title="200808171623181_3426132759" src="/wp-content/uploads/2008/08/200808171623181_3426132759-225x300.jpg" alt="" width="135" height="180"></a></p></body></html>