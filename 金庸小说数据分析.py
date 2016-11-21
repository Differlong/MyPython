# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 15:10:34 2016

@author: Differlong
"""

import jieba
import pyfpgrowth

#两个对应关系
idPool = {}# id --word
wordPool = {}# word --id


newId = (i for i in range(1000000000000))


def wordList(file):
    with open(file)as f:
        text = f.read();
        s = list(jieba.cut(text))
        return s




def word2Sentence(s):
    global idPool
    global wordPool
    punctuation="，。、‘’“；：！”\n？《》【】　（）#@…\t "
    sentenceList = []
    sentence = []
    for word in s:
        if word not in punctuation:
            if word not in wordPool:
                wordId = next(newId)
                idPool[wordId] = word
                wordPool[word] = wordId
                sentence.append(wordId)
            else:
                sentence.append(wordPool[word])
        elif word in "？！。；\n":
            if sentence!=[]:
                sentenceList.append(tuple(sentence))
                sentence.clear()
    return sentenceList

file = open("射雕英雄传分词.txt","w")
s = wordList("金庸小说/射雕英雄传.txt")
sentenceList = word2Sentence(s)

for sentence in sentenceList:
    for word in sentence:
        print(word,end=" ",file=file)
    print("\n",file=file)

#实现了分词，变成了一个个list
#然后就是词频分析
file.close()


#patterns = pyfpgrowth.find_frequent_patterns(sentenceList, 2)
#rules = pyfpgrowth.generate_association_rules(patterns, 0.7)
