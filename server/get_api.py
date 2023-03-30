from http.server import BaseHTTPRequestHandler, HTTPServer
import json

listarry=[
    {'id':1,'todo':'list1'},
    {'id':2,'todo':'routing'}
]

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        if self.path == '/GET':
            message = json.dumps(listarry)
        else:
            message = '404 Not Found'

        self.wfile.write(message.encode('utf-8'))

server = HTTPServer(('127.0.0.1', 8000), RequestHandler)
print('Starting server, use <Ctrl-C> to stop')
server.serve_forever()