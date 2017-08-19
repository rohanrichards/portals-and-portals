import sys
from Controller import Controller
from tkinter import *
from pathlib import Path

def main(argv):
    if len(argv) > 1 and argv[1] == "-g":
        try:
            preload = [
                "./images/playerTokens/playerTokens_blueDisc.png",
                "./images/playerTokens/playerTokens_boomerangePrawn.png",
                "./images/playerTokens/playerTokens_casinoChip.png",
                "./images/playerTokens/playerTokens_orangeDisc.png",
                "./images/playerTokens/playerTokens_purpleDisc.png",
                "./images/playerTokens/playerTokens_sherriffStar.png",
                "./images/playerTokens/playerTokens_yellowDisc.png",
                "./images/redButtons/redButtonsStartGame.png",
                "./images/redButtons/redButtonsQuit.png",
                "PortalsSplash.PNG",
                "./images/dice/diceClickToRoll.png",
                "./images/tiles/tilesStartTile.png",
                "./images/tiles/tilesEndTile.png",
                "./images/tiles/tilesBeigeTile.png",
                "./images/tiles/tilesBrownTile.png",
                "./images/arrows/arrowDown.png",
                "./images/arrows/arrowLeft.png",
                "./images/arrows/arrowRight.png",
                "./images/portals/portalBurgundy.png",
                "./images/portals/portalCyan.png",
                "./images/portals/portalGreen.png",
                "./images/portals/portalRed.png",
                "./images/portals/portalYellow.png"
            ]

            for imagePath in preload:
                my_file = Path(imagePath)
                if my_file.is_file():
                    pass
                else:
                    raise Exception(imagePath)


        except Exception as error:
            print("Images not found : " + str(error))
            print("Launching text based game!")
            print()
            controller = Controller(graphical=False)


        controller = Controller(graphical=True);
    else:
        controller = Controller(graphical=False);

if __name__ == "__main__":
    main(sys.argv)