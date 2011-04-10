# -*- coding: utf-8 -*-

# Servidor HTTP com as páginas de estatísticas
import SimpleHTTPServer
import SocketServer
import threading
from KThread import *

class HttpServer (threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def stop (self):
        #self._stop.set()
        self.A.kill()

    def stopped (self):
        return self._stop.isSet()
    
    def start (self):
        self.A = KThread(target=self.start_thread)
        self.A.start()

    def start_thread (self):
        PORT = 80                     # port used by the http server
        
        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = SocketServer.TCPServer(("localhost", PORT), Handler)
        
        print "serving at port", PORT
        httpd.serve_forever()
        pass
    pass