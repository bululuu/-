# -*- coding: utf-8 -*-
"""
Created on Wed May 20 09:26:13 2020

@author: bululu
"""


from Apriori import apriori
import pandas as pd
import numpy as np

datafile = 'visit-patterns-by-census-block-group\cbg_patterns.csv'
#数据导入
data =pd.read_csv(datafile,encoding='utf-8')
data.info()
brand=data['top_brands']
print(brand)
dataSet=brand
L,suppData=apriori(dataSet)
i=0
for one in L:
    print("项数为 %s 的频繁项集：" % (i+1),one,"\n")
    i +=1
 print "minConf=0.7时："
    rules = generateRules(L,suppData, minConf=0.7)

    print "\nminConf=0.5时："
    rules = generateRules(L,suppData, minConf=0.5)

