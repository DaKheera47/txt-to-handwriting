# Importing Library
from PIL import Image
from sys import argv
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# if you'd rather not use the command line, put the path to your file here
fileName = "dummy.txt"  # path of your text file

# read file that user wants converted from command line. If file can't be read, assign
# the file to a file in the directory
try:
    txt = open(argv[1], "r")
except IndexError:
    print("No file entered. Using default file...")
    txt = open(fileName, "r")
except FileNotFoundError:
    print("Could not find file. Using default file...")
    txt = open(fileName, "r")

gapFromLeft = 100
lineHeight = 100

# path of page(background)photo (I have used blank page)
BG = Image.open("myfont/bg.png")
sheet_width = BG.width
distX, distY = gapFromLeft, lineHeight


# for each letter in the uploaded txt file, read the unicode value and replace it with
# the corresponding handwritten file in the "myfont" folder.
for i in txt.read():
    # clear()
    # print(i)
    if i == "\n":
        distX, distY = gapFromLeft, distY + lineHeight
        continue

    if ord(i) >= 48 and ord(i) <= 85:

        cases = Image.open(f"./out/{ord(i)}.png")
        BG.paste(cases, (distX, distY))
        size = cases.width
        height = cases.height
        distX += size

        # if we've reached end of sheet or if next letter will exceed line
        if sheet_width < distX or len(i) * 115 > (sheet_width - distX):
            # goto next line
            distX, distY = gapFromLeft, distY + lineHeight

# print(distX)
# print(sheet_width)
BG.save("./out4.png")
