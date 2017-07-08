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