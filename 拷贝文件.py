# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 16:50:35 2016

@author: Differlong
"""

import shutil
import glob
import os
file = "拷贝文件.py"

purposeDir = r"C:\Users\*\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

purposeDir = glob.glob(purposeDir)[0]





shutil.copyfile(file,purposeDir + "/" + file)

os.remove("拷贝文件.py")

print("hello World")