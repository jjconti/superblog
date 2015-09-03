<html><body><p>¿Cómo saber en Django <strong>qué</strong> sentencias SQL se están ejecutando detrás de su ORM? Según la <a href="http://docs.djangoproject.com/en/dev/faq/models/#how-can-i-see-the-raw-sql-queries-django-is-running">FAQ</a>, podemos hacerlo de esta forma:



</p><blockquote>

Make sure your Django DEBUG setting is set to True. Then, just do this:



<pre>&gt;&gt;&gt; from django.db import connection

&gt;&gt;&gt; connection.queries

[{'sql': 'SELECT polls_polls.id,polls_polls.question,polls_polls.pub_date FROM polls_polls',

'time': '0.002'}]</pre>



connection.queries is only available if DEBUG is True. It's a list of dictionaries in order of query execution. Each dictionary has the following:



``sql`` -- The raw SQL statement

``time`` -- How long the statement took to execute, in seconds.



connection.queries includes all SQL statements -- INSERTs, UPDATES, SELECTs, etc. Each time your app hits the database, the query will be recorded.

</blockquote>



Cada vez que se realiza una nueva petición, esa variable es sobre escrita con las consultas que se ejecutaron en la vista asociada. La forma de verlas es accediendo a <code>connection.queries</code> en cada vista de nuestro interés. Para facilitar esta tarea y no tener código intrusivo, escribí un decorador:



<pre>

from django.db import connection

def sql_debug(f):

    '''

    Decorador útil para inspeccionar las sentencias SQL que se ejecutan en

    cada request.

    '''

    def inner(*args, **kwargs):

        r = f(*args, **kwargs)

        for d in connection.queries:

            print "time: %s\n sql:%s\n\n" % (d['time'], d['sql'])

        return r

    return inner

</pre></body></html>