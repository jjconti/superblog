<html><body><p>A veces me pasa que en un proyecto tengo un archivo X que empezó siendo un archivo común, pero en un momento dado, cada desarrollador necesita taner su propia copia y no revisionarlo más.



Cómo dejar de revisionarlo sin borrarlo?



La primer vez que me topé con el problema hice:

</p><pre lang="bash">cp X Y

svn rm X

svn ci -m "chau X"

mv Y X

</pre>

Ugly.



La forma correcta de hacerlo es:

<pre lang="bash">svn rm --keep-local X

</pre></body></html>