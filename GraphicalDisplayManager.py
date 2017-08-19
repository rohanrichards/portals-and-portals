from tkinter import *
from tkinter import ttk
from Dialog import *
import tkinter as tk
import math
import time

class GraphicalDisplayManager:

    def __init__(self):
        self.debug = False
        self.root = Tk()
        self.mainFrame = None
        self.boardTileHeight = 95
        self.boardTileWidth = 95
        self.renderLoopRunning = False
        self.scene = "main"

        self.tokenImages = [
            "./images/playerTokens/playerTokens_blueDisc.png",
            "./images/playerTokens/playerTokens_boomerangePrawn.png",
            "./images/playerTokens/playerTokens_casinoChip.png",
            "./images/playerTokens/playerTokens_orangeDisc.png",
            "./images/playerTokens/playerTokens_purpleDisc.png",
            "./images/playerTokens/playerTokens_sherriffStar.png",
            "./images/playerTokens/playerTokens_yellowDisc.png",
        ]

    def drawSplashScreen(self, menuOptions):
        self.setupPlayers = menuOptions["options"][1]["method"];
        self.startGame = menuOptions["options"][0]["method"];

        if self.mainFrame:
            self.mainFrame.destroy()

        self.root.title("Portals and Portals")

        self.mainFrame = Frame(self.root)
        self.mainFrame.pack()

        image = PhotoImage(file="PortalsSplash.PNG")
        lblPhoto = Label(self.mainFrame, image=image)
        lblPhoto.pack()

        imgStart = PhotoImage(file="./images/redButtons/redButtonsStartGame.png")
        imgQuit = PhotoImage(file="./images/redButtons/redButtonsQuit.png")

        bottomFrame = Frame(self.mainFrame)
        bottomFrame.pack(side=BOTTOM)

        btnStart = Button(bottomFrame, text="New Game", fg="red", command=self.setupPlayers)
        btnStart.config(image=imgStart)
        btnStart.pack(side=LEFT)

        btnQuit = Button(bottomFrame, text="Exit", fg="black", command=self.root.destroy)
        btnQuit.config(image=imgQuit)
        btnQuit.pack(side=LEFT)

        self.root.mainloop()

        # while True:
        #     self.root.update()
        #     self.root.update_idletasks()

        # menuOptions["options"][1]["method"]()

    def drawPlayerSetupScreen(self, maxPlayers, playersList, tokens, selectedTokens):
        if self.debug == False:
            self.setNumberOfPlayers(maxPlayers, playersList)
            self.setNameAndTokens(playersList, tokens, selectedTokens)
            self.startGame()
        else:
            for index, player in enumerate(playersList):
                print(index)

                player.token = int(index)
                player.ai = False
            self.startGame()

    def setNumberOfPlayers(self, maxPlayers, playersList):
        d = SetPlayersDialog(self.root, "How many players?")

        for index, player in enumerate(playersList):
            if index < d.result:
                print("set player to non-ai")
                player.ai = False
            else:
                print("set player to ai")
                player.ai = True
        #
        # mainFrame = ttk.Frame(root, padding="10 10 10 10")
        # mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        # mainFrame.columnconfigure(0, weight=1)
        # mainFrame.rowconfigure(0, weight=1)
        #
        # ttk.Label(mainFrame, text="How many players?").grid(column=0, row=0, sticky=(W, E))
        # buttonFrame = ttk.Frame(mainFrame, padding="10 10 10 10")
        # buttonFrame.grid(column=0, row=3)
        #
        # # draw the tokens
        # for i in range(1, maxPlayers+1):
        #         b = ttk.Button(buttonFrame, text=i,
        #                        command=lambda number=i: setNumPlayers(number))
        #         b.grid(column=i, row=0)

        # root.mainloop()

    def setNameAndTokens(self, playersList, tokens, selectedTokens):

        for index, player in enumerate(playersList):
            if player.ai == False:

                d = SelectTokensDialog(self.root, "Setup Players",
                               data={"tokens": tokens, "selectedTokens": selectedTokens, "images": self.tokenImages })
                print(d.result)
                player.name = d.result[0]
                player.token = d.result[1]
                selectedTokens.append(d.result[2])
                print("added to selected tokens")
                print(selectedTokens)

            else:
                player.name = "Bot " + str(index)
                print('Player {} is now known as {}'.format(index + 1, player.name))
                for index, token in enumerate(tokens):
                    if token not in selectedTokens:
                        player.token = index;
                        selectedTokens.append(token);
                        print('{} has been allocated {} for their game token '.format(player.name,
                                                                                      player.token))
                        break

        # for player in playersList:
        #     if player.ai == False:
        #         root = Tk()
        #         root.title("Setup " + player.name)
        #
        #         mainFrame = ttk.Frame(root, padding="10 10 10 10")
        #         mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        #         mainFrame.columnconfigure(0, weight=1)
        #         mainFrame.rowconfigure(0, weight=1)
        #
        #         nameEntry = ttk.Entry(mainFrame, width=7)
        #         nameEntry.grid(column=0, row=1, sticky=(W, E))
        #         ttk.Label(mainFrame, text="Enter your name").grid(column=0, row=0, sticky=(W, E))
        #
        #         ttk.Label(mainFrame, text="Select your token").grid(column=0, row=2, sticky=(W, E))
        #         tokenFrame = ttk.Frame(mainFrame, padding="10 10 10 10")
        #         tokenFrame.grid(column=0, row=3)
        #
        #         #draw the tokens
        #         for index, token in enumerate(tokens):
        #             if token not in selectedTokens:
        #                 print("token found: " + token)
        #                 b = ttk.Button(tokenFrame, text=token, command=lambda token=token: setToken(player, nameEntry.get(), token))
        #                 b.grid(column=index, row=0)
        #
        #         root.mainloop()
        #     else:
        #         player.name = "Bot " + str(index)
        #         print('Player {} is now known as {}'.format(index + 1, player.name))
        #         for token in tokens:
        #             if token not in selectedTokens:
        #                 player.token = token;
        #                 selectedTokens.append(token);
        #                 print('{} has been allocated {} for their game token '.format(player.name,
        #                                                                               player.token))
        #                 break

    def drawBoard(self, board, menuOptions=None, isAi=False):
        self.board = board
        if menuOptions:
            self.takeTurn = menuOptions["options"][0]["method"];

        if self.scene != "game":
            self.mainFrame.destroy()
            self.root.title("Portals and Portals")

            self.mainFrame = Frame(self.root)
            self.mainFrame.pack()

            self.boardFrame = Frame(self.mainFrame, height=board.height * self.boardTileHeight,
                                    width=board.width * self.boardTileWidth)
            self.boardFrame.pack()

            self.buttonFrame = Frame(self.mainFrame)
            self.buttonFrame.pack()

            btnStart = Button(self.buttonFrame, text="New Game", fg="red", command=self.takeTurn)
            btnStart.image = PhotoImage(file="images/dice/diceClickToRoll.png")
            btnStart.config(image=btnStart.image)
            btnStart.pack(side=RIGHT)

            try:
                del self.tileFrames
            except Exception:
                pass

            self.buttonFrame.nameLabels = []
            for index, player in enumerate(board.players):
                image = PhotoImage(file=self.tokenImages[player.token])
                nameLabel = Label(self.buttonFrame, text=player.name, padx=20, image=image, compound=CENTER)
                nameLabel.image = image
                nameLabel.pack(side=LEFT)
                self.buttonFrame.nameLabels.append(nameLabel)
                if player.isActive == True:
                    nameLabel.config(background="green")
            self.scene = "game"

        if isAi:
            self.drawTiles(board)
            self.takeTurn()

        # self.root.mainloop()
        if self.renderLoopRunning == False:
            while True:
                #redraw tiles
                self.renderLoopRunning = True
                self.drawTiles(board)
                for index, player in enumerate(board.players):
                    if player.isActive == True:
                        # print("setting label " + str(index) + " green")
                        self.buttonFrame.nameLabels[index].config(background="green")
                    else:
                        # print("setting label " + str(index) + " white")
                        self.buttonFrame.nameLabels[index].config(background="white")
                self.root.update()
                self.root.update_idletasks()
                time.sleep(0.01)

    def drawTiles(self, board):
        try:
            self.tileFrames
        except AttributeError:
            self.tileFrames = []
            self.setupTiles(board)

        for tile in board.tiles:
            canvas = self.tileFrames[tile.tileNumber - 1].canvas
            self.drawPortalsOnTile(tile, canvas)
            self.drawPlayerTokensOnTile(tile, canvas)

    def setupTiles(self, board):
        for row in range(0, board.height):
            for col in range(0, board.width):
                tiles = board.tiles
                tile = tiles[(row * board.width) + (col)]
                if tile.tileNumber == 1:
                    tileFile = "images/tiles/tilesStartTile.png"
                elif tile.tileNumber == board.width * board.height:
                    tileFile = "images/tiles/tilesEndTile.png"
                elif tile.tileNumber % 2 == 0:
                    tileFile = "images/tiles/tilesBeigeTile.png"
                else:
                    tileFile = "images/tiles/tilesBrownTile.png"

                tileFrame = Frame(self.boardFrame,
                                  height=self.boardTileHeight, width=self.boardTileWidth,
                                  background="green", borderwidth=0, highlightthickness=0)
                canvas = tk.Canvas(tileFrame, width=self.boardTileWidth, height=self.boardTileHeight,
                                   background="blue", borderwidth=0, highlightthickness=0)
                self.tileFrames.append(tileFrame)
                tileFrame.canvas = canvas
                canvas.pack()
                canvas.image = PhotoImage(file=tileFile)
                canvas.create_image(0, 0, image=canvas.image, anchor='nw')

                if row % 2:
                    index = (board.width) - (col + 1);
                    x = index * self.boardTileWidth
                else:
                    x = col * self.boardTileWidth
                y = row * self.boardTileHeight
                tileFrame.place(x=x, y=y)

                self.drawDirectionArrows(tile, canvas)
                tokenText = canvas.create_text(10, 10, anchor="nw")
                canvas.itemconfig(tokenText, text=tile.tileNumber)

    def drawDirectionArrows(self, tile, canvas):
        if tile.tileNumber > 1 and tile.tileNumber < 40:
            if tile.tileNumber % 8 == 0:
                arrowPath = "images/arrows/arrowDown.png"
            elif math.ceil(tile.tileNumber / 8) % 2 == 0:
                arrowPath = "images/arrows/arrowLeft.png"
            else:
                arrowPath = "images/arrows/arrowRight.png"
            canvas.arrow = PhotoImage(file=arrowPath)
            canvas.create_image(90, 90, image=canvas.arrow, anchor="se")

    def drawPlayerTokensOnTile(self, tile, canvas):
        try:
            for token in canvas.token:
                canvas.delete(token)
            canvas.token = []
        except AttributeError:
            canvas.token = []

        players = tile.players
        for count, player in enumerate(players):
            tokenFile = self.tokenImages[player.token]
            tokenImage = PhotoImage(file=tokenFile).subsample(2, 2)
            player.tokenImage = tokenImage
            x = count * tokenImage.width()
            y = 20
            if count > 1:
                y += tokenImage.height()
                x = (count - 2)* tokenImage.width()
            image = canvas.create_image(20+x, y, image=tokenImage, anchor="nw")
            canvas.token.append(image)

    def drawPortalsOnTile(self, tile, canvas):
        try:
            canvas.delete(canvas.portal)
            canvas.portal = None
        except AttributeError:
            pass
        if tile.portal:
            portalImage = PhotoImage(file=tile.portal.image)
            tile.portalImage = portalImage
            canvas.portal = canvas.create_image(0, 0, image=portalImage, anchor="nw")
            # canvas.portal.image = portalImage


    def drawEndGameScenario(self, playerList, player, menuOptions):
        self.drawTiles(self.board)
        self.scene = "end"
        self.renderLoopRunning = False
        d = EndGameScreen(self.root, "Winner Winner Chicken Dinner!", {
            "player": player,
            "menuOptions": menuOptions,
            "players": playerList
        })

    def quitGame(self):
        self.mainFrame.destroy()
        self.root.quit()
        self.root.destroy()