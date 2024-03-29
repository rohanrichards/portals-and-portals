# class for managing the rendering of game elements to a terminal window

from Tile import Tile
from Board import Board
import sys

from termcolor import colored, cprint
# https://pypi.python.org/pypi/termcolor

class TerminalDisplayManager:
    tileHeight = 4;
    tileWidth = 10;
    innerTileHeight = 3;
    innerTileWidth = 8;

    # constructor
    def __init__(self):
        # print("Created a TerminalDisplayManager instance");
        pass;

    def drawSplashScreen(self, menuOptions):
        self.drawMenu(menuOptions);

    def drawPlayerSetupScreen(self, maxPlayers, playersList, tokens, selectedTokens):
        while True:
            userInput = input('How many players (0 - {})?'.format(maxPlayers));
            try:
                int(userInput)
            except ValueError:
                print("Please make a valid menu selection: ", end='')
                continue
            if int(userInput) not in range(0, maxPlayers + 1):
                print("Please make a valid menu selection: ", end='')
                continue
            else:
                break

        for i in range(len(playersList)):
            if i < int(userInput):
                playersList[i].ai = False;
            else:
                playersList[i].ai = True;

        for index, player in enumerate(playersList):
            if player.ai != True:
                self.setPlayerName(player);
                self.setPlayerToken(player, tokens, selectedTokens);
            else:
                player.name = "Bot " + str(index)
                print('Player {} is now known as {}'.format(index + 1, player.name))
                for token in tokens:
                    if token not in selectedTokens:
                        player.token = token;
                        selectedTokens.append(token);
                        print('{} has been allocated {} for their game token '.format(player.name,
                                                                                      player.token))
                        break

    def setPlayerName(self, player):
        valid = False;
        while valid == False:
            player.name = input('{} enter your name: '.format(player.name));
            if len(player.name) <= 10 and len(player.name) >= 1:
                valid = True;
                break;
            print("Name must be between 1 and 10 characters");

    def setPlayerToken(self, player, tokens, selectedTokens):
        print("{} select your game token: ".format(player.name));
        for index, token in enumerate(tokens):
            if token not in selectedTokens:
                print("{} {}  ".format((index + 1), token));
            else:
                print("{} {}  ".format((index + 1), '(taken)'));
        valid = False
        while valid == False:
                try:
                    playerInput = int(input("Enter token number: "));
                    if tokens[playerInput - 1] in selectedTokens[:]:
                        print('Token {} is not available, try again:'.format(tokens[playerInput - 1]));
                        continue
                    elif playerInput < 1:
                        raise IndexError
                    else:
                        player.token = tokens[playerInput - 1];
                        selectedTokens.append(tokens[playerInput - 1]);
                        print("{} has selected {}".format((player.name), player.token));
                        valid = True;
                        break
                except IndexError:
                    print("Please make a valid menu selection: ", end='')
                    continue
                except ValueError:
                    print("Please make a valid menu selection: ", end='')
                    continue

    def drawTile(self, row, tile):
        # draws the requested row number of the tile
        # draws any relevant tile data (players present, tile number, portals etc)
        # Params:
        #   row=the row of the tile to draw (int)
        #   tile=instance of a Tile object (Tile)
        " "
        tileCapRow = "---------";
        playersRow = self.generatePlayersRow(tile);
        tileNumberRow = self.generateTileNumberRow(tile);
        portalRow = self.generatePortalRow(tile);

        rows = [
            tileCapRow,
            playersRow,
            tileNumberRow,
            portalRow
        ]

        sys.stdout.write(rows[row]);

    def generatePlayersRow(self, tile):
        # creates a string to represent the players in a tile
        # has appropriate padding if there are no players present

        playerString = "     ";
        for player in tile.players:
            if player.isActive:
                playerString = colored(player.token, attrs=["reverse", "blink"]) + playerString;
            else:
                playerString = player.token + playerString;
            playerString = playerString[:len(playerString)-1] + playerString[len(playerString):];

        playersRow = "|  " + playerString + " ";
        return playersRow;

    def generatePortalRow(self, tile):
        portalString = "    "
        padding = " ";
        symbol = "";
        if tile.portal:
            #if the tile has a portal

            #because the two tiles share the same portal instance we need to find out
            #if the tile is the origin or the destination and draw the right number
            #and because tile index is zero based but tile number is not we need to +- 1
            if tile.portal.origin == tile.tileNumber - 1:
                #this means the tile is the origin so we want to draw out the destination of the portal
                destinationName = tile.portal.destination + 1;
            else:
                #vice versa, must draw the origin of the portal
                destinationName = tile.portal.origin + 1;

            if tile.portal.destination < tile.tileNumber:
                # change the symbol if its leading backwards
                if 0 <= tile.tileNumber <= 8 or 17 <= tile.tileNumber <= 24 or 33 <= tile.tileNumber <= 40:
                    symbol = colored("<-" + str(destinationName), "red", "on_grey", attrs=["bold", "reverse"]);
                else:
                    symbol = colored("->" + str(destinationName), "red", "on_grey", attrs=["bold", "reverse"]);

                if tile.portal.origin > 9:
                    padding = "";
            else:
                #symbol is forward and blue
                if 0 <= tile.tileNumber <= 8 or 17 <= tile.tileNumber <= 24 or 33 <= tile.tileNumber <= 40:
                    symbol = colored("->" + str(destinationName), "cyan", "on_grey", attrs=["bold", "reverse"]);
                else:
                    symbol = colored("<-" + str(destinationName), "cyan", "on_grey", attrs=["bold", "reverse"]);
                if tile.portal.destination > 9:
                    padding = "";

            portalString = symbol + padding;
        return "|  " + portalString + "  "

    def generateTileNumberRow(self, tile):
        # just returns a space if the number is smaller than 10
        # its padding for single digit numbers in the tile rendering
        padding = "";
        if tile.tileNumber< 10:
            padding = " ";

        #Adds arrows next to the tile number to indicate direction of play.
        if 0 < tile.tileNumber < 8 or 17 <= tile.tileNumber < 24 or 33 <= tile.tileNumber < 40:
            return "|   " + str(tile.tileNumber) + padding + "  >";
        elif 9 <= tile.tileNumber < 16 or 25 <= tile.tileNumber < 32:
            return "|<  " + str(tile.tileNumber) + padding + "   ";
        elif 16 == tile.tileNumber or tile.tileNumber == 32:
            return "|v  " + str(tile.tileNumber) + padding + "   ";
        elif tile.tileNumber == 40:
            return "|   " + str(tile.tileNumber) + padding + " :)";
        else:
            return "|   " + str(tile.tileNumber) + padding + "  v";

        #return "|   " + str(tile.tileNumber) + padding + "   ";

    def drawBoard(self, board, menuOptions=None, isAi=False):
        # draws the game board
        # Params:
        #   board=instance of the board to draw (Board)

        input("Press Enter to continue...")

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

        if isAi == True:
            menuOptions["options"][0]["method"]()
        else:
            if menuOptions != None:
                self.drawMenu(menuOptions)

    def drawMenu(self, menu):
        print(menu["heading"]);
        for index, option in enumerate(menu["options"]):
            print(index + 1, option["name"])
        print("\nPlease enter an option: ", end='')    
        while True:
            selection = input();
            try:
                option = menu["options"][int(selection) -1];
            except IndexError:
                # print(str(e));
                print("Please make a valid menu selection: ", end='')
                continue
            except ValueError:
                print("Please make a valid menu selection: ", end='')
                continue
            if int(selection) <= 0:
                print("Please make a valid menu selection: ", end='')
                continue
            else:
                break
        option["method"]();

    def drawEndGameScenario(self, playerlist, player, menuOptions):
        maxlength = max(max(len(p.name) for p in playerlist), 8)+2


        print("\n\nWinner winner chicken dinner! Congratulations " + player.name);
        print("\nGame Stats\n----------\n")

        print("Player:\t", end="\t")
        for p in playerlist:
            print("{0:>{1}}".format(p.name, maxlength), end='')

        print("\nTurns: \t", end="\t")
        for p in playerlist:
            print("{0:{1}}".format(p.turncount, maxlength), end='')

        print("\nPortals: \t", end="")
        for p in playerlist:
            print("{0:{1}}".format(p.portalsactivated, maxlength), end='')

        print("\nTiles: \t", end="\t")
        for p in playerlist:
            print("{0:{1}}".format(p.tilesmoved, maxlength), end='')

        print("\nRemaining: ", end="\t")
        for p in playerlist:
            print("{0:{1}}".format(39 - p.location, maxlength), end='')

        print("\n")


        # print("\n\nWinner winner chicken dinner! Congratulations " + player.name);
        # print("\nGame Stats\n----------\n")
        #
        # print("Player:\t", end="\t")
        # for p in self.controller.model.board.players:
        #     padding = ""
        #     nameLen = len(p.name)
        #     if (nameLen < 10):
        #         for j in range(0, 10 - nameLen):
        #             padding = padding + " "
        #     print(p.name + padding, end="\t")
        #
        # print("\nBot: \t", end="\t")
        # for p in self.controller.model.board.players:
        #     print(p.ai, end="\t\t")
        #
        # print("\nTurns: \t", end="\t")
        # for p in self.controller.model.board.players:
        #     print(p.turncount, end="\t\t\t")
        #
        # print("\nPortals: \t", end="")
        # for p in self.controller.model.board.players:
        #     print(p.portalsactivated, end="\t\t\t")
        #
        # print("\nTiles: \t", end="\t")
        # for p in self.controller.model.board.players:
        #     print(p.tilesmoved, end="\t\t\t")
        #
        # print("\nRemaining: ", end="\t")
        # for p in self.controller.model.board.players:
        #     print(39 - p.location, end="\t\t\t")
        #
        # print("\n")


        # test code to just run through the methods

        self.drawMenu(menuOptions);

    def quitGame(self):
        #this is just for the graphical manager to play nice
        pass