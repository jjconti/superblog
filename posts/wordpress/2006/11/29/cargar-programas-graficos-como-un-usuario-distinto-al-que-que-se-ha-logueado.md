<html><body><h2>Escenario</h2>

Te despertás en la mañana. El zumbido de la computadora se entremezcla con el canto de los pájaritos. Tu hermana la debe haber encendido temprano. Una ducha para terminar de despertarte. Café, masitas de agua (típico desayuno del día que te das cuenta que hay que ir al super a hacer las compras de la semana). La computadora está encendida, pensás en iniciar el cliente de correo para leer algunos mails. Usás Thunderbird (no necesariamente, pero si algún cliente gráfico). Encendés el monitor que está apagado y rápidamente reconocés el  wallpaper que tu hermana se hizo con la foto del novio. En la barra de tareas hay un programa minimizado: lees aMule 2.0.3. Click. Decenas de barritas de colores, algunas ya se completaron de verde (hoy es un buen día para compartir música).



Abris una terminal:

<code>

marisu@sarge:~$ su juanjo

Password:

juanjo@sarge:/home/marisu$ thunderbird

Xlib: connection to ":0.0" refused by server

Xlib: No protocol specified

<br>

(thunderbird-bin:15655): Gtk-WARNING **: cannot open display:

juanjo@sarge:/home/marisu$

</code>

Oops!



Sos un buen hermano, así que no querés cortarle la descarga de música a tu hermana. Pero querés aprovechar mientras el café está aún caliente para leer tus mails. ¿Solución?

<!--more-->

<h2>Solución</h2>

<code>

juanjo@sarge:~$ exit

exit

marisu@sarge:~$ xhost +local:juanjo

non-network local connections being added to access control list

marisu@sarge:~$ su juanjo

Password:

juanjo@sarge:/home/marisu$ thunderbird

</code>



Dejo este post por que hoy a la mañana no recordaba el comando y estuve unos 10 minutos en google hasta encontrarlo, espero a alguien le sirva! ¿Alguna otra forma de solucionar el problema?



Saludos!</body></html>