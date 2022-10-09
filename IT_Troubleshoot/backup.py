
'''
The hierarchy of the subfolders of /data/prod, data is from different projects 
(e.g., , beta, gamma, kappa) and they're independent of each other. You have 
to use multiprocessing and subprocess module methods to sync the data 
from /data/prod to /data/prod_backup folder.

Try applying multiprocessing, which takes advantage of the idle CPU cores 
for parallel processing. Here, you have to use multiprocessing and subprocess 
module methods to sync the data from /data/prod to /data/prod_backup folder.

Hint: os.walk() generates the file names in a directory tree by walking the 
tree either top-down or bottom-up. This is used to traverse the file system in Python.

Dailysync.py
'''

import subprocess
from multiprocessing import Pool
import os

global src
src = "{}/data/prod/".format(os.getenv("HOME"))


def sync_data(folder):
    dest = "{}/data/prod_backup/".format(os.getenv("HOME"))
    subprocess.call(["rsync", "-arq", folder, dest])
    print("Handling {}".format(folder))


if __name__ == "__main__":
    folders = []
    root = next(os.walk(src))[0]
    dirs = next(os.walk(src))[1]

    for dir in dirs:
        folders.append(os.path.join(root, dir))

    pool = Pool(len(folders)) if len(folders) != 0 else Pool(1)
    pool.map(sync_data, folders)
    
    
    
# #!/usr/bin/env python3

# from multiprocessing import Pool
# import os
# import subprocess

# src = "/home/student-01-#######/data/prod"
# dirs = next(os.walk(src))[1]

# def backingup(dirs):
#     dest = "/home/student-01-#######/data/prod_backup"
#     subprocess.call(["rsync", "-arq", src+'/'+ dirs, dest])




# p = Pool(len(dirs))
# p.map(backingup, dirs)