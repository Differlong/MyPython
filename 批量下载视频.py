# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:18:24 2016

@author: Differlong

version = 1.0

改进空间：
1.增加批量下载视频的站点，包括优酷，youtube，bilibili等

"""

import os
import requests
from bs4 import BeautifulSoup



videoId = 0


def downloadVideo(url):
    global videoId
    fold = str(videoId)
    if not os.path.isdir(fold):
        os.mkdir(fold)
    os.chdir(fold)
    os.system("you-get %s"%url)
    os.chdir("..")
    videoId += 1

#downloadVideo(url)

def getUrl(keyWord,num = 1):
    #下载视频数小于20
    s = []
    for page in range((num-1)//20+1):
        searchUrl = "http://www.soku.com/search_video/q_"+keyWord+"&page="+str(page)
        headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"}
        try:
            resp = requests.get(searchUrl,headers=headers).text
            soup = BeautifulSoup(resp,"lxml")
            urlList = soup.findAll("div",{"class":"v"})
            for i in range(min(num,len(urlList))):
                s.append(urlList[i].a.get("href"))
        except Exception as e:
            print("Connection Error",e)
    return s


if __name__ == "__main__":
    keyWord = ""
    num = 200 #
    path = "./dota2"
    
    
    if not os.path.isdir(path):
        os.mkdir(path)
    os.chdir(path)
    urls = getUrl(keyWord,num)
    for url in urls:
        downloadVideo(url)