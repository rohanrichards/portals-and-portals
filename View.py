
class View:

    def __init__(self, displayManager, controller):
        self.controller = controller;
        self.displayManager = displayManager;
        # self.controller.testPresence();

    def drawMenu(self, menu):
        self.displayManager.drawMenu(menu);