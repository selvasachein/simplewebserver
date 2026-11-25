import http.server
import socketserver
import socket
import platform

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

with socketserver.TCPServer(("", PORT), MyHandler) as server:
    print("Server started at http://localhost:8000")
    print("Operating System:", platform.system())
    print("Computer Name:", socket.gethostname())
    server.serve_forever()