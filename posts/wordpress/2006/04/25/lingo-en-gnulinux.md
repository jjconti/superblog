<html><body><p>En Investigación Operativa estamos usando el software Lingo, desde su web bajé la versión de evaluación para uso académico para GNU/Linux. La versión disponible es la 9.0, para Windows está ya la 10.0 :(

<a title="Lingo9 para Linux" href="http://www.lindo.com/downloads/LINGO-LINUX-IA32-9.0.tar.gz">http://www.lindo.com/downloads/LINGO-LINUX-IA32-9.0.tar.gz</a>



Seguí leyendo para obtener algunos tips..

<!--more-->

<strong>Ponerlo a andar</strong>



<code>$ tar xvfz LINGO-LINUX-IA32-9.0.tar.gz

$ LD_LIBRARY_PATH=$PWD/lingo9/bin

$ export LD_LIBRARY_PATH

$ LINGO_LICENSE_FILE=$PWD/lingo9/license/lndlng90.lic

$ export LINGO_LICENSE_FILE

</code>

<strong>Y ejecutarlo..</strong>

<code>

$ cd  cd lingo9/bin/linux32/

$ ./lingo9

</code>



<strong>Una vez en la matrix:</strong>

<code>

: take modelo1.lingo

: go

</code>



El archivo puede crearse con cualquier editor de texto, yo estoy usando Vim y me instalé un <a href="http://www.vim.org/scripts/script.php?script_id=1122">resaltador de sintaxis para lingo</a>.



<strong>En Vim:</strong>

<code>

: syntaxis on

: colorscheme elflord

</code>



<strong>Reporte de sensibilidad</strong>

Por defecto esta característica no está habilitada, se puede habilitar ejecutando el siguiente comando antes de obtener la solución del modelo:

<code>

: SET DUALCO 2

</code>

Luego, para guardar esta opción como por defecto:



<code>: FREEZE</code>



<strong>Ejemplo</strong>: 



<a href="files/g2ej6.lingo">g2ej6.lingo</a>

</p></body></html>