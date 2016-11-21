# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 08:51:25 2016

@author: Differlong
"""

    



#==============================================================================
 #def change(path="."):
 #    files = os.listdir(path)
 #    for file in files:
 #        file = path + "/" + file
 #        if os.path.isdir(file):
 #            change(file)
 #            continue
 #        if os.path.isfile(file):
 #            a,b = os.path.splitext(file)
 #            if b ==".gif":
 #                newName = a + ".jpg"
 #                os.rename(file,newName)
 #
 #
 #change()
#==============================================================================

#==============================================================================
# 
# 
# for a,b,c in os.walk("."):
#     for file in c:
#         if ".gif" in file:
#             newName = a +"/" + file.split(".")[0] + ".jpg"
#             os.rename(a+"/" + file,newName)
#==============================================================================
