import BaseHTTPServer
import time


class LongPollHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    
    def sendchunk(self, data):
        self.wfile.write(format(len(data), 'X'))
        self.wfile.write('\r\n')
        self.wfile.write(data)
        self.wfile.write('\r\n')
        self.wfile.flush()
        
        
    
    def do_GET(self):
        self.protocol_version = 'HTTP/1.1'
        self.send_response(200)
        self.send_header('Transfer-Encoding',  'chunked')
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        start = """
<html> 
<head><title>Longpoll</title></head>       
<body>
        ERE IAM JH<br/>"""
        
        self.sendchunk(start)
        
        for x in range(5):
            self.sendchunk("Tick = {}<br/>\r\n".format(x))
            time.sleep(1)

        self.sendchunk("</body></html>")
     
        self.sendchunk('')
        
     
     
if __name__ == '__main__':
    server_address = ('127.0.0.1', 8000)

    httpd = BaseHTTPServer.HTTPServer(server_address, LongPollHandler)
    httpd.serve_forever()