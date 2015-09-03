<html><body><p>Todo empezó con <a href="http://www.gleducar.org.ar/pipermail/gleducar/2006-September/003388.html">este mail en la lista del Gleducar</a>.

<!--more-->

La entrada: una lista de palabras representables en una calculadora normal simplemente girando el display. 



Esto parece algo sin mucha utilidad, pero esta técnica es utilizada en muchos dispositivos con capacidades gráficas reducidas para mostrar mensajes de error u otra informaición adicional a la salida numérica.



En este archivo están las palabras a procesar enviadas a la lista de correos (en la selección original de palabras no se incluyeron aquellas con la letra 'z', pero también podrían haber sido elejidas para representar en Alfabeto Calculadora): <a href="http://firebirds.com.ar/~juanjo/wordpress/files/python/palabras.txt">palabras.txt</a>



</p><h2>El programa</h2>

Almuerzo de por medio escribí este código y lo mandé a la lista del Gleducar como respuesta al reto: <a href="http://firebirds.com.ar/~juanjo/wordpress/files/python/alfabeto_calc.py.html">alfabeto_calc.py</a> (<strong>update:</strong> tiene la corrección que me sugirió Alecu)



La forma de representación que elejí es esta: tomar todas las letras y conviértalas a mayúsculas excepto a la 'h' ('h' puede representarse con un '4' de calculadora invertido, pero 'H' no se puede representar con ningún número). Podemos representar la 'l' en minúsculas o en mayúscula ('L'), al usar la mayúscula y representarla con el '7', nos guardamos el '1' para la 'I'. Una vez que se tiene la palabra en formato <em>upper_except_h</em> cambiar cada letra por el número correspondiente e invertir el orden de los números.



<h2>Links para leer un poco más</h2>

<ul>

	<li><a href="http://en.wikipedia.org/wiki/List_of_calculator_words">http://en.wikipedia.org/wiki/List_of_calculator_words</a></li>

	<li><a href="http://en.wikipedia.org/wiki/Calculator_spelling">http://en.wikipedia.org/wiki/Calculator_spelling</a></li>

</ul>



<h2>Resultado</h2>

Esta es la salida que se obtiene al correr el programa en una terminal con el archivo <a href="http://firebirds.com.ar/~juanjo/wordpress/files/python/palabras.txt">palabras.txt</a> en el mismo directorio:





be = BE = 38

bebe = BEBE = 3838

bebible = BEBIBLE = 3781838

beisbol = BEISBOL = 7085138

belio = BELIO = 01738

bello = BELLO = 07738

beso = BESO = 0538

bielgo = BIELGO = 097318

bilioso = BILIOSO = 0501718

bilis = BILIS = 51718

biologo = BIOLOGO = 0907018

bis = BIS = 518

bisbiseo = BISBISEO = 03518518

bisel = BISEL = 73518

biso = BISO = 0518

bobilis = BOBILIS = 5171808

bobillo = BOBILLO = 0771808

bobo = BOBO = 0808

bohio = BOhIO = 01408

boi = BOI = 108

bolillo = BOLILLO = 0771708

bollo = BOLLO = 07708

bolo = BOLO = 0708

bolsillo = BOLSILLO = 07715708

bolso = BOLSO = 05708

e = E = 3

eh = Eh = 43

el = EL = 73

ele = ELE = 373

elegible = ELEGIBLE = 37819373

eliseo = ELISEO = 035173

elisio = ELISIO = 015173

elle = ELLE = 3773

ello = ELLO = 0773

elogio = ELOGIO = 019073

elogioso = ELOGIOSO = 05019073

eolio = EOLIO = 01703

es = ES = 53

ese = ESE = 353

eso = ESO = 053

gel = GEL = 739

geologo = GEOLOGO = 0907039

giboso = GIBOSO = 050819

gil = GIL = 719

gili = GILI = 1719

gis = GIS = 519

globo = GLOBO = 08079

globoso = GLOBOSO = 0508079

gobio = GOBIO = 01809

gol = GOL = 709

goloso = GOLOSO = 050709

he = hE = 34

helio = hELIO = 01734

heliosis = hELIOSIS = 51501734

hibleo = hIBLEO = 037814

hiel = hIEL = 7314

hielo = hIELO = 07314

higo = hIGO = 0914

hilo = hILO = 0714

hiogloso = hIOGLOSO = 05079014

hobo = hOBO = 0804

ibis = IBIS = 5181

ilegible = ILEGIBLE = 37819371

ileo = ILEO = 0371

ileso = ILESO = 05371

le = LE = 37

legible = LEGIBLE = 3781937

lego = LEGO = 0937

leible = LEIBLE = 378137

lelili = LELILI = 171737

lelo = LELO = 0737

leo = LEO = 037

les = LES = 537

lesbio = LESBIO = 018537

leso = LESO = 0537

libelo = LIBELO = 073817

libio = LIBIO = 01817

liego = LIEGO = 09317

ligio = LIGIO = 01917

lilili = LILILI = 171717

lio = LIO = 017

lioso = LIOSO = 05017

lis = LIS = 517

lisis = LISIS = 51517

liso = LISO = 0517

lo = LO = 07

lobo = LOBO = 0807

loboso = LOBOSO = 050807

logis = LOGIS = 51907

o = O = 0

obelo = OBELO = 07380

obeso = OBESO = 05380

oboe = OBOE = 3080

obolo = OBOLO = 07080

obseso = OBSESO = 053580

oh = Oh = 40

oible = OIBLE = 37810

oislo = OISLO = 07510

ole = OLE = 370

oleo = OLEO = 0370

oleoso = OLEOSO = 050370

os = OS = 50

oseo = OSEO = 0350

oso = OSO = 050

se = SE = 35

sebe = SEBE = 3835

sebillo = SEBILLO = 0771835

sebo = SEBO = 0835

seboso = SEBOSO = 050835

seis = SEIS = 5135

seise = SEISE = 35135

sello = SELLO = 07735

seo = SEO = 035

ses = SES = 535

seseo = SESEO = 03535

sesgo = SESGO = 09535

seso = SESO = 0535

si = SI = 15

sibil = SIBIL = 71815

sieso = SIESO = 05315

sigilo = SIGILO = 071915

sigiloso = SIGILOSO = 05071915

siglo = SIGLO = 07915

silbo = SILBO = 08715

silboso = SILBOSO = 0508715

silesio = SILESIO = 0153715

silo = SILO = 0715

siseo = SISEO = 03515

so = SO = 05

sobeo = SOBEO = 03805

sobo = SOBO = 0805

sois = SOIS = 5105

sol = SOL = 705

soleo = SOLEO = 03705

solio = SOLIO = 01705

solo = SOLO = 0705

sos = SOS = 505

sosiego = SOSIEGO = 0931505

soso = SOSO = 0505 </body></html>