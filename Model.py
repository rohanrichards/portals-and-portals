from Board import Board
from random import randint

class Model:

    def __init__(self, controller):
        self.board = Board();
        self.controller = controller;
        # print("board init")

    def getActivePlayer(self):
        #returns the currently active player
        for player in self.board.players:
            if player.isActive:
                return player;

    def setHumanPlayers(self):
        userInput = self.countHumanPlayers()
        userInput = int(input('How many players (max {})?'.format(self.board.maxPlayers)))
        while userInput not in range(1, self.board.maxPlayers + 1):
            userInput = int(input('Try again. How many players (max {})?'.format(self.board.maxPlayers)))
        for i in range(len(self.board.players)):
            if i < userInput:
                self.board.players[i].ai = False
            else:
                self.board.players[i].ai = True

    def setHumanNames(self):
        # print('setting up names')
        for i in range(0, self.countHumanPlayers()):
            self.board.players[i].name = input ('Player {} enter your name: '.format(self.board.players[i].name))
            while len(self.board.players[i].name) not in range(1,21):
                self.board.players[i].name = input('Must be between 1 and 21 characters. Player {} enter your name: '.format(self.board.players[i].name))

    def countHumanPlayers(self):
        # helper function to count the number of human players
        count = 0;
        for player in self.board.players:
            if player.ai == False:
                count += 1;
        return count;

    def resetBoard(self):
        self.board = None;
        self.turncount = 0;
        self.board = Board();

    def movePlayerBySpaces(self, player, spaces):
        if (player.location + spaces + 1) >= 40:
            moveTile = 40;
        else:
            moveTile = player.location + spaces + 1
        print("Moving " + player.name + " from tile " +str(player.location + 1) + " to tile " +
              str( moveTile ))
        destIndex = player.location + spaces;

        player.tilesmoved = player.tilesmoved + spaces;

        if destIndex >= 39:
            destIndex = 39;
        self.movePlayerToTile(player, destIndex);
        self.portalCheck(player, destIndex);

    def movePlayerToTile(self, player, index):
        # move a player to a new tile
        currentTile = self.board.tiles[player.location];
        destinationTile = self.board.tiles[index];

        #remove it from the current tile
        currentTile.players.remove(player);
        #add it to the new tile
        destinationTile.players.append(player);
        #update its local location variable
        player.location = index;

    def portalCheck(self, player, index):
        #checks if a player has landed on a portal
        #moves them through the portal if they have
        if self.board.tiles[index].portal:
            print("You slipped into a portal!")
            portal = self.board.tiles[index].portal;
            player.portalsactivated = player.portalsactivated + 1
            destination = portal.destination;
            origin = portal.origin;

            if player.location == origin:
                #player is at the head of the portal
                #so we move them to the portals destination
                self.movePlayerToTile(player, destination)
                print("Phew! It was a shortcut!")
                print("You appeared at tile "+ str(destination+1))
            else:
                #player is at the tail of the portal
                #so we have to move them to the origin
                self.movePlayerToTile(player, origin)
                print("Oh no! It lead you backwards!")

                print("You appeared at tile "+ str(origin+1))

    def rollDice(self):
        #randomisation of die roll returns between (1-6)
        return randint(1,30);
        # return 15;


    def setNextActivePlayer(self):
        playerIndex = 0;
        nextPlayerIndex = 1;
        for player in self.board.players:
            if player.isActive:
                if playerIndex == self.board.maxPlayers - 1:
                    nextPlayerIndex = 0;
                else:
                    nextPlayerIndex = playerIndex + 1;
                player.isActive = False;
            playerIndex += 1;
        self.board.players[nextPlayerIndex].isActive = True;

    def randomizePortalsTest(self):
        self.board.tryRandomizePortals();

    def resetTokens(self):
        for player in self.board.players:
            self.movePlayerToTile(player, 0);

    def resetActivePlayer(self):
        #just resets the active player back to player 1
        for player in self.board.players:
            player.isActive = False;
        self.board.players[0].isActive = True;