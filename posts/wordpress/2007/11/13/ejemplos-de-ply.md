<html><body><p>Acabo de crear <a target="_blank" title="PLY examples" href="http://www.juanjoconti.com.ar/files/python/ply-examples/">un sitio web</a> con todos los ejemplos de PLY que acompañan su distribución.



En distribuciones derivadas de Debian los pueden encontrar en:



<code>/usr/share/doc/python-ply-doc/examples/

</code>

luego de haber instalado python-ply y su documentación:



<code>apt-get install python-ply python-ply-doc</code>



<a target="_blank" title="PLY examples" href="http://www.juanjoconti.com.ar/files/python/ply-examples/"><strong>PLY Examples</strong></a>

<!--more-->Los archivos .py de los ejemplos se encuentran en una versión html con su sintaxis coloreada. Esto lo hice con el comando <code>pygmentize</code>. Para poder usarlo, en Debian y similares, debemos instalarlo el paquete <code>python-pygments</code>. <a target="_blank" title="Pygments" href="http://pygments.org/">Más información</a>.



En particular utilicé OpenOffice para editar el README que acompaña la distribución de los ejemplos y crear una página html y este oneliner para crear todos los .py.html de una pasada:

<code>

for d in `ls -d * | grep -v index.html`; do cd $d; for f in `ls *.py`; do pygmentize -f html -O full -o $f.html $f; done; cd ..; done</code>



Espero sea útil, cree el sitio a partir de una sugerencia en la lista de correos de PLY.</p></body></html>