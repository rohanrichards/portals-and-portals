class Tile():
    players = [];
    tileNumber = 0;
    portal = -1;

    # constructor
    def __init__(self, number):
        # print("Created a new Tile instance");
        self.tileNumber = number;