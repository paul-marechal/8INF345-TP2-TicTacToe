# -*- coding:utf8 -*-
from . import Server

games = {'counter': 0}

@Server.addRoute(r"/test/{test}/?")
def test(param, handler, **kargs):
    return param.get('test')


#crée une partie, renvoie son id
@Server.addRoute(r"/game/create/{username}/?")
def createGame(param, **kargs):
    username = param.get('username')
    grid = {}

    for i in range(3):
        for j in range(3):
            grid[i,j] = 0

    #si 'turn' est pair c'est au tour du 'player1', sinon 'player2'
    games[games['counter']] = {'player1': username, 'player2': None, 'grid': grid, 'turn': 0}
    games['counter'] += 1

    return games['counter'] - 1


#vérifie si une partie existe encore
@Server.addRoute(r"/game/exists/{id}/?")
def gameExists(param, **kargs):
    id = int(param.get('id'))

    if id in games:
        return True

    return False


#renvoie la liste des parties en attente
@Server.addRoute(r"/game/list/?")
def gameList(**kargs):
    list = {}

    for i in games.keys():
        if i != ('counter') and games[i]['player2'] == None:
            list[i] = games[i]['player1']

    return list


#est-ce qu'on devrait pas rajouter le username de celui qui veut rejoindre la partie ?
#ou est-ce qu'on utilise le username comme celui qui veut rejoindre ?
#vérifie que l'id et le username correspondent bien à une partie en attente
@Server.addRoute(r"/game/join/{id}/{username}/?")
def gameJoin(param, **kargs):
    id = int(param.get('id'))
    username = param.get('username')

    if id in games:
        if games[id]['player1'] == username and games[id]['player2'] == None:
            return True

    return False


#renvoie la grille de jeu
@Server.addRoute(r"/game/grid/{id}/?")
def gameGrid(param, **kargs):
    id = int(param.get('id'))

    if id in games:
        if games[id]['player2'] != None:
            return games[id]['grid']

    return {}


#vérifie qu'un coup peut être joué
@Server.addRoute(r"/game/play/{id}/{username}/{x}/{y}/?")
def gamePlay(param, **kargs):
    id = int(param.get('id'))
    username = param.get('username')
    x = int(param.get('x'))
    y = int(param.get('y'))

    if id in games:
        if games[id]['player2'] != None:
            #à vérifier si le joueur choisit une case entre 0 et 2 ou entre 1 et 3
            if x >= 0 and x <= 2 and y >= 0 and y <= 2:
                if games[id]['grid'][x,y] == 0:
                    if games[id]['player1'] == username and (games[id]['turn'] % 2) == 0:
                        games[id]['grid'][x,y] = 'X'
                    elif games[id]['player2'] == username and (games[id]['turn'] % 2) != 0:
                        games[id]['grid'][x,y] = 'O'
                    games[id]['turn'] += 1
                    return True

    return False


#renvoie le joueur qui doit jouer
@Server.addRoute(r"/game/turn/{id}/?")
def gameTurn(param, **kargs):
    id = int(param.get('id'))

    if id in games:
        if (games[id]['turn'] % 2) == 0:
            return games[id]['player1']
        else:
            return games[id]['player2']

    return None


#vérifie qu'une partie peut être supprimée et la supprime
@Server.addRoute(r"/game/quit/{id}/{username}/?")
def gameQuit(param, **kargs):
    id = int(param.get('id'))
    username = param.get('username')

    if id in games:
        if games[id]['player1'] == username or games[id]['player2'] == username:
            del games[id]
            return True

    return False
