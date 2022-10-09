

import psutil
import shutil

def cpu_usage():
    cpuusage = psutil.cpu_percent(1)
    return cpuusage > 75
    

def disck_usage():
    du = shutil.disk_usage("/")
    free = du.free/du.total *100
    return free < 20

if not cpu_usage and not disck_usage:
    print("Error")
else:
    print('OK')
    

   
   
'''
#!/usr/bin/env python3
import shutil
import psutil
def check_disk_usage(disk):
    """Verifies that there's enough free space on disk"""
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20
def check_cpu_usage():
    """Verifies that there's enough unused CPU"""
    usage = psutil.cpu_percent(1)
    return usage > 75
# If there's not enough disk, or not enough CPU, print an error
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
else:
    print("Everything ok")
'''                        
                           

