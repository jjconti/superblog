<html><body><p>Buscando información sobre diseño de lenguajes de programación (<em>just for fun</em>) me topé con un artículo que relaciona este tópico con los libros de Harry Potter (de los que soy un <a title="Lecturas de verano" href="http://www.juanjoconti.com.ar/2007/03/21/lecturas-de-verano/" target="_blank">feliz lector</a>). Para darle más fuerza a la casualidad, el autor del artículo es la misma persona que creó <a title="Aprendiendo Python" href="http://www.juanjoconti.com.ar/category/aprendiendo-python/" target="_blank">el lenguaje de programación que más me gusta</a>.



Me tomo la libertad de traducir <a title="HP Theory" href="http://www.artima.com/weblogs/viewpost.jsp?thread=123234" target="_blank">este artículo</a> de Guido Van Rossum, creador del lenguaje de programación <a title="Python" href="http://www.python.org/">Python</a>.

</p><h2>La Teoría de Harry Potter para el Diseño de Lenguajes de Programación</h2>

<em>por Guido van Rossum</em>

14 de Agosto de 2005

<h3>Resumen</h3>

Una comparación alegre de como exitosos autores de ficción y diseñadores de lenguajes de programación pueden por accidente encontrar en su primer trabajo las pistas de sus éxitos futuros.

<!--more-->

<h3>La teoría</h3>

Me encanta leer los libros de Harry Potter, y recientemente se me ocurrió una analogía interesante entre escribir series de libros de ficción y diseñar lenguajes de programación.



Estoy seguro de esto: cuando J.K. Rowling escribió el primer libro de Harry Potter (como el primero de una serie de siete) había desarrollado una buena idea de las cosas que eventualmente iban a pasar en la serie pero no tenía la idea exacta de lo que iba a pasar en los restantes libros, tampoco todos los detalles de cómo funcionaría la magia en el mundo que estaba creando.



También estoy asumiendo que a medida que iba escribiendo los volúmenes sucesivos, volvía a los primeros libros para rescatar detalles que habían sido introducidos solo para darle color a la historia y darles un nuevo significado. Por ejemplo, dudo que cuando inventó el nombre Voldemort ya haya pensado que "I am Lord Voldemort" (Yo soy el Señor Voldemort) sería un anagrama de "Tom Marvolo Riddle" (Tom Riddle no es un nombre muy convincente para quien terminaría siendo la persona más mala del mundo, pero aparentemente no pudo encontrar un buen anagrama para Voldemort solo). Tampoco pienso que haya pensado que la patética rata de Ron, Scrabbers, sería un animago (el hecho de que le falte un dedo, al menos en lo que yo se, no aparece en ninguno de los dos primeros libros). Creo que ya captaron mi idea.



De forma similar, no había pensado en  iteradores o generadores cuando  se me ocurrió por primera vez el for-loop de Python o  usar % como un operador para el formateo de <em>strings</em>, y de hecho, usar 'def' para definir tanto funciones como métodos tampoco fue parte del plan inicial.



De la misma forma en que los sucesivos libros de Harry Potter requieren tener continuidad (el gusto de Dumblendor por los dulces no puede cambiar drásticamente en el tercer libro), las versiones sucesivas de Python están limitadas por serios requerimientos de compatibilidad hacia atrás.



A veces es fácil volver y generalizar una característica, por ejemplo, trasnformar las funciones de conversión int(), str() y list() en clases. Por otro lado, una reciente discusión en python-dev sobre la jerarquía de las excepciones (<a title="PEP 348" href="http://www.python.org/dev/peps/pep-0348/" target="_blank">PEP 348</a>) ha mostrado que deciciones anteriores pueden ser menos que ideales. Las inconsistencias en la convención de nombres y la calidad del API son otro ejemplo.



<strong>Comentarios</strong> al artículo original: <a title="Comments on HP Theory" href="http://www.artima.com/forums/flat.jsp?forum=106&amp;thread=123234" target="_blank">http://www.artima.com/forums/flat.jsp?forum=106&amp;thread=123234</a>



<strong>Correcciones:</strong> por desconocer cuestiones internas del lenguaje o de mi traducción en sí son bienvenidas.</body></html>