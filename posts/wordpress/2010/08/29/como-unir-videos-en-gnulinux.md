<html><body><p>Ayer en <a href="http://es.wikipedia.org/wiki/Carlos_Pellegrini_%28Santa_Fe%29" target="_blank">Carlos Pellegrini</a> fue el <a href="http://es.wikipedia.org/wiki/Agust%C3%ADn_de_Hipona" target="_blank">Día del Pueblo</a>. Una de las actividades que hubo fue una <strong>carrera de autos con obstáculos</strong>. Aproveché para filmar un poco y probar <a href="http://es.wikipedia.org/wiki/Motorola_Milestone" target="_blank">mi nuevo celular</a>, por lo que terminé con varios archivos <strong>mp4</strong>. Para subirlos a Internet quería unirlos: ¿cómo hacerlo de forma fácil? Si tenés varios archivos de texto y querés unirlos, o expresándome de forma más correcta, <strong>contactenarlos</strong>, usás el comando <strong>cat</strong>. ¿Se puede hacer lo mismo con videos? Suena algo loco cuando se escucha por primera vez, pero hay algunos formatos que SI lo soportan, como <a href="http://es.wikipedia.org/wiki/MPEG-1" target="_blank">mpeg 1</a> y <a href="http://es.wikipedia.org/wiki/MPEG-2" target="_blank">2</a>.



Usando <strong>ffmpeg</strong> podemos convertir los archivos mp4 a mpeg. Parados en el directorio donde estén los videos:

</p><pre lang="bash">for i in `ls *.mp4`; do ffmpeg -i $i -sameq $i.mpeg; done

</pre>

Ahora simplemente los <strong>concatenamos y redirigimos la salida de cat</strong> a un nuevo archivo:

<pre lang="bash">cat *.mpeg &gt; video.mpeg

</pre>

Notemos que el orden <em>lexicográfico</em> de los videos coincide con el orden en que fueron tomados; por eso puedo usar el * y obtener un resultado ordenado en el tiempo.



Listo, <a href="http://www.youtube.com/watch?v=8Txgi8mFy6w" target="_blank">subí el resultado a YouTube</a>.



Me hubiese gustado una transición más suave entre video y video, pero investigarlo y hacerlo excedía la ecuación costo beneficio. Se escuchan ideas!</body></html>