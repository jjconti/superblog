<html><body><p>Si intentás usar FPDF en Django hay algunas cosas que necesitás saber:

</p><ul>

	<li>(ya sabés qué) <a href="http://www.fpdf.org/">FPDF</a> está originalmente escrita en PHP y permite generar documentos PDF sin usar PDFLib (C).</li>

	<li>(ya sabés qué) hay más de un port de esta librería a Python. Todos son incompletos.</li>

	<li>Usá este <a href="http://www.nsis.com.ar/svn/pyfpdf/" target="_blank">http://www.nsis.com.ar/svn/pyfpdf/</a> (parcheado en Argentina para utilizar unicode).</li>

	<li>FPDF <a href="http://www.fpdf.org/en/FAQ.php#q7">trabaja con la codificación ISO-8859-1</a>.</li>

	<li>Mi código fuente Django usa la cotificación UTF-8 y en los documentos resultantes aparecían caracteres raros en lugar de vocales con tilde o eñes.</li>

	<li>Lo soluciné haciendo una modificacicón en el método Output:</li>

</ul>

<code>self.buffer = buffer.encode('iso-8859-1')</code></body></html>