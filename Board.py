# Class for defining a game board

from Tile import *
from Player import Player

import sys

from termcolor import colored, cprint
# https://pypi.python.org/pypi/termcolor

class Board:
    portals = [
        Portal(3, 7),
        Portal(6, 10),
        Portal(14, 23),
        Portal(21, 27),
        Portal(18, 37),
        Portal(25, 30),
        Portal(35, 38),
    ]

    tiles = [];
    height = 5;
    width = 8;
    maxPlayers = 4;
    playerTokens = [
        colored("@", "green"),
        colored("#", "blue"),
        colored("%", "magenta"),
        colored("$", "yellow")
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

        players[0].isActive = True;

        self.setupPortals();
        # self.tiles[1].portal = 5;
        # self.tiles[4].portal = 2;
        # self.tiles[2].portal = 28;
        # self.tiles[27].portal = 3;
        self.destroyPortalAtTile(self.tiles[5]);


    def setupPortals(self):
        #iterate over portals collection and setup the tiles
        for portal in self.portals:
            originTile = self.tiles[portal.origin];
            originTile.portal = portal;
            destinationTile = self.tiles[portal.destination];
            destinationTile.portal = portal;
            # originTile.portal = destinationTile.tileNumber;
            # destinationTile.portal = originTile.tileNumber;

    def destroyPortal(self, portal):
        origin = self.tiles[portal.origin];
        dest = self.tiles[portal.destination];
        origin.portal = None;
        dest.portal = None;

    def destroyPortalAtTile(self, tile):
        if(tile.portal):
            self.destroyPortal(tile.portal);