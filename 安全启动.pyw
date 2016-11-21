# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:17:06 2016

@author: Differlong
"""
import os
import win32api,win32con
import shutil
import glob
Disks = "CDEFGHIJKLMN"
purposeDir = r"C:\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
purposeDir = glob.glob(purposeDir)[0]
file = "安全启动.pyw"




def safe():
    win32api.MessageBox(0,"   欢迎使用电脑！   ", "洛鸣",win32con.MB_OK)

def poweroff():
    os.system("shutdown -s -t 0 -c 没有启动盘，立刻关机！")
    

def check(site):
    if not os.path.isfile(site):
        return False
    with open(site) as file:
        return  "人生苦短，我用Python"  in file
        

if not os.path.isfile(purposeDir + "/" + file):
    shutil.copyfile(file,purposeDir + "/" + file)
    
if any(map(check,(Disk +":/.password.txt" for Disk in Disks))):
   safe()
else:
   poweroff()

#os.remove(file)