
class View:
    def gameMenu(self):
        return {
            "heading": "It is " + self.controller.activePlayer().name + "'s turn ("
                       + self.controller.activePlayer().token + ")",
            "options": [
                {"name": "Roll Dice", "method": self.controller.takeTurn},
                {"name": "Quit to Menu", "method": self.controller.quitToMenu}
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
        userInput = int(input('How many players (max {})?'.format(self.controller.model.board.maxPlayers)));
        while userInput not in range(1, self.controller.model.board.maxPlayers + 1):
            userInput = int(input('Try again. How many players (max {})?'.format(self.controller.model.board.maxPlayers)));
        for i in range(len(self.controller.getPlayersList())):
            if i < userInput:
                self.controller.model.board.players[i].ai = False;
            else:
                self.controller.model.board.players[i].ai = True;

        # print("this should draw the UI for setting up players");

    def drawPlayerNamesScreen(self):
        # print('setting up names')
        players = self.controller.getPlayersList()
        for i in range(0, self.controller.model.countHumanPlayers()):
            players[i].name = input ('Player {} enter your name: '.format(players[i].name))
            while len(players[i].name) not in range(1,21):
                players[i].name = input('Must be between 1 and 20 characters. Player {} enter your name: '.format(players[i].name))


    def drawGameScreen(self):
        self.displayManager.drawBoard(self.controller.getGameBoard());
        if self.controller.isActivePlayerAi():
            self.controller.takeTurn();
        else:
            self.drawMenu(self.gameMenu())

    def drawEndGameScreen(self):
        playerlist = self.controller.getPlayersList()
        player = self.controller.activePlayer()
        self.displayManager.drawBoard(self.controller.getGameBoard());
        self.displayManager.drawEndGameScenario(playerlist, player)
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