<html><body><p>N-Puzzle sigue sin tener una real inteligencia, pero hice una modificación que lo hace verse un poco más inteligente:



Si un jugador o el desordenador aleatorio hace movimientos que se cancelan entre sí

</p><ul>

	<li>Izquierda - Derecha</li>

	<li>Izquierda - Izquierda - Derecha - Derecha</li>

	<li>Izquierda - Izquierda - Arriba - Arriba - Derecha - Izquierda - Abajo - Abajo - Derecha - Derecha</li>

</ul>

el siguiente algoritmo es capás de eliminarlos de la lista de acciones y así lograr una resolución en menos movimientos y que parezca menos tonta.

<!--more-->



El método que encapsula al algoritmo en cuestión es llamado cada vez que se entra al modo Auto Solve:

<pre>

    def _reduce_actions(self):

        '''This method try to reduce the actions' log

        removing repeted moves.'''



        log = self.actions_log

        stack = []



        while log:



            a = log.pop()

            ia = self._inverse_action(a)



            if stack:

                s = stack.pop()

                if ia != s:

                    stack += [s, a]

            else:

                stack += [a]



            print "Stack: ", len(stack)

            print "Log: ", len(log)



        stack.reverse()

        self.actions_log = stack</pre>

Download last version: <a href="http://www.juanjoconti.com.ar/files/python/n-puzzle-0.1-2.tgz">n-puzzle-0.1-2</a></body></html>