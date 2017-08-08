# Class for defining a game board

from Tile import *
from Player import Player
from random import randint
from random import sample


import sys
from random import randint
from random import sample

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

    maxPortals = 6; #max portals ever possible on the board
    minPortals = 2; #min portals ever possible on the board
    randomizePortalsChance = 30; #the percent chance to randomize portals each turn
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
        # use this if you cant easily get a reference to the portal itself (you only know where it is)
        if(tile.portal):
            self.destroyPortal(tile.portal);

    def getActivePlayer(self):
        #returns the currently active player
        for player in self.players:
            if player.isActive:
                return player;

    def tryRandomizePortals(self):
        # roll a dice to see if its time to randomize the portals
        roll = randint(0,100);
        # print("Chance to randomize portals: " + str(roll));
        if(roll <= self.randomizePortalsChance):
            print("The portals are shifting!")
            self.randomizePortals();

    def randomizePortals(self):
        # randomizes all of the portals
        # never call this directly, use tryRandomizePortals
        self.portals = [];

        #strip out all the old portals;
        self.removeAllPortals();

        numberOfPortals = randint(self.minPortals, self.maxPortals);
        tileRange = (self.height * self.width) - 1; #minus one because we want to reference an array
        portalRange = sample(range(0, tileRange), numberOfPortals * 2)
        x = 0;

        for i in range(numberOfPortals):
            firstEnd = portalRange[x]
            secondEnd = portalRange[x+1]
            if firstEnd < secondEnd:
                portalHeadLocation = firstEnd;
                portalTailLocation = secondEnd;
            else:
                portalHeadLocation = secondEnd;
                portalTailLocation = firstEnd;
            x = x + 2

            self.portals.append(Portal(portalHeadLocation, portalTailLocation));

        self.setupPortals();


    def removeAllPortals(self):
        #remove every portal from the board
        for tile in self.tiles:
            self.destroyPortalAtTile(tile);