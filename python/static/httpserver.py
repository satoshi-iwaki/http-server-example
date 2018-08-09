#! /usr/bin/python
# -*- coding: utf-8 -*-
from http.server import HTTPServer, SimpleHTTPRequestHandler
import time
import os

hostname = '127.0.0.1'
port = 8081

document_root_dir = os.path.expanduser('~/document_root')
os.chdir(document_root_dir)

httpd = HTTPServer((hostname, port), SimpleHTTPRequestHandler)
print(time.asctime(), "Server Starts - %s:%s" % (hostname, port))

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostname, port))
