# -*- coding:utf8 -*-
from . import Server

@Server.addRoute(r"/test/{test}/.*")
def test(param, handler, **kargs):
    return param.get('test')
