import sys
from TerminalDisplayManager import TerminalDisplayManager
from Model import Model
from View import View

class Controller:
    def gameMenu(self): return {
        "heading": "It is " + self.model.getActivePlayer().name + "'s turn ("
                   + self.model.getActivePlayer().token + ")",
        "options": [
            {"name": "Roll Dice", "method": self.takeTurn},
            {"name": "Quit Game", "method": self.quitToMenu}
        ]
    }

    def endMenu(self): return {
        "heading": "Game Over!",
                    # to-do: game summary data
                    # who won
                    # total portals used
                    # total turns taken
                    
        "options": [
            {"name": "Replay Game", "method": self.replayGame},
            {"name": "Main Menu", "method": self.newGame},
            {"name": "Quit Game", "method": self.quitGame}
        ]
    }

    def mainMenu(self): return {
        "heading": ("Welcome to Portals and Portals!\n"
                    "Players: " + str(self.model.countHumanPlayers())),
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
        self.gameInPlay = True;
        while self.gameInPlay:
            #draw the board
            self.view.displayManager.drawBoard(self.model.board);
            if self.model.board.getActivePlayer().ai:
                self.takeTurn();
            else:
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
        spaces = self.model.rollDice();
        print("Taking your turn - you rolled a " + str(spaces));
        
        player = self.model.getActivePlayer();
        self.model.movePlayerBySpaces(player, spaces);
        
        #end game check here
        if player.location == 39: 
            print("Winner winner chicken dinner! Congratulations " + player.name);
            self.view.displayManager.drawBoard(self.model.board);
            self.view.drawMenu(self.endMenu());
            
        self.model.setNextActivePlayer();
        self.model.randomizePortalsTest();

def main(argv):
    controller = Controller();

if __name__ == "__main__":
    main(sys.argv)