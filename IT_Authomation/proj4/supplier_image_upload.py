
#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
curpath = os.getcwd()
images_dir = 'supplier-data/images/'
upl_dir = curpath + '/' + images_dir
print(upl_dir)
ifiles = os.listdir(upl_dir)
for file in ifiles:
    if 'jpeg' in file:
        with open(os.path.join(upl_dir,file),'rb') as opened:
            r = requests.post(url, files={'file': opened})
            print(r)