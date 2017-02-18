# -*- coding:utf8 -*-
from .modules import WebServer

__all__ = ['TicTacToeServer']

Server = TicTacToeServer = WebServer()

# Route seems messy but its fine, really...
@Server.addRoute(r'.*\.(html?|js|css|jpg|png|gif)')
def resourceAccess(path, handler, **_):
    """This first method should serve any resource file"""
    content = Server.serveFileContent(path)
    if content is None:
        handler.send_error(404)
    else:
        handler.wfile.write(content)
