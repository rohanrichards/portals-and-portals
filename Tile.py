class Portal:
    # very simply class to define a portal as an object
    def __init__(self, origin, dest):
        self.origin = origin;
        self.destination = dest;

class Tile():
    # Things declared here are considered *class* variables
    # CLASS VARIABLES ARE SHARED BY ALL INSTANCES
    # SERIOUSLY PYTHON!?!?!? SERIOUSLY!?!??!
    # players = [];
    # tileNumber = 0;
    # portal = -1;

    # constructor
    def __init__(self, number):
        # things defined here are
        # *INSTANCE* variables!!!!!
        self.players = [];
        self.tileNumber = number;
        self.portal = None;