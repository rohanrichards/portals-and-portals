# Class for defining a game board

from Tile import *
from Player import Player

import sys
from random import randint

from termcolor import colored, cprint
# https://pypi.python.org/pypi/termcolor

class Board:
    # the default portals for a new board
    portals = [
        # portal format is origin, destination
        Portal(3, 7),
        Portal(6, 10),
        Portal(14, 23),
        Portal(21, 27),
        Portal(18, 37),
        Portal(25, 30),
        Portal(35, 38),
    ]

    height = 5;
    width = 8;
    maxPlayers = 4;
    playerTokens = [
        colored("@", "green"),
        colored("#", "blue"),
        colored("%", "magenta"),
        colored("$", "yellow")
    ];


    # players = [];

    def __init__(self):
        # create an empty board
        self.tiles = [];

        # collection of references to player objects
        # these same instances also exist inside Tile objects
        self.players = [];

        tileNumber = 1;
        for y in range(0, self.width * self.height):
            self.tiles.append(Tile(tileNumber));
            tileNumber += 1;

        for i in range(0, self.maxPlayers):
            name = "Player " + str(i + 1);
            player = Player(name, self.playerTokens[i], False);
            self.players.append(player);
            self.tiles[0].players.append(player);

        #selects a random player to begin the game.
        self.players[randint(0,3)].isActive = True
        self.setupPortals();

    def setupPortals(self):
        #iterate over portals collection and setup the tiles
        for portal in self.portals:
            originTile = self.tiles[portal.origin];
            originTile.portal = portal;
            destinationTile = self.tiles[portal.destination];
            destinationTile.portal = portal;

    def destroyPortal(self, portal):
        #helper function to cleanly remove a portal
        origin = self.tiles[portal.origin];
        dest = self.tiles[portal.destination];
        origin.portal = None;
        dest.portal = None;

    def destroyPortalAtTile(self, tile):
        # helper function to cleanly remove a portal at a specific tile
        # use this if you cant easily get a reference to the portal itself
        if(tile.portal):
            self.destroyPortal(tile.portal);

    def getActivePlayer(self):
        #returns the currently active player
        for player in self.players:
            if player.isActive:
                return player;