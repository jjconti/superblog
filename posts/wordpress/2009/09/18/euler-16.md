<html><body><p>De vez en cuando se me da por hacer saries de posts en el blog. Sagas. Una de las últimas fue la saga sobre <a href="http://www.juanjoconti.com.ar/etiqueta/euler/" target="_blank">resoluciones a problemas del proyecto Euler</a>. Lo que intentaba era resolverlos con alguna característica interesante de Python y luego explicarla. Luego de los primeros, los ejercisios se volvieron más matemáticos y encontraba menos cosas interesantes de Python que comentar, así que dejé de postear mis soluciones. Acabo de encontrar esta entre mis archivos y creo que tiene algo de originalidad como para merecer ser publicada:



<em><a href="http://projecteuler.net/index.php?section=problems&amp;id=16" target="_blank">¿Cuál es la suma de los dígitos del número 2^(1000)?</a></em>

</p><pre>&gt;&gt;&gt; 2**1000

107150860718626732094842504906000[algunos números fueron intencionalmente borrados]

&gt;&gt;&gt; a = 2**1000

&gt;&gt;&gt; sum((int(x) for x in list(str(a))))

1366</pre>

¿A alguien se le ocurre otra forma?</body></html>