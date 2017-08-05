
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
        while True:
            userInput = input('How many players (0 - {})?'.format(self.controller.model.board.maxPlayers));
            try:
                int(userInput)
            except ValueError:
                print("Please make a valid menu selection: ", end='')
                continue
            if int(userInput) not in range(0, self.controller.model.board.maxPlayers + 1):
                print("Please make a valid menu selection: ", end='')
                continue
            else:
                break

        for i in range(len(self.controller.getPlayersList())):
            if i < int(userInput):
                self.controller.model.board.players[i].ai = False;
            else:
                self.controller.model.board.players[i].ai = True;

        # print("this should draw the UI for setting up players");

    def drawPlayerNamesScreen(self):
        # print('setting up names')
        players = self.controller.getPlayersList()
        for i in range(0, self.controller.model.countHumanPlayers()):
            players[i].name = input ('Player {} enter your name: '.format(players[i].name))
            while len(players[i].name) not in range(1,11):
                players[i].name = input('Must be between 1 and 10 characters. Player {} enter your name: '.format(players[i].name))


    def drawGameScreen(self):
        self.displayManager.drawBoard(self.controller.getGameBoard());
        if self.controller.isActivePlayerAi():
            print("It is " + self.controller.activePlayer().name + "'s turn ("
            + self.controller.activePlayer().token + ")")
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
            padding = ""
            nameLen = len(p.name)
            if(nameLen < 10):
                for j in range(0, 10-nameLen):
                    padding = padding + " "
            print(p.name + padding, end="\t")

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
        elif sceneName == "setNames":
            self.updateView = self.drawPlayerNamesScreen;
        elif sceneName == "endGame":
            self.updateView = self.drawEndGameScreen;
        else:
            print("Scene not found!")