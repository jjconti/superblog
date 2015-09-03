<html><body><p>Hoy un amigo necesitaba un servidor web para engañar a un programa. Cada vez que el programa iniciaba, se conectaba con un servidor web para verificar si había actualizaciones disponibles.



El nombre del host a dónde se hacía la petición era leído de un archivo de configuración, por lo que lo podíamos cambiar. El resto solo era levantar un servidor web que responda con la información apropiada.



En la librería estándar de <strong>Python</strong> tenemos todos los elementos necesarios para realizar la tarea. Luego de probar un poco, el resultado final fue algo como esto:



</p><pre>

PORT = 8090



from BaseHTTPServer import BaseHTTPRequestHandler

import SocketServer

import cgi



class MyHandler(BaseHTTPRequestHandler):



	def do_GET(self):

		self.send_response(200)

		self.end_headers()

        	self.wfile.write('1.9.1')



	def do_POST(self):

		form = cgi.FieldStorage(

			fp=self.rfile, 

			headers=self.headers,

			environ={'REQUEST_METHOD':'POST',

			'CONTENT_TYPE':self.headers['Content-Type'],

			})

		print form

		self.send_response(200)

		self.end_headers()

		self.wfile.write('1.9.1')



httpd = SocketServer.TCPServer(("", PORT), MyHandler)



print "serving at port", PORT

httpd.serve_forever()

</pre>

Levanta en <strong>localhost</strong> y responde la cadena '1.9.1' al ser consultado tanto por <strong>GET</strong> como por <strong>POST</strong> y en el caso de POST, también imprime los valores recibidos.</body></html>