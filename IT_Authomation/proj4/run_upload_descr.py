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
#titles = ["name","weight", "description","image_name"]; d={}

for file in ifiles:   
    with open(os.path.join(upl_dir,file),'r') as opened:
        image = file.split()[0]
        data = opened.read()
        data = data.split("\n")
        fruit_dic = {"name": data[0], "weight": int(data[1].strip(" lbs")), "description": data[2], "image_name": image + ".jpeg"}
        response = requests.post(url, json=fruit_dic)
        response.raise_for_status()
        print(response.request.url)
        print(response.status_code)