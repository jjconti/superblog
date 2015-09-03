<html><body><p>¿Querés crear un motor de búsqueda de Firefox para tu sitio web? Esta receta es para vos.



<a href="http://astaffolani.blogspot.com/" title="el blog de Adrián" target="_blank">Adrián</a> tiró el desafío en la lista de <a href="http://wiki.gleducar.org.ar/wiki/Portada" title="GleduWiki" target="_blank">Gleducar</a>. Uno de los links dados como pista fue:



<a href="http://developer.mozilla.org/es/docs/Creaci%C3%B3n_de_plugins_OpenSearch_para_Firefox" title="Search Engine" target="_blank">http://developer.mozilla.org/es/docs/Creaci%C3%B3n_de_plugins_OpenSearch_para_Firefox</a>



Puede seguirse sin problemas para generar el archivo xml que describe al plugin, pero me hubiese venido bien encontrar un motor.xml de ejemplo. Tal vez le falten algunos retoques, pero mientras tanto aquí está el mío:

<!--more-->

</p><blockquote>&lt;OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/"

xmlns:moz="http://www.mozilla.org/2006/browser/search/"&gt;

&lt;ShortName&gt;motorGleduwiki&lt;/ShortName&gt;

&lt;Description&gt;"motor de busqueda para el GleduWiki"&lt;/Description&gt;

&lt;InputEncoding&gt;"UTF-8"&lt;/InputEncoding&gt;

&lt;Image width="16" height="16"&gt;IIIIIIIIIIIIIIIIIIII&lt;/Image&gt;

&lt;Url type="text/html" method="POST" template="http://wiki.gleducar.org.ar/wiki/Especial:Search"&gt;

&lt;Param name="search" value="{searchTerms}"/&gt;

&lt;Param name="fulltext" value="Buscar"/&gt;

&lt;/Url&gt;

&lt;Url type="application/x-suggestions+json" template="suggestionURL"/&gt;

&lt;moz:SearchForm&gt;searchFormURL&lt;/moz:SearchForm&gt;

&lt;/OpenSearchDescription&gt;</blockquote>

<a href="http://juanjo.firebirds.com.ar/gleducar/motor.xml" title="motor.xml" target="_blank">motor.xml</a>



Dónde IIIIIIIIIIIIIIIIIIII debe reemplazarse por la salida obtenida en <a href="http://software.hixie.ch/utilities/cgi/data/data" title="2 Base64" target="_blank">http://software.hixie.ch/utilities/cgi/data/data</a> luego de subir una imagen de 16px de lado.



Por último usé:



<code>&lt;<span class="start-tag">script</span><span class="attribute-name"> type</span>=<span class="attribute-value">"text/javascript"</span>&gt;

window.external.AddSearchProvider(urlEngine);

&lt;/<span class="end-tag">script</span>&gt;</code>



dónde urlEngine es la url absoluta al archivo xml generado, encerrado entre comillas.</body></html>