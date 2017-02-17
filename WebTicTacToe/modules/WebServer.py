# -*- coding:utf8 -*-
import urllib.parse
import http.server
import os.path
import re

__all__ = ['WebServer', 'RouteHandler']

# Request handler
class RouteHandler(http.server.BaseHTTPRequestHandler):
    """ Original doc:
    https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler
    """

    Routes = {}

    def serve(self):
        """Generic serving method"""

        # Decode url and try to clean it
        decodedPath = urllib.parse.unquote(self.path)
        cleanPath = \
            urllib.parse.urljoin(decodedPath, ".") + \
            os.path.basename(decodedPath)

        # Parcour each route's regex
        for route, action in self.Routes.items():
            pathRegex = re.compile("^" + route + "$")
            matches = pathRegex.search(cleanPath)
            if matches is not None:
                return action(cleanPath, handler=self, matches=matches)

        # If nothing has been found...
        self.log_error("No route matching: " + cleanPath)
        self.send_error(404, "Not found")

    def do_GET(self): self.serve()
    def do_POST(self): self.serve()

# Actual server class
class WebServer(object):
    def __init__(self, address='localhost', port=80, baseDir='./www', handler=RouteHandler):
        self.HttpServer = None
        self.baseDir = baseDir
        self.handlerClass = handler
        self.address = address
        self.port = 80

    def getBaseDir(self):
        return os.path.realpath(self.baseDir)

    def initialize(self, **kargs):
        """Initialization"""
        self.baseDir = kargs.get('baseDir', self.baseDir)
        self.address = kargs.get('address', self.address)
        self.port = kargs.get('port', self.port)

        self.HttpServer = http.server.HTTPServer(
            (self.address, self.port),
            self.handlerClass
            )
        print("Server is initialized.")
        print("Base directory is: " + self.getBaseDir())

    def run(self):
        """Running the server"""
        try:
            self.HttpServer.serve_forever()
        except KeyboardInterrupt as e:
            self.stop()
        except Exception as e:
            print(e) # Show the error
            self.stop()

    def stop(self):
        """Stopping the server"""
        print("Server is shutting down.")

    def addRoute(self, route, code=200):
        """Decorator Generator
        Decorated prototype:
            func(path, handler, matches)"""

        def decorator(func):
            """Actual Decorator
            Tries to replace the route formating with re format
            {thing} becomes (?P<thing>\.+)
            """

            def modified(path, *margs, **mkargs):
                """Modified function returned"""
                handler = mkargs.get('handler', None)
                retval = None

                if handler is not None:

                    # Set the response code
                    handler.send_response(code)

                    # Run the decorated function
                    retval = func(path, *margs, **mkargs)

                    # End the headers
                    handler.end_headers()

                # Finally return the function's result
                return retval

            bracketsRegex = re.compile(r"{(\w+)}")
            formatedRoute = bracketsRegex.sub(r"(?P<\1>.+)", route)
            self.handlerClass.Routes[formatedRoute] = func

            # decorator -> modifiedFunction
            return modified

        # addRoute -> decorator
        return decorator

    def serveFile(self, path):
        """Tries to serve a file if it exists"""
        realpath = self.getBaseDir() + path
        print(realpath)
        return open(realpath, 'br') if os.path.isfile(realpath) else None

    def serveFileContent(self, path):
        """Serves the content of a file, if it exists"""
        content = None
        file = self.serveFile(path)
        if file is not None:
            content = file.read()
            file.close()
        return content
