from tkinter import *

class Splash:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        bottomFrame = Frame(master)
        bottomFrame.pack(side=BOTTOM)

        self.splash = PhotoImage(file="PortalsSplash.PNG")
        self.lblPhoto = Label(frame, image=self.splash)
        self.lblPhoto.pack()

        self.btnStart = Button(bottomFrame, text="New Game", fg="red", command=self.startGame)
        self.btnStart.pack(side=LEFT)

        self.btnPlayers = Button(bottomFrame, text="Set Up Players", fg="red", command=self.playerSetup)
        self.btnPlayers.pack(side=LEFT)

        self.btnQuit = Button(bottomFrame, text="Exit", fg="black", command=frame.quit)
        self.btnQuit.pack(side=LEFT)

    def startGame(self):
        print("Starting Game!")

    def playerSetup(self):
        print("Setting Up Players!")

root = Tk()
b = Splash(root)
root.mainloop()