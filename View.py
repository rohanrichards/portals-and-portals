
class View:
    def gameMenu(self):
        return {
            "heading": "It is " + self.controller.activePlayer().name + "'s turn ("
                       + self.controller.activePlayer().token + ")",
            "options": [
                {"name": "Roll Dice", "method": self.controller.takeTurn},
                {"name": "Quit Game", "method": self.controller.quitToMenu}
            ]
        }

    def endMenu(self):
        return {
            "heading": "Game Over!",
            # to-do: game summary data
            # who won
            # total portals used
            # total turns taken

            "options": [
                {"name": "Replay Game", "method": self.controller.replayGame},
                {"name": "Main Menu", "method": self.controller.newGame},
                {"name": "Quit Game", "method": self.controller.quitGame}
            ]
        }

    def mainMenu(self):
        return {
            "heading": ("Welcome to Portals and Portals!\n"
                        "Players: " + str(self.controller.countHumanPlayers())),
            "options": [
                {"name": "Start Game", "method": self.controller.startGame},
                {"name": "Setup Players", "method": self.controller.setupPlayers},
                {"name": "Quit Game", "method": self.controller.quitGame}
            ]
        }

    def __init__(self, displayManager, controller):
        self.controller = controller;
        self.displayManager = displayManager;
        self.updateView = self.drawMainScreen;
        # self.controller.testPresence();

    def drawMenu(self, menu):
        self.displayManager.drawMenu(menu);

    def drawMainScreen(self):
        self.displayManager.drawMenu(self.mainMenu());

    def drawPlayerSetupScreen(self):
        print("this should draw the UI for setting up players");

    def drawGameScreen(self):
        self.displayManager.drawBoard(self.controller.getGameBoard());
        if self.controller.isActivePlayerAi():
            self.controller.takeTurn();
        else:
            self.drawMenu(self.gameMenu())

    def drawEndGameScreen(self):
        self.displayManager.drawBoard(self.controller.getGameBoard());
        player = self.controller.activePlayer()
        print("\n\nWinner winner chicken dinner! Congratulations " + player.name);
        print("\nGame Stats\n----------\n")

        print("Player:\t", end="\t")
        for p in self.controller.model.board.players:
            print(p.name, end="\t")

        print("\nBot: \t", end="\t")
        for p in self.controller.model.board.players:
            print(p.ai, end="\t\t")

        print("\nTurns: \t", end="\t")
        for p in self.controller.model.board.players:
            print(p.turncount, end="\t\t\t")

        print("\nPortals: \t", end="")
        for p in self.controller.model.board.players:
            print(p.portalsactivated, end="\t\t\t")

        print("\nTiles: \t", end="\t")
        for p in self.controller.model.board.players:
            print(p.tilesmoved, end="\t\t\t")

        print("\nRemaining: ", end="\t")
        for p in self.controller.model.board.players:
            print(39 - p.location, end="\t\t\t")

        print("\n")

        self.drawMenu(self.endMenu());

    def setScene(self, sceneName):
        # scenes are mainMenu, playerSetup, gameBoard, endGame
        # determines what method should be called by updateView

        if sceneName == "mainMenu":
            self.updateView = self.drawMainScreen;
        elif sceneName == "playerSetup":
            self.updateView = self.drawPlayerSetupScreen;
        elif sceneName == "gameBoard":
            self.updateView = self.drawGameScreen;
        elif sceneName == "endGame":
            self.updateView = self.drawEndGameScreen;
        else:
            print("Scene not found!")