# -*- coding:utf8 -*-
from .modules import WebServer

__all__ = ['Server']

# Yes, this lib imports an instance
Server = WebServer()

# Route seems messy but its fine, really...
@Server.addRoute(r'.*\.(html?|js|css|jpg|png|gif)')
def resourceAccess(path, **_):
    """This first method should serve any resource file"""
    return Server.getFileContent(path)

@Server.addRoute(r'.*/', index=float('inf'))
def defaultFileLookup(path, handler, **_):
    """This should serves files like index or stuff"""
    for f in Server.DefaultIndexes:
        content = Server.getFileContent(path + '/' + f)
        if content is not None:
            return content
