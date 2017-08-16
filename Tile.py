class Portal:
    # very simple class to define a portal as an object
    files = [
        "images/portals/portalBurgundy.png",
        "images/portals/portalCyan.png",
        "images/portals/portalGreen.png",
        "images/portals/portalRed.png",
        "images/portals/portalYellow.png",
    ]
    def __init__(self, origin, dest, image=None):
        self.origin = origin;
        self.destination = dest;
        self.image = image

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