import http.server

class HttpHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

        self.wfile.write(b'test')

class WebServer(object):
    def __init__(self, address='localhost', port=80):
        self.HttpServer = http.server.HTTPServer((address, port), HttpHandler)

    def run(self):
        self.HttpServer.serve_forever()
