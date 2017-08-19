
class View:
    def gameMenu(self):
        return {
            "heading": "It is " + self.controller.activePlayer().name + "'s turn ("
                       + str(self.controller.activePlayer().token) + ")",
            "options": [
                {"name": "Roll Dice", "method": self.controller.takeTurn},
                {"name": "Quit to Menu", "method": self.controller.quitToMenu}
            ]
        }

    def endMenu(self):
        return {
            "heading": "Game Over!",
            "options": [
                {"name": "Replay Game", "method": self.controller.replayGame, "image": "images/redButtons/redButtonsReplay.png"},
                {"name": "Main Menu", "method": self.controller.newGame, "image": "images/redButtons/redButtonsMainMenu.png"},
                {"name": "Quit Game", "method": self.controller.quitGame, "image": "images/redButtons/redButtonsQuit.png"}
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

    # def drawMenu(self, menu):
    #     self.displayManager.drawMenu(menu);

    def drawMainScreen(self):
        self.displayManager.drawSplashScreen(self.mainMenu());

    def drawPlayerSetupScreen(self):
        self.displayManager.drawPlayerSetupScreen(self.controller.model.board.maxPlayers,
                                                  self.controller.getPlayersList(),
                                                  self.controller.model.board.playerTokens,
                                                  self.controller.model.selectedTokens)

    # def drawPlayerNamesScreen(self, playersNum):
    #     players = self.controller.getPlayersList();
    #     players[playersNum].name = input ('{} enter your name: '.format(players[playersNum].name));
    #     while len(players[playersNum].name) not in range(1, 21):
    #         players[playersNum].name = input('Must be between 1 and 20 characters:');
    #
    # def drawTokenSelectionScreen(self, playersNum):
    #     players = self.controller.getPlayersList();
    #     tokens = self.controller.model.board.playerTokens;
    #     selectedTokens = self.controller.model.selectedTokens;
    #
    #     if playersNum == (self.controller.model.board.maxPlayers - 1):
    #         for i in range(self.controller.model.board.maxPlayers - 1):
    #             if tokens[i] not in selectedTokens[:]:
    #                 players[playersNum].token = tokens[i];
    #                 print('{} has been assigned {}'.format((players[playersNum].name), players[playersNum].token));
    #     else:
    #         print("{} select your game token: ".format(players[playersNum].name), end = '');
    #         for i in range(len(tokens)):
    #             if tokens[i] not in selectedTokens[:]:
    #                 print( "{}>{}  " .format((i + 1), tokens[i]) , end = '');
    #             else:
    #                 print( "{}>{}  " .format((i + 1), '-') , end = '');
    #         print(":", end = "")
    #         while True:
    #             try:
    #                 playerInput = int(input(""));
    #                 while tokens[playerInput - 1] in selectedTokens[:]:
    #                     playerInput = int(input('Token {} is not available, try again:'.format(tokens[playerInput - 1])));
    #                 players[playersNum].token = tokens[playerInput - 1];
    #                 break
    #             except IndexError:
    #                 print("Please make a valid menu selection: ", end='')
    #                 continue
    #             except ValueError:
    #                 print("Please make a valid menu selection: ", end='')
    #                 continue
    #         print("{} has selected {}".format((players[playersNum].name), players[playersNum].token));
    #         selectedTokens.append(tokens[playerInput - 1]);
    #
    # def drawAIPlayersScreen(self):
    #     players = self.controller.getPlayersList()
    #     tokens = self.controller.model.board.playerTokens;
    #     selectedTokens = self.controller.model.selectedTokens;
    #     botNum = 1;
    #     aiNumber = self.controller.countHumanPlayers();
    #     try:
    #         for i in range(self.controller.model.board.maxPlayers):
    #             if tokens[i] not in selectedTokens[:]:
    #                 players[aiNumber].token = tokens[i];
    #                 selectedTokens.append(tokens[i]);
    #                 players[aiNumber].name = "Bot " + str(botNum);
    #                 print('Player {} is now known as {}'.format(aiNumber + 1, players[aiNumber].name))
    #                 print('{} has been allocated {} for their game token '.format(players[aiNumber].name, players[aiNumber].token))
    #             else:
    #                 continue;
    #             aiNumber += 1;
    #             botNum += 1;
    #     except IndexError:
    #         return

    def drawGameScreen(self):
        self.displayManager.drawBoard(self.controller.getGameBoard(),
                                      self.gameMenu(),
                                      self.controller.isActivePlayerAi(),);
        # if self.controller.isActivePlayerAi():
        #     self.controller.takeTurn();
        # else:
        #     self.drawMenu(self.gameMenu())

    def drawEndGameScreen(self):
        playerlist = self.controller.getPlayersList()
        player = self.controller.activePlayer()
        # self.displayManager.drawBoard(self.controller.getGameBoard());
        self.displayManager.drawEndGameScenario(playerlist, player, self.endMenu())
        # self.drawMenu(self.endMenu());

    def quitGame(self):
        self.displayManager.quitGame();

    def setScene(self, sceneName):
        # scenes are mainMenu, playerSetup, gameBoard, endGame
        # determines what method should be called by updateView

        if sceneName == "mainMenu":
            self.updateView = self.drawMainScreen;
        elif sceneName == "playerSetup":
            self.updateView = self.drawPlayerSetupScreen;
        elif sceneName == "gameBoard":
            self.updateView = self.drawGameScreen;
        # elif sceneName == "setNames":
        #     self.updateView = self.drawPlayerNamesScreen;
        # elif sceneName == "setTokens":
        #     self.updateView = self.drawTokenSelectionScreen;
        # elif sceneName == "createAIPlayers":
        #     self.updateView = self.drawAIPlayersScreen;
        elif sceneName == "endGame":
            self.updateView = self.drawEndGameScreen;
        elif sceneName == "quit":
            self.updateView = self.quitGame;
        else:
            print("Scene not found!")