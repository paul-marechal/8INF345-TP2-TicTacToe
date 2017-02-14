import http.server

# Request handler
class HttpHandler(http.server.BaseHTTPRequestHandler):
    """ Original doc:
    https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler
    """

    Routes = {}

    def serve(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'<html><body>TEST</body></html>')

    def do_GET(self):
        self.serve()
    def do_POST(self):
        self.serve()

# Actual server class
class WebServer(object):
    def __init__(self, address='localhost', port=80):
        self.HttpServer = http.server.HTTPServer((address, port), HttpHandler)

    def run(self):
        try:
            self.HttpServer.serve_forever()
        except KeyboardInterrupt as e:
            self.stop()

    def stop(self):
        print("Server is shutting down.")
