<html><body><p>Un par de noches atrás nos juntamos con los excompañeros de la facu en casa. Mi amigo <a href="http://nicocesar.com/" target="_blank">Nico</a> trajo su nuevo chiche, una camarita de alta resistencia que está haciendo furor por estos días: <a href="http://gopro.com/" target="_blank">GoPro</a>.



Una de las cosas que se puede hacer con la cámara es dejarla en algún lugar sacando fotos cada, por ejemplo, dos segundos. Luego, con un comando en Linux, puede generar un video. El resultado es muy bueno; muy acorde a lo acelerado que se vive en estos días y una forma de que los nerds avancemos varios casilleros en la escala social mostrando el artilugio.



Le pedí el pace mágico para tenerlo a mano si alguna vez me compro uno de estos aparatitos:



</p><pre lang="bash">

for a in $( seq -w 65 141); 

do ls /media/3837-3763/DCIM/100GOPRO/GOPR0$a.JPG &gt;&gt; lista.txt; done

mencoder mf://@lista.txt -mf fps=25:type=jpg  -lavcopts vcodec=mpeg4:vbitrate=3200000:mbd=2:mv0:trell:v4mv:cbp:last_pred=3:predia=2:dia=2:vmax_b_frames=2:vb_strategy=1:precmp=2:cmp=2:subcmp=2:preme=2:vme=5:naq:qns=2 -vf scale=1280:1024 -oac copy -audiofile soundtrack.mp3 -o video-1024.avi

</pre>

<center>

<iframe width="420" height="315" src="http://www.youtube.com/embed/ZKsxxhmeBqg" frameborder="0" allowfullscreen></iframe>

</center></body></html>