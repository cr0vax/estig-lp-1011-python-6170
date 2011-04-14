# -*- coding: utf-8 -*-

# Servidor HTTP com as páginas de estatísticas
import SimpleHTTPServer
import SocketServer
from KThread import *

class HttpServer (threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def stop (self):
        self.server.kill()
        print "HTTP server stopped"
        pass
    pass

    def stopped (self):
        return self._stop.isSet()
        pass
    pass
    
    def start (self):
        self.server = KThread(target=self.start_thread)
        self.server.start()
        pass
    pass

    def start_thread (self):
        PORT = 8000                     # port used by the http server
        
        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = SocketServer.TCPServer(('', PORT), Handler)
        
        print "HTTP serving at port", PORT
        httpd.serve_forever()
        pass
    pass
    