import argparse


def getcolor(arg):
    if arg == "int":
        return "red"
    elif arg == "list":
        return "blue"
    elif arg == "any":
        return "green"
    else:
        # Default
        return "white"


def printargs(args):
    for arg in vars(args):
        val = getattr(args, arg)
        if (val != None):
            color = getcolor(arg)
            print("Argument: '{}', Value: '{}', Color: {}".format(arg,
val, color))


parser = argparse.ArgumentParser(description="A simple program to parse arguments")
parser.add_argument('-a', '--any', help="Any input type")
parser.add_argument('-l', '--list', help="Values for a list",
type=list)
parser.add_argument('-i', '--int', help="Integers", type=int)
args = parser.parse_args()

printargs(args)
