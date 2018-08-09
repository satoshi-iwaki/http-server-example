#! /usr/bin/python
# -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler, HTTPServer
# import ssl
import hashlib
import time

hostname = '127.0.0.1'
port = 8081

class HelloHandler(BaseHTTPRequestHandler):
	def do_POST(self):
		if self.path=="/api/digest":
			length = int(self.headers['Content-Length'])
			content = self.rfile.read(length)
			digest = hashlib.sha256(content).hexdigest();
			message = '{{"content" : "{}", "digest" : "{}"}}'.format(str(content, encoding='utf-8'), digest)

			self.send_response(200)
			self.send_header('Content-Type', 'application/json')
			self.send_header('Content-Length', str(len(message)))
			self.end_headers()
			self.wfile.write(bytes(message, 'utf-8'))
		else:
			self.send_error(404,'File Not Found: %s' % self.path)
		return

httpd = HTTPServer((hostname, port), HelloHandler)
print(time.asctime(), "Server Starts - %s:%s" % (hostname, port))

try:
	httpd.serve_forever()
except KeyboardInterrupt:
	pass

httpd.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostname, port))

