<html><body><p>Con el nombre genérico de Citrix, se suele conocer dentro de muchas empresas a una solución de virtualización de aplicaciones (<a href="http://en.wikipedia.org/wiki/Citrix_XenApp" target="_blank">XenApp</a>) muy utilizada en corporaciones que permite a los usuarios conectarse con su PC a un servidor remoto y ejecutar las aplicaciones que allí se encuentran. Con esto se logra por ejemplo: reducir el gasto en licencias y centralizar actualizaciones.



En la empresa donde trabajo (una multinacional del rubro de las telecomunicaciones) lo usa. Además de aplicaciones de gestión de equipos, dentro de "Citrix", se puede correr un escritorio remoto. Esto permite, desde una PC con Internet, acceder a tu puesto de trabajo respetando las políticas de seguridad que haya dispuesto la empresa.



Ok, quiero acceder desde GNU/Linux. En particular Ubuntu, el SO que uso en mi notebook. El la mayoría de los casos, no vamos a tener soporte para esto. Escribo las siguientes instrucciones con la esperanza de que a alguien le sirva dentro de su organización.



Lo primero que necesitamos es un software cliente. Es la parte fácil. Podemos <a href="http://www.citrix.com/English/SS/downloads/details.asp?downloadID=3323" target="_blank">bajar el cliente e instalarlo</a>. El ejecutable queda en:

</p><pre lang="bash">/usr/lib/ICAClient/wfcmgr

</pre>

Al intenatr ejecutarlo puede ser que obtengamos un error diciendo que falta la bibiloteca libXm.so.4. en Ubuntu 10.04 no viene la versión 4 de esta biblioteca, sino la 3.



Podemos instalar la versión 3:

<pre lang="bash">sudo apt-get install libmotif3

</pre>

y engañarlo; parece funcionar sin problemas:

<pre lang="bash">sudo ln -s /usr/lib/libXm.so.3.0.2 /usr/lib/libXm.so.4

</pre>

Lo siguiente que falta es un certificado, de lo contrario al intentar conectarnos obtendremos un error diciendo que no hemos especificado que confiamos en el host que nos servirá las aplicaciones.



A los usuarios de Windows les dan un archivo binario de extesión <code>.p7b</code> al que le hacen click derecho y eligen la opción "Instalar certificado". En GNU/Linux no es tan fácil y luego de buscar bastante en Internet, no encontré la forma de instalarlo, pero la solución me llegó casi Inspiración Divina o por Instinto Animal.



Utilicé el comando <code>strings</code> para leer cadenas de texto dentro del archivo <code>.p7b</code> y con <code>grep</code> busqué <code>.crt</code>, la extensión de los certificados:

<pre lang="bash">strings XXXX.p7b | grep .crt

</pre>

Encontré una url dentro de la empresa, me bajé el certificado y lo guardé en <code>/usr/lib/ICAClient/keystore/cacerts</code>, que es donde Citrix Xen App guarda los certificados.



Voilá! Estaba adentro.</body></html>