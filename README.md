# 8INF345-TP2-TicTacToe
Web Tic-Tac-Toe

Python help/test file:
https://gist.github.com/WKnight02/a5cb80b56e9148c03b6df61a5f24e1d8

Fonctionnalitées:
- Créer Partie
  - `/game/create/{username}`
  - Return: id (de la partie créée)
- Savoir si une partie existe encore
  - `/game/exists/{id}`
  - Return: True/False
- Liste des parties en attente
  - `/game/list`
  - Return: {id: playerName}
- Joindre une partie
  - `/game/join/{id}/{username}`
  - Return: True/False
- Afficher la grille
  - `/game/grid/{id}`
  - Return: grille
  - Si le joueur est en attente, renvoyer []
  - Si aucune partie existe avec id, renvoyer []
- Placer pion
  - `/game/play/{id}/{username}/{x}/{y}`
  - Return: True/False
- Savoir le tour
  - `/game/turn/{id}`
  - Return: playername
- Quitter la partie
  - `/game/quit/{id}/{username}`
  - Return: True
  - Supprimer la partie (complétement)

```python
# HELP

dictionnaire = {}
dictionnaire['key'] = 'value'

GameS = {}
GameS[id] = {...}

GameS[id]['turn'] += 1
Game = GameS['id']
Game['turn'] = 0
```
