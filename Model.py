from Board import Board

class Model:

    def __init__(self, controller):
        self.board = Board();
        self.controller = controller;
        # print("board init")

    def getActivePlayer(self):
        #returns the currently active player
        for player in self.board.players:
            if player.isActive:
                return player;

    def resetBoard(self):
        self.board = None;
        self.board = Board();