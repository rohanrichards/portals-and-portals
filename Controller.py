import sys
from TerminalDisplayManager import TerminalDisplayManager
from Model import Model
from View import View
# Temp comment
class Controller:
    def __init__(self):
        textDisplayManager = TerminalDisplayManager();
        self.model = Model(self);
        self.view = View(textDisplayManager, self);
        self.gameInPlay = False;

        self.newGame();

    def newGame(self):
        self.model.resetBoard();
        self.view.setScene("mainMenu");
        self.view.updateView();
        # self.view.drawMenu(self.mainMenu());

    def replayGame(self):
        #resets the position of all players to the first tile
        #resets the active player to the first player in the players array
        #starts a game again without going to the main menu
        self.model.resetTokens();
        self.model.resetActivePlayer();
        self.startGame();

    def startGame(self):
        #main game loop
        #can be broken by setting self.gameInPlay to false
        self.model.resetBoard()
        self.gameInPlay = True;
        self.view.setScene("gameBoard");
        while self.gameInPlay:
            self.view.updateView();

    def setupPlayers(self):
        print("setting up players");
        self.view.setScene("playerSetup");
        self.view.updateView();

    def quitToMenu(self):
        print("quitting to main menu");
        self.gameInPlay = False;
        self.newGame();

    def quitGame(self):
        print("quitting game");
        #break the main game loop
        self.gameInPlay = False;

    def takeTurn(self):
        spaces = self.model.rollDice();
        print("Taking your turn - you rolled a " + str(spaces));
        
        player = self.model.getActivePlayer();

        self.model.movePlayerBySpaces(player, spaces);
        
        #end game check here
        if player.location == 39:
            self.view.setScene("endGame")
            self.view.updateView();
            # self.view.displayManager.drawBoard(self.model.board);
            # self.view.drawMenu(self.endMenu());

        player = self.activePlayer()
        player.turncount = player.turncount + 1;
        self.model.setNextActivePlayer();
        self.model.randomizePortalsTest();

    def activePlayer(self):
        return self.model.getActivePlayer();

    def countHumanPlayers(self):
        return self.model.countHumanPlayers();

    def getGameBoard(self):
        return self.model.board;

    def isActivePlayerAi(self):
        return self.model.board.getActivePlayer().ai;

    def getPlayersList(self):
        playersList = self.model.board.players
        return playersList

    def endGame(self, player):
        print("\n\nWinner winner chicken dinner! Congratulations " + player.name);
        print("\nGame Stats\n----------\n")

        print("Player:\t", end="\t")
        for p in self.model.board.players:
            print(p.name, end="\t")

        print("\nBot: \t", end="\t")
        for p in self.model.board.players:
            print(p.ai, end="\t\t")

        print("\nTurns: \t", end="\t")
        for p in self.model.board.players:
            print(p.turncount, end="\t\t\t")

        print("\nPortals: \t", end="")
        for p in self.model.board.players:
            print(p.portalsactivated, end="\t\t\t")

        print("\nTiles: \t", end="\t")
        for p in self.model.board.players:
            print(p.tilesmoved, end="\t\t\t")

        print("\nRemaining: ", end="\t")
        for p in self.model.board.players:
            print(39 - p.location, end="\t\t\t")

        print("\n")

def main(argv):
    controller = Controller();

if __name__ == "__main__":
    main(sys.argv)