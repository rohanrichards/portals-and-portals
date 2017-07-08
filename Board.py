# Class for defining a game board

from Tile import Tile
from Player import Player

class Board:
    tiles = [];
    height = 5;
    width = 8;
    maxPlayers = 4;
    playerTokens = ["@", "#", "%", "$"];

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
            self.tiles[0].players.append(player);

        playersArray = self.tiles[1].players;
        # print(playersArray);
        # playersArray.append(players[0]);
        # self.tiles[0].players = players;
        # print(self.tiles[0].players)
        # print(self.tiles[1].players)
        # print(self.tiles[2].players)