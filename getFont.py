from PIL import ImageGrab
import os
import pyautogui as pag
import time


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


for i in range(48, 123):
    clear()
    print(i, chr(i))
    # codes.append(i)
    # x1, y1 = pag.position()
    # input("\r")
    # x2, y2 = pag.position()
    pag.hotkey("win", "shift", "s")
    input("\r")
    # time.sleep(1)
    # pag.moveTo(x1, y1)
    # pag.dragRel(x2 - x1, 75, duration=1)
    # time.sleep(1)
    im = ImageGrab.grabclipboard()
    im.save(f'./out/{i}.png', 'PNG')

# for i in range(48, 123):
#     print(chr(i), end=", ")
