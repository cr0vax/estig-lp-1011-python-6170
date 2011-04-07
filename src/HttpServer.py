# -*- coding: utf-8 -*-

# Servidor HTTP com as páginas de estatísticas
import SimpleHTTPServer
import SocketServer
from KThread import KThread

class HttpServer:
    
    PORT = 8000                     # port used by the http server
    server = KThread(target=self.start)
    
    def start_thread(self):
        self.server.start()
        pass
    pass
    
    def start(self):
        Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
        httpd = SocketServer.TCPServer(("./http", self.PORT), Handler)
        
        print "serving at port", self.PORT
        httpd.serve_forever()
        pass
    pass
    
    def stop(self):
        self.server.kill()
        pass
    pass

        
