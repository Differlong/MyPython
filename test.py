# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:17:06 2016

@author: Differlong
"""
import os
import win32api,win32con
Disks = "CDEFGHIJKLMN"

def safe():
    win32api.MessageBox(0,"欢迎使用电脑！", "洛鸣",win32con.MB_OK)

def poweroff():
    win32api.MessageBox(0, "Big Brother Is Watching You!!!", "安全警告",win32con.MB_OK)
    os.startfile("shutdown -s -t 5 -c 没有启动盘，5秒后关机！！！")

def check(site):
    return os.path.isfile(site)



if any(map(os.path.isfile,(Disk +":/password.pwd" for Disk in Disks))):
   safe()
else:
   poweroff()