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

    def countHumanPlayers(self):
        # helper function to count the number of human players
        count = 0;
        for player in self.board.players:
            if player.ai == False:
                count += 1;
        return count;

    def resetBoard(self):
        self.board = None;
        self.board = Board();

    def movePlayerBySpaces(self, player, spaces):
        print("Moving " + player.name + " by " + str(spaces) + " spaces!")
        destIndex = player.location + spaces;
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
        if self.board.tiles[index].portal:
            print("You found a portal here!")
            portal = self.board.tiles[index].portal;
            destination = portal.destination;
            origin = portal.origin;

            if(player.location == origin):
                #player is at the head of the portal
                self.movePlayerToTile(player, destination)
                print("Phew! It was a shortcut!")
                print("You appeared at "+ str(destination+1))
            else:
                self.movePlayerToTile(player, origin)
                print("Oh no! It lead you backwards!")
                print("You appeared at "+ str(origin+1))

    def rollDice(self):
        #randomisation of die roll returns between (1-6)
        #return randint(1,6);
        return 1;
    
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