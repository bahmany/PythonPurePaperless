

import BaseHTTPServer
import cgi

class ReqHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_POST(self):
        print "GOT POST-REQUEST ",self.path
        env={}
        env['REQUEST_METHOD'] = self.command
        env['CONTENT_TYPE'] = self.headers.typeheader or self.headers.type
        env['CONTENT_LENGTH'] = self.headers.getheader('content-length') or -1
        print "Creating fieldstorage from",self.rfile
        fs = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ=env)  # triggers bug (hangs)
        print "Done, fs=",fs
        self.send_response(200)
        self.end_headers()
        self.wfile.write("okay")
        print "waiting for next request...\n"
        
    
addr = ('',9000)
server = BaseHTTPServer.HTTPServer( addr, ReqHandler )
sa = server.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "... (only POST requests)"
server.serve_forever()


 	  	 
