from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


correct_argv = ["-f", "--font"]

fonts = figlet.getFonts() #crea una lista in automatico, se assegni doppia lista errore


if len(sys.argv) > 2:

    # check if the middle term is in the list correct arg
    for arg in sys.argv[1:-1]:
        if arg in correct_argv:
            continue
        else:
            sys.exit("Invalid usage")

        # check if the last term is the list font
    for arg in sys.argv[2:]:
        if arg in fonts:
            continue
        else:
            sys.exit("Invalid usage")


    name_font = sys.argv[2]
    word = input("Input: ")
    figlet.setFont(font = name_font)
    word = figlet.renderText(word)
    print(f"{word}")


if len(sys.argv) > 1 and len(sys.argv) == 2:

        sys.exit("Invalid usage")



if len(sys.argv) == 1:

    word = input("Input: ")
    name_font = random.choice(fonts)
    s = str(name_font)
    figlet.setFont(font = s)
    word = figlet.renderText(word)
    print(f"{word}")


