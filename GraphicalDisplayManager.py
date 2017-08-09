from tkinter import *
from tkinter import ttk

class GraphicalDisplayManager:

    def __init__(self):
        pass

    def drawSplashScreen(self, menuOptions):
        print("draw the splash screen")
#         to-do Shawn


    def drawPlayerSetupScreen(self, maxPlayers, playersList, tokens, selectedTokens):
        self.setNumberOfPlayers(maxPlayers, playersList)
        self.setNameAndTokens(playersList, tokens, selectedTokens)

    def setNumberOfPlayers(self, maxPlayers, playersList):
        def setNumPlayers(number):
            for index, player in enumerate(playersList):
                if index < number:
                    print("set player to non-ai")
                    player.ai = False
                else:
                    print("set player to ai")
                    player.ai = True
            root.destroy()

        root = Tk()
        root.title("Setup Game")

        mainFrame = ttk.Frame(root, padding="10 10 10 10")
        mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
        mainFrame.columnconfigure(0, weight=1)
        mainFrame.rowconfigure(0, weight=1)

        ttk.Label(mainFrame, text="How many players?").grid(column=0, row=0, sticky=(W, E))
        buttonFrame = ttk.Frame(mainFrame, padding="10 10 10 10")
        buttonFrame.grid(column=0, row=3)

        # draw the tokens
        for i in range(1, maxPlayers+1):
                b = ttk.Button(buttonFrame, text=i,
                               command=lambda number=i: setNumPlayers(number))
                b.grid(column=i, row=0)

        root.mainloop()

    def setNameAndTokens(self, playersList, tokens, selectedTokens):
        def setToken(player, name, token):
            print("selected token" + token)
            print(player.name)
            player.name = name
            player.token = token
            selectedTokens.append(token)
            print("added to selected tokens")
            print(selectedTokens)
            root.destroy()

        for player in playersList:
            if player.ai == False:
                root = Tk()
                root.title("Setup " + player.name)

                mainFrame = ttk.Frame(root, padding="10 10 10 10")
                mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
                mainFrame.columnconfigure(0, weight=1)
                mainFrame.rowconfigure(0, weight=1)

                nameEntry = ttk.Entry(mainFrame, width=7)
                nameEntry.grid(column=0, row=1, sticky=(W, E))
                ttk.Label(mainFrame, text="Enter your name").grid(column=0, row=0, sticky=(W, E))

                ttk.Label(mainFrame, text="Select your token").grid(column=0, row=2, sticky=(W, E))
                tokenFrame = ttk.Frame(mainFrame, padding="10 10 10 10")
                tokenFrame.grid(column=0, row=3)

                #draw the tokens
                for index, token in enumerate(tokens):
                    if token not in selectedTokens:
                        print("token found: " + token)
                        b = ttk.Button(tokenFrame, text=token, command=lambda token=token: setToken(player, nameEntry.get(), token))
                        b.grid(column=index, row=0)

                root.mainloop()
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

    def drawBoard(self, menuOptions=None, isAi=False):
        pass

    def drawEndGameScenario(self, playerList, player, menuOptions):
        pass



# class Splash:
#
#     def __init__(self, master):
#
#         frame = Frame(master)
#         frame.pack()
#
#         bottomFrame = Frame(master)
#         bottomFrame.pack(side=BOTTOM)
#
#         self.splash = PhotoImage(file="PortalsSplash.PNG")
#         self.lblPhoto = Label(frame, image=self.splash)
#         self.lblPhoto.pack()
#
#         self.btnStart = Button(bottomFrame, text="New Game", fg="red", command=self.startGame)
#         self.btnStart.pack(side=LEFT)
#
#         self.btnPlayers = Button(bottomFrame, text="Set Up Players", fg="red", command=self.playerSetup)
#         self.btnPlayers.pack(side=LEFT)
#
#         self.btnQuit = Button(bottomFrame, text="Exit", fg="black", command=frame.quit)
#         self.btnQuit.pack(side=LEFT)
#
#     def startGame(self):
#         print("Starting Game!")
#
#     def playerSetup(self):
#         print("Setting Up Players!")
#
# root = Tk()
# b = Splash(root)
# root.mainloop()
