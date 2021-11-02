import os
import sys
from PIL import Image

import os
from os import listdir, makedirs
from os.path import isfile, join
path = './gray'  # Source Folder
dstpath = './graySized'  # Destination Folder
try:
    makedirs(dstpath)
except:
    print("Directory already exist, images will be written in same folder")
# Folder won't used
files = list(filter(lambda f: isfile(join(path, f)), listdir(path)))
size = 100, 200
for image in files:
    print(image)

    outfile = f"{dstpath}/{image}"
    print(outfile)
    if image != outfile:
        try:
            im = Image.open(image)
            print(im)
            # im.thumbnail(size, Image.ANTIALIAS)
            im = im.resize(size)
            im.save(outfile, "png")
        except IOError:
            print("cannot create thumbnail for '%s'" % image)
