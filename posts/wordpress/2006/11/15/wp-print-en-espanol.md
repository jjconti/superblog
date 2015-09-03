<html><body><p>Acabo de instalar el plug-in <a href="http://dev.wp-plugins.org/wiki/wp-print">wp-print</a> para wordpress. Permite presentar una versión <em>imprimible</em> (sin colores, sin estrafalarios encabezados, pies o barras) de los artículos que uno tiene en el blog.



Le hice algunos pequeños cambios para que se vea en español. <strong>Contra:</strong> el plug-in no está preparado para ser traducido, hay que cambiar varias archivos y el texto en inglés aparece de heterogéneas formas :). <strong>Pro:</strong> yo ya hice algo de esto, así que se los dejo por si les sirve: <a href="http://firebirds.com.ar/~juanjo/wordpress/files/wp-print-es-2.06.tgz">wp-print-es-2.06</a>.



Para instalarlo, además de descomprimirlo en la carpeta <code>plugins</code> y habilitarlo, hay que llamar a print_link() o print_link_image() o ambas desde el código del template del blog, yo agregué:



<code>

&lt;?php if(function_exists('wp_print')) {

echo "&lt;div align='right'&gt;"; print_link_image(); echo " "; print_link(); echo "&lt;/div&gt;"; } ?&gt;

</code>



en <code>index.php</code>, <code>page.php</code>, <code>single.php</code> y <code>archive.php</code>.</p></body></html>