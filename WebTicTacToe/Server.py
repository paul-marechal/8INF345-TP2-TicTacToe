# -*- coding:utf8 -*-
from .modules import WebServer

__all__ = ['Server']

# Yes, this lib imports an instance
Server = WebServer()

# Route seems messy but its fine, really...
@Server.addRoute(r'.*\.(html?|js|css|jpg|png|gif)')
def resourceAccess(path, handler, **_):
    """This first method should serve any resource file"""
    return Server.getFileContent(path)
