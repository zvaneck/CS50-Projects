from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    fonts = figlet.getFonts()
    font = random.choice(fonts)
    current_font = figlet.setFont(font=font)
    print(figlet.renderText(input("Input: ")))
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--f":
        font = figlet.setFont(font=sys.argv[2])
        print(figlet.renderText(input("Input: ")))
    else:
        sys.exit('Invalid usage')
else:
    sys.exit('Invalid usage')
