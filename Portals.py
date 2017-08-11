import sys
from Controller import Controller

def main(argv):
    print(argv)
    if len(argv) > 1 and argv[1] == "-g":
        controller = Controller(graphical=True);
    else:
        controller = Controller(graphical=False);

if __name__ == "__main__":
    main(sys.argv)