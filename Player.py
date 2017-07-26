#Player definitions

class Player:

    def __init__(self, name, token, ai):
        self.name = name;
        self.token = token;
        self.ai = ai;
        self.isActive = False;
        self.location = 0;
        self.numGamesPlayed = 0;