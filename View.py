
class View:

    def __init__(self, displayManager, controller):
        self.controller = controller;
        self.displayManager = displayManager;
        self.controller.testPresence();