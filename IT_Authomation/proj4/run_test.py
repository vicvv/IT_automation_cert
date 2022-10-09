#! /usr/bin/env python3
import os
import requests
import json

url = "http://localhost/fruits/"
curpath = os.getcwd()
desctiption_dir = 'supplier-data/descriptions/'
upl_dir = curpath + '/' + desctiption_dir
print(upl_dir)
ifiles = os.listdir(upl_dir)
titles = ["name","weight", "description","image_name"]; 

for file in ifiles:
    i=0;  
    with open(os.path.join(upl_dir,file),'r') as opened:
        img = file.split()[0]
        data = opened.read()
        data = data.split("\n")
        d ={"name": data[0], "weight": int(data[1].strip(" lbs")), "description": data[2], "image_name": img + ".jpeg"}
        r = requests.post(url, json=d)
        print(r)