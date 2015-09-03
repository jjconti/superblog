<html><body><p>Anoche estuve jugando un poco con los datos (publicados) del escrutinio provisorio de las elecciones a gobernador en la provincia de Santa Fe.



La misma noche de las elecciones, cuando los resultados provisorios no lo favorecieron, Miguel del Sel y los partidarios del PRO en general empezaron a <a href="http://www.ellitoral.com/index.php/id_um/114934-del-sel-vamos-a-contar-voto-por-voto-porque-queremos-saber-la-verdad" target="_blank">instalar una sospecha de fraude</a>. No tardaron en hacerse eco en las redes sociales distinto tipo de usuarios: obsecuentes, tira bombas, paranoicos, ingenuos.



En distintos medios, Del Sel mostró como "prueba" del fraude errores producidos al realizar la carga manual de datos durante el escrutinio provisorio, es decir durante el proceso humano de mirar una planilla completada a mano e ingresar (tipeando) los valores en el sistema.



De los tipos de errores, voy a tomar uno, el primero que mostró (<a href="http://www.lanacion.com.ar/1802244-miguel-del-sel-pasan-cosas-extranas-hay-mesas-en-las-que-figuro-con-cero-votos-y-tengo-73" target="_blank">1</a>, <a href="https://youtu.be/vsmUzNNMahw" target="_blank">2</a>): <strong>el candidato figura con 0 votos en el sitio web, pero en la planilla tiene X votos.</strong>



Mi objetivo es ver cuantas veces se da este error y como afecta a los distintos candidatos.



Programé un <a href="https://github.com/jjconti/escrutinio/blob/master/escrutinio.py" target="_blank">pequeño script</a> que hace lo siguiente:

</p><ol>

	<li>Baja el archivo XML con los datos de la categoría Gobernador correspondiente a cada mesa.</li>

	<li>Lee los archivos XML para obtener, para cada mesa, la cantidad de votos de los 3 partidos dominantes.</li>

	<li>Encuentra las mesas en las que cada partido tiene 0 votos.

<ol>

	<li>Si en una mesa los 3 candidatos tienen 0 votos, se asume que se trata de una mesa con telegrama desestimado.</li>

</ol>

</li>

</ol>

Luego revisé los archivos PDF de los telegramas de estas mesas. Arribé a lo siguiente:

<table dir="ltr" border="1" cellspacing="0" cellpadding="0"><colgroup> <col width="100"> <col width="100"> <col width="136"> <col width="100"></colgroup>

<tbody>

<tr>

<td data-sheets-value='[null,2,"Partido"]'>Partido</td>

<td data-sheets-value='[null,2,"N\u00ba de mesa"]'>Nº de mesa</td>

<td data-sheets-value='[null,2,"Votos en el telegrama"]'>Votos</td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"PRO"]'>PRO</td>

<td data-sheets-value="[null,3,null,1725]">1725</td>

<td data-sheets-value="[null,3,null,0]">0</td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"PRO"]'>PRO</td>

<td data-sheets-value="[null,3,null,270]">270</td>

<td data-sheets-value="[null,3,null,73]">73</td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"PRO"]'>PRO</td>

<td data-sheets-value="[null,3,null,5351]">5351</td>

<td data-sheets-value="[null,3,null,0]">0</td>

<td data-sheets-value='[null,2,"*"]'>*</td>

</tr>

<tr>

<td colspan="2" rowspan="1" data-sheets-value='[null,2,"Total votos faltantes PRO"]'>Total votos faltantes PRO</td>

<td data-sheets-value="[null,3,null,73]" data-sheets-numberformat="[null,0]" data-sheets-formula="=sum(R[-3]C[0]:R[-1]C[0])"><span style="color: #ff0000;"><span style="color: #000000;"><b>73</b></span></span></td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"FPV"]'>FPV</td>

<td data-sheets-value="[null,3,null,1478]">1478</td>

<td data-sheets-value="[null,3,null,0]">0</td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"FPV"]'>FPV</td>

<td data-sheets-value="[null,3,null,7591]">7591</td>

<td data-sheets-value="[null,3,null,0]">0</td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"FPV"]'>FPV</td>

<td data-sheets-value="[null,3,null,5545]">5545</td>

<td data-sheets-value="[null,3,null,0]">0</td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"FPV"]'>FPV</td>

<td data-sheets-value="[null,3,null,4912]">4912</td>

<td data-sheets-value="[null,3,null,0]">0</td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"FPV"]'>FPV</td>

<td data-sheets-value="[null,3,null,7601]">7601</td>

<td data-sheets-value="[null,3,null,0]">0</td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"FPV"]'>FPV</td>

<td data-sheets-value="[null,3,null,1845]">1845</td>

<td data-sheets-value="[null,3,null,0]">0</td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"FPV"]'>FPV</td>

<td data-sheets-value="[null,3,null,4950]">4950</td>

<td data-sheets-value="[null,3,null,0]">0</td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"FPV"]'>FPV</td>

<td data-sheets-value="[null,3,null,4729]">4729</td>

<td data-sheets-value="[null,3,null,85]">85</td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"FPV"]'>FPV</td>

<td data-sheets-value="[null,3,null,6555]">6555</td>

<td data-sheets-value="[null,3,null,0]">0</td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"FPV"]'>FPV</td>

<td data-sheets-value="[null,3,null,6333]">6333</td>

<td data-sheets-value="[null,3,null,0]">0</td>

<td data-sheets-value='[null,2,"*"]'>*</td>

</tr>

<tr>

<td colspan="2" rowspan="1" data-sheets-value='[null,2,"Total votos faltantes FPV"]'>Total votos faltantes FPV</td>

<td data-sheets-value="[null,3,null,85]" data-sheets-numberformat="[null,0]" data-sheets-formula="=sum(R[-10]C[0]:R[-1]C[0])"><span style="color: #000000;"><strong>85</strong></span></td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"FPCS"]'>FPCS</td>

<td data-sheets-value="[null,3,null,6852]">6852</td>

<td data-sheets-value="[null,3,null,0]">0</td>

<td data-sheets-value='[null,2,"*"]'>*</td>

</tr>

<tr>

<td data-sheets-value='[null,2,"FPCS"]'>FPCS</td>

<td data-sheets-value="[null,3,null,1478]">1478</td>

<td data-sheets-value="[null,3,null,0]">0</td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"FPCS"]'>FPCS</td>

<td data-sheets-value="[null,3,null,134]">134</td>

<td data-sheets-value="[null,3,null,0]">0</td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"FPCS"]'>FPCS</td>

<td data-sheets-value="[null,3,null,7591]">7591</td>

<td data-sheets-value="[null,3,null,0]">0</td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"FPCS"]'>FPCS</td>

<td data-sheets-value="[null,3,null,5485]">5485</td>

<td data-sheets-value="[null,3,null,82]">82</td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"FPCS"]'>FPCS</td>

<td data-sheets-value="[null,3,null,4501]">4501</td>

<td data-sheets-value="[null,3,null,75]">75</td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"FPCS"]'>FPCS</td>

<td data-sheets-value="[null,3,null,6555]">6555</td>

<td data-sheets-value="[null,3,null,0]">0</td>

<td></td>

</tr>

<tr>

<td data-sheets-value='[null,2,"FPCS"]'>FPCS</td>

<td data-sheets-value="[null,3,null,1845]">1845</td>

<td data-sheets-value="[null,3,null,0]">0</td>

<td></td>

</tr>

<tr>

<td colspan="2" rowspan="1" data-sheets-value='[null,2,"Total votos faltantes FPCS"]'>Total votos faltantes FPCS</td>

<td data-sheets-value="[null,3,null,157]" data-sheets-numberformat="[null,0]" data-sheets-formula="=sum(R[-8]C[0]:R[-1]C[0])"><span style="color: #000000;"><strong>157</strong></span></td>

<td></td>

</tr>

<tr>

<td colspan="3" rowspan="1" data-sheets-value='[null,2,"* la casilla estaba en blanco en el telegrama"]'>* la casilla estaba en blanco en el telegrama</td>

<td></td>

</tr>

</tbody>

</table>

Se pueden analizar otros tipos de errores en la carga, pero con uno me alcanza para demostrar mi punto: esto no es prueba ni de fraude ni del accionar de un cracker, solo errores humanos distribuidos uniformemente.



Es decir, <strong>este tipo de error ocurrió una vez para el PRO (a quien se le deben contabilizar 73 votos más), una vez para el FPV (a quien se le deben contabilizar 85 votos más) y 2 veces para el FPCS (a quien se le deben contabilizar 157 votos más).</strong>



Los datos y las herramientas están disponibles para periodistas y entusiastas que quieran seguir explorando el espectro de los votos mientras el tribunal <a href="http://www.ellitoral.com/index.php/id_um/115067-se-escrutaron-1500-urnas-y-se-abrieron-unas-45" target="_blank">sigue contando</a>.



Finalmente, como esto se puso muy serio, cierro con un poco de humor, uno de los mejores <a href="https://twitter.com/eameook" target="_blank">Eameos</a>:



<a href="/wp-content/uploads/2015/06/migueles.jpg"><img class="aligncenter size-full wp-image-5327" src="/wp-content/uploads/2015/06/migueles.jpg" alt="MI-DA-CHI" width="599" height="395"></a><strong>Actualización:</strong> <a href="http://www.juanjoconti.com.ar/2015/06/20/audio-de-la-entrevista-en-recreo-diario-sobre-mi-articulo-sobre-el-escrutinio-en-las-elecciones-santa-fe-2015/">audio disponible</a>.



 </body></html>