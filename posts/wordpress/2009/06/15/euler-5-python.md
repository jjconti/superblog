<html><body><h2>Enunciado 5</h2>

<div class="problem_content">



2520 es el menor número que puede ser dividido sin resto por todos los números de 1 a 10.



¿Cuál es el menor número que que puede dividirse sin resto por todos los números de 1 a 20?</div>

<h2>Solución</h2>

La solución fue obtenida ejecutando el siguiente programa Python 2.5.2:

<pre>from math import sqrt

from operator import mul, add



def primo(n):

    for i in xrange(2,int(sqrt(n))+1):

        if n % i == 0:

            return False

    return True



def factorizar(n):

    primos = [x for x in xrange(2,n+1) if primo(x)]

    factores = []

    if n == 1:

        return [1]

    for p in primos:

        if n == p:

                factores.append(p)

                return factores

        if n % p == 0:

                n /= p

                factores.append(p)

                while n % p == 0:

                    n /= p

                    factores.append(p)

    return factores



def mcm(l):

    '''Maximo comun multiplo'''

    ff = [factorizar(i) for i in l]

    singles = list(set(reduce(add,ff)))

    temp = []

    for s in singles:

        temp.extend([s] * max([f.count(s) for f in ff]))

    return reduce(mul,temp,1)



if __name__ == '__main__':

    #print mcm(range(1,11))

    print mcm(range(1,21))</pre>

<h2>Python tips</h2>

<ul>

	<li>El módulo <code>operator</code> tiene varias funciones útiles equivalentes a operadores como * y + que pueden utilizarse con funciones como <code>reduce</code>, cuyo primer parámetro es una función.</li>

	<li><code>reduce</code> toma una función f de dos argumentos y una lista l. Aplica f a los dos primeros elementos de la lista y obtiene un resultado, luego aplica la función f al resultado con el tercer elemento de la lista, y así sucesivamente hasta consumir toda la lista y retornar el resultado final. Opcionalmente se le puede pasar un tercer parámetro para que la primer llamada a la función f sea aplicada sobre este y el primer elemento de la lista.</li>

</ul></body></html>