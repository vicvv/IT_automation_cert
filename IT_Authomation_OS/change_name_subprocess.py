#!/usr/bin/env python3
# works with bash change_name.sh
import sys
import subprocess

infile = sys.argv[1]
with open(infile, mode='r',encoding='UTF-8') as file:
    for line in  file.readlines():
      sline = line.strip()
      nline = sline.replace("jane", 'jdoe')
      path = '/home/student-00-25f6f747abf1'
      
      subprocess.run(["mv",path+sline,path+nline])