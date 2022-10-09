'''Project Problem Statement
To complete this module, you'll need to write a script that processes a bunch of images. 
It turns out that your company is in the process of updating its website, and a design 
contractor has been hired to create some new icon graphics for the site. However, 
the contractor has delivered the final designs and they’re in the wrong format, 
rotated 90° and too large. You’re unable to get in contact with the designers and your 
own deadline is approaching fast. You’ll need to use Python to get these images ready for launch!

So, how will you do this? You'll need to go through a folder full of images and operate 
with each of them. On each image, you'll use PIL methods like the ones we saw in the 
examples, and then write the new images in the right place.
'''


import os
from re import L
from PIL import Image
curpath = os.getcwd()
print(curpath)
for root, dirs, files in os.walk(curpath, topdown=False):
    for name in files:
        # print(name)
        #print(os.path.join(root, name))
        try:
            img = Image.open(os.path.join(root, name))
            #print(img)
            new_img = img.resize((128,128)).rotate(270).convert("RGB")
            #print(new_img.size)
            outfile = os.path.splitext(os.path.join(root, name))[0] + ".jpg"
            #outfile = '/opt/icons/' + name + ".jpg" #<-- was in lab
            #print('OUTFILER',outfile)
            new_img.save(outfile, quality=100)
            print(os.path.join(root, name))
            #os.remove(os.path.join(root, name))
            print(new_img.format)
            #new_img.save(os.path.splitext(os.path.join(root, name)) + ".jpg", "JPEG", quality=100)
        except:
            continue
            
    


      