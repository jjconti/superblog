<html><body><p>Mi amigo Joel estudia Filosofía en <a title="UNR" href="http://www.unr.edu.ar" target="_blank">Rosario</a> y este fin de semana estuvimos charlando sobre <strong>lógica</strong>. Durante la charla me  enseño que los conectores lógicos se pueden pensar como relaciones entre conjuntos. Yo nunca los había visto así.



Esta forma de pensarlos es a veces muy útil y sirve para darnos cuenta cual es el conector indicado para representar cierto conocimiento. Por ejemplo, muchas veces me encontré queriendo representar conocimiento del tipo <em>"Los conejos son blancos"</em> y errónea e instintivamente escribía:

<code>

B(x): x es blanco

C(x): x es conejo</code>

<code>

C(x) ^ B(x)

</code>

Lo cual es un error. La forma correcta de representar ese conocimiento es:

<code>

C(x) -&gt; B(x)

</code>



La implicación entre C(x) y B(x) puede entenderse una forma muy simple:



C es el conjunto de todos los conejos y B es el conjunto de todas las cosas blancas.



Recordemos que la información que queremos representar es <em>"Los conejos son blancos"</em>, enfatisando: <em>Todos</em> los conejos son blancos. No hay conejos grises o negros, todos son blancos.



El ejemplo en cuestión no era este, sino otro, pero lo importante es que Joel me explicó que la implicación es equivalente a la relación entre conjuntos de inclusión e hizo un dibujo parecido a este:

</p><p style="text-align: center;"><img src="/wp-content/uploads/2007/10/conejos_blancos.png" alt="Conejos blancos"></p>

En el dibujo se ve claramente el exacto conocimiento que queríamos representar: si algo es conejo, entonces es blanco. Si pertenece al conjunto C entonces pertenece al conjunto B. Porque el conjunto B incluye al conjunto C. El conjunto de las cosas blancas incluye al conjunto de los conejos.



El resto de los conectores lógicos también pueden verse como relaciones entre conjuntos.

<!--more-->



<strong>AND : intersección</strong>



AND o conjunción, muchas veces simbolizado con ^, es verdadero cuando los dos predicados que conecta lo son. Así pues  <code>B(x) ^ A(x)</code> será verdadero cuando x pertenezca tanto a B como a A.



<img src="/wp-content/uploads/2007/10/and1.png" alt="AND sin corchetes">



<strong>OR: unión</strong>



OR o disyunción  es una relación menos estricta ya que para ser verdadera solo necesita que uno de sus predicados sea verdadero. En el ejemplo anterior, que x pertenezca a B o a A. Eventualmente podría pertenecer a ambos conjuntos.



<img src="/wp-content/uploads/2007/10/or1.png" alt="OR sin corchetes">



<strong>XOR: unión - intersección</strong>



Unión MENOS intersección. La disyunción exclusiva es verdadera cuando x pertenece exclusivamente a uno de los conjuntos, pero es falsa cuando pertenece a ambos.



<img src="/wp-content/uploads/2007/10/xor.png" alt="XOR">



<strong>-&gt; : inclusión</strong>



Es el caso del ejemplo de los conejos con el que empezó este post.



<img src="/wp-content/uploads/2007/10/imp1.png" alt="IMP sin corchetes">



<strong>&lt;-&gt; : mutua inclusión</strong>



La doble implicación es un caso especial de la implicación ya que se define como <code>A -&gt; B AND B -&gt; A</code>. Así mismo su representación en forma de conjuntos es un caso especial de la inclusión. En el dibujo puede verse claramente que cuando decimos <code>A(x) &lt;-&gt; B(x)</code> estamos diciendo que cualquier elemento x que pertenezca a A también pertenece a B.



<img src="/wp-content/uploads/2007/10/bimp.png" alt="bimp">



<strong>NOT : no pertenencia</strong>



Todos los conectores pueden pensarse como conjuntos: <code>NOT A(x)</code> significa que el elemento x no pertenece a A.

<p style="text-align: center;"><img src="/wp-content/uploads/2007/10/not.png" alt="NOT"></p>

Para finalizar: todos los conectores lógicos pueden pensarse como relaciones entre conjuntos. Si se crean conectores a partir de algunos de los listados anteriormente, también se podrán definir las relaciones entre conjuntos correspondientes.</body></html>