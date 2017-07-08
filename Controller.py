import sys
from TerminalDisplayManager import TerminalDisplayManager
from Model import Model
from View import View

class Controller:

    def __init__(self):
        textDisplayManager = TerminalDisplayManager();
        self.model = Model(self);
        self.view = View(textDisplayManager, self);
        self.view.displayManager.drawBoard(self.model.board);

    def testPresence(self):
        print("I'm here.");

def main(argv):
    # print("Main ran")
    controller = Controller();

if __name__ == "__main__":
    main(sys.argv)