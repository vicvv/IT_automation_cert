#!/usr/bin/env python3
import os
from PIL import Image

curpath = os.getcwd()
print(curpath + '/supplier-data/images')
p = curpath + '/supplier-data/images'
for root, dirs, files in os.walk(p, topdown=False):
    for name in files:
        try:
            img = Image.open(os.path.join(root, name))
            new_img = img.resize((600,400)).convert("RGBA").convert("RGB")
            outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpeg"
            new_img.save(outfile, quality=100)
            print(os.path.join(root, name))
            print(new_img.format, new_img.size)
            print(p + '/', name)
            os.remove(p + '/', name)
            
        except:
            continue