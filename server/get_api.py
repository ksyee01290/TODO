from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import json

listarry=[
    {'id':1,'todo':'list1'},
    {'id':2,'todo':'routing'}
]
next_id = 3

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/GET':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(listarry).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write("Error 404: Page not found".encode())

    
    def do_POST(self):
        global listarry,next_id,todo
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/POST':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            new_item = json.loads(post_data.decode())
            new_item['id'] = next_id
            next_id += 1
            listarry.append(new_item)
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(new_item).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write("Error 404: Page not found".encode())
        
if __name__ == '__main__':
    server = HTTPServer(('127.0.0.1', 8000), RequestHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()