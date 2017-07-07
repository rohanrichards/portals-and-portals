#Player definitions

class Player:
    name = "";
    token = "";
    ai = True;

    def __init__(self, name, token, ai):
        print("new player instance")
        self.name = name;
        self.token = token;
        self.ai = ai;