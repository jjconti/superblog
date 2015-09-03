<html><body><p>En mi anterior artículo les conté sobre <a href="http://www.juanjoconti.com.ar/2008/06/12/soporte-unicode-para-pyrtf-ng/" title="pyrtf-ng" target="_blank">pyrtf-ng</a>, una librería para generar <a href="http://es.wikipedia.org/wiki/Rich_Text_Format" title="Rich Text Format" target="_blank">archivos rtf</a> en forma fácil desde un programa escrito en Python. Fue la primer alternativa que manejamos a la hora de plantearnos el problema de generar archivos rtf en forma dinámica desde <a href="http://www.djangoproject.com" title="Django project" target="_blank">Django</a>.



En este artículo les cuento el <em>aproach</em> que finalmente adoptamos. Si la naturaleza dinámica del documento que queremos generar radica en que ciertas partes del texto tendrán valores dinámicos o ciertas partes pueden estar o no dependiendo de alguna condición, lo que podemos hacer es utilizar un sistema de templates. El formato rtf es un lenguaje de marcas (es texto, no binario!). Por lo que fácilmente podemos usar el <a href="http://www.djangoproject.com/documentation/templates/" target="_blank">subsistema de templates de Django</a> para lograr nuestro objetivo.<!--more-->

</p><h2>Un ejemplo de lo que queremos obtener</h2>

Simplificando, si en el sistema la variable <code>nombre</code> vale <code>"Juan"</code> y la variable <code>tratamiento</code> es <code>False</code>, el resultado esperado en el archivo rtf es:

<blockquote>Hola Juan</blockquote>

Si la variable <code>nombre</code> vale <code>"Raúl"</code>, la variable <code>tratamiento</code> es <code>"Sr."</code> el resultado esperado en el archivo rtf es:

<blockquote>Hola Sr. Raúl</blockquote>

Para lograrlo necesitamos un archivo hola.rtf (puede tener cualquier nombre y cualquier extensión, pero estos parecen apropiados para el ejemplo) ubicado en algún <a href="http://www.djangoproject.com/documentation/settings/#template-dirs" title="Definido en settings.py" target="_blank">directorio accesible por el subsistema de templates</a>. Tip: crear un archivo rtf con OpenOffice Writer o WordPad y luego editarlo con un editor de texto para agregar las marcas necesarias para que Django lo procese.

<h2>El template</h2>

Así se ve el template del ejemplo cuando lo abrimos con un editor de texto, luego de agregar las marcas correspondientes:

<code>

<strong>{% load filtros %}</strong>{\rtf1\ansi\deff0\adeflang1025

{\fonttbl{\f0\froman\fprq2\fcharset0 Bitstream Vera Sans;}{\f1\froman\fprq2\fcharset0 Bitstream Vera Sans;}{\f2\fswiss\fprq2\fcharset0 Bitstream Vera Sans;}{\f3\fnil\fprq2\fcharset0 Bitstream Vera Sans;}}

{\colortbl;\red0\green0\blue0;\red128\green128\blue128;}

[....]

{\rtlch \ltrch\loch\f0\fs24\lang11274\i0\b0 Hola <strong>{% if tratamiento %}{{ tratamiento }} {% endif %}{{ nombre|rtf }}</strong>}

\par }

</code>

El encabezado suele ser largo (esto depende del programa utilizado para crear el documento, con WordPad se obtienen los encabezados más cortos). Las partes importantes están resaltadas en <strong>negrita</strong>.



El bloque <code>load</code> carga el filtro de nombre rtf que luego es usado. Notar que este bloque debe incluirse en la misma línea que la primer línea del documento o en alguna línea siguiente, pero nunca en la primer línea del archivo y solo. Esto provocará una línea en blanco al principio del documento resultante, un error de sintaxis en el formato rtf, y por lo tanto no podrá ser interpretado por los procesadores de palabras.

<h2>Un filtro para codificar caracteres Unicode en rtf</h2>

Como rtf no soporta nativamente caracteres Unicode (tildes y otros caracteres no ascii), estos deben ser codificados para ser correctamente interpretados. El siguiente filtro hace esa tarea, es un <a href="http://www.djangoproject.com/documentation/templates_python/#template-filters-that-expect-strings" target="_blank">string filter</a> de Django:

<pre>

@register.filter(name='rtf')

@stringfilter

def rtf(value):

    if isinstance(value, UnicodeType):

        return "".join(["u%s?" % str(ord(c)) for c in value])

    return value</pre></body></html>