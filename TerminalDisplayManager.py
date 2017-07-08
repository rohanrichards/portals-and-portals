# class for managing the rendering of game elements to a terminal window

from Tile import Tile
from Board import Board
import sys

class TerminalDisplayManager:
    tileHeight = 4;
    tileWidth = 10;
    innerTileHeight = 3;
    innerTileWidth = 8;

    # constructor
    def __init__(selfself):
        print("Created a TerminalDisplayManager instance");

    def drawTile(self, row, tile):
        # draws the requested row number of the tile
        # draws any relevant tile data (players present, tile number, portals etc)
        # Params:
        #   row=the row of the tile to draw (int)
        #   tile=instance of a Tile object (Tile)

        tileCapRow = "---------";
        playerString = "     ";
        for player in tile.players:
            playerString = player.token + playerString;
            playerString = playerString[:len(playerString)-1] + playerString[len(playerString):];


        playersRow = "|  "+ playerString + " ";
        tileNumberRow = "|   " + str(tile.tileNumber) + self.tileNumberSpace(tile.tileNumber) + "   ";
        portalRow = "|        ";

        rows = [
            tileCapRow,
            playersRow,
            tileNumberRow,
            portalRow
        ]

        sys.stdout.write(rows[row]);

    def tileNumberSpace(self, number):
        # just returns a space if the number is smaller than 10
        # its padding for single digit numbers in the tile rendering
        if number < 10:
            return " ";
        else:
            return "";

    def drawBoard(self, board):
        # draws the game board
        # Params:
        #   board=instance of the board to draw (Board)

        for row in range(0, board.height):
            #for each row of tiles
            for tileRow in range(0, self.tileHeight):
                #for each row in a tile (row of characters)
                for col in range(0, board.width):
                    #for each column of tiles
                    if row % 2:
                        #on odd rows the highest number in the range needs to come first
                        #have to use -1 and +1 because of starting at zero (2nd row needs to multiply by 2, not 1)
                        index = (board.width * (row + 1)) - (col + 1);
                        self.drawTile(tileRow, board.tiles[index]);
                    else:
                        #get current col (from 0 to board width)
                        #find a row multiple and add it to col
                        index = col + (board.width * row);
                        self.drawTile(tileRow, board.tiles[index]);
                sys.stdout.write("\n");

# test code to just run through the methods
# this wont exist in prod and will get called by the view class
testClass = TerminalDisplayManager();
testClass.drawBoard(Board())
print("Player 1's turn (%)");
print("1. Roll Dice");
print("2. Quit Game");