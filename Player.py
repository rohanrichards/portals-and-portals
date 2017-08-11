#Player definitions

class Player:

    def __init__(self, name, token, ai):
        self.name = name;
        self.token = token;
        self.ai = ai; #whether or not it is AI
        self.isActive = False; #is it the currently active player
        self.location = 0; # their current tile
        self.turncount = 0; # how many turns they've had
        self.portalsactivated = 0; # how many portals they've activated
        self.tilesmoved = 0; # how many tiles they've moved
