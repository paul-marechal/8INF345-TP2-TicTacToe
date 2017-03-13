# -*- coding:utf8 -*-
from WebTicTacToe import Server
import WebTicTacToe.Game
import socket

ip = socket.gethostbyname(socket.gethostname())

Server.initialize(address=ip, baseDir="./ClientSide")
Server.run()
