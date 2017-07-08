#Player definitions

class Player:

    def __init__(self, name, token, ai):
        print("new player instance")
        self.name = name;
        self.token = token;
        self.ai = ai;
        self.isActive = False;