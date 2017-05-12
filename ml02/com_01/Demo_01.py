#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: fxl
@site: 
@software: PyCharm Community Edition
@file: Demo_01.py
@time: 2017-5-10 9:15
"""

from numpy import *
import operator

##给出训练数据以及对应的类别
def createDataSet():
    group=array([[1.0,2.0],[1.2,0.1],[0.1,1.4],[0.3,3.5]])
    labels=['A','A','B','B']
    return group,labels

###通过KNN进行分类
def classify(input,dataset,label,k):
    dataSize=dataset.shape[0]
    diff=tile(input,(dataSize,1))-dataset
    sqdiff=diff**2
    squareDist=sum(sqdiff,axis=1)
    dist=squareDist**0.5

    sortedDistIndex=argsort(dist)

    classCount={}
    for i in range(k):
        voteLabel=label[sortedDistIndex[i]]
        classCount[voteLabel]=classCount.get(voteLabel,0)+1

    maxCount=0
    for key,value in classCount.items():
        if value > maxCount:
            maxCount=value
            classes=key

    return classes


dataSet,labels=createDataSet()
input=array([1.1,0.3])
k=3
output=classify(input,dataSet,labels,k)
print("测试数据为：",input,"分类结果为：",output)















