import sys
from TerminalDisplayManager import TerminalDisplayManager
from Model import Model
from View import View

class Controller:
    def gameMenu(self):
        return {
            "heading": "It is " + self.model.getActivePlayer().name + "'s turn",
            "options": [
                {"name": "Roll Dice", "method": self.takeTurn},
                {"name": "Quit Game", "method": self.quitToMenu}
            ]
        }

    def mainMenu(self):
        return {
            "heading": "Welcome to Portals and Portals!",
            "options": [
                {"name": "Start Game", "method": self.startGame},
                {"name": "Setup Players", "method": self.setupPlayers},
                {"name": "Quit Game", "method": self.quitGame}
            ]
        }

    def __init__(self):
        textDisplayManager = TerminalDisplayManager();
        self.model = Model(self);
        self.view = View(textDisplayManager, self);
        self.gameInPlay = False;
        self.newGame();

    def newGame(self):
        self.model.resetBoard();
        self.view.drawMenu(self.mainMenu());

    def startGame(self):
        self.gameInPlay = True;
        while self.gameInPlay:
            #draw the board
            self.view.displayManager.drawBoard(self.model.board);
            #draw the menu (get input)
            self.view.drawMenu(self.gameMenu());

    def setupPlayers(self):
        print("setting up players");
        self.view.drawMenu(self.mainMenu());

    def quitToMenu(self):
        print("quitting to main menu");
        self.gameInPlay = False;
        self.newGame();

    def quitGame(self):
        print("quitting game");
        #break the main game loop
        self.gameInPlay = False;

    def takeTurn(self):
        print("taking turn");


def main(argv):
    # print("Main ran")
    controller = Controller();

if __name__ == "__main__":
    main(sys.argv)