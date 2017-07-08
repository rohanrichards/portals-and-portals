# Class for defining a game board

from Tile import Tile
from Player import Player

from termcolor import colored, cprint
# https://pypi.python.org/pypi/termcolor


class Board:
    tiles = [];
    height = 5;
    width = 8;
    maxPlayers = 4;
    playerTokens = [
        colored("@", "green", attrs=["blink"]),
        colored("#", "blue", attrs=["blink"]),
        colored("%", "magenta", attrs=["blink"]),
        colored("$", "yellow", attrs=["blink"])
    ];

    # collection of references to player objects
    players = [];

    def __init__(self):
        # create an empty board
        tileNumber = 1;
        for y in range(0, self.width * self.height):
            self.tiles.append(Tile(tileNumber));
            tileNumber += 1;

        players = [];
        for i in range(0, self.maxPlayers):
            name = "Player " + str(i + 1);
            player = Player(name, self.playerTokens[i], True);
            players.append(player);
            self.tiles[0].players.append(player);

        # players[3].isActive = True;
        # self.tiles[1].portal = 5;
        # self.tiles[4].portal = 2;
        # self.tiles[2].portal = 28;
        # self.tiles[27].portal = 3;