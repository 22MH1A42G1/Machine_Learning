# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 14:13:17 2023
//find s algorithm
@author: LENOVO
"""

##find s algorithm

import pandas as pd
d=pd.DataFrame([['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
                ['Sunny','Warm','high','Strong','Warm','Same','Yes'],
                ['rainy','cold','high','Strong','Warm','change','no'],
                ['Sunny','Warm','Normal','Strong','cool','change','Yes']])

a=list(d.iloc[:,:-1].values)
b=list(d.iloc[:,-1].values)

s=0
for i in range(len(b)):
    if b[i]=='Yes' and s==0:
        g=a[i].copy()
        s+=1
        #print(g)
    if b[i]=='Yes' and s>0:
        for j in range(len(g)):
            if g[j]!=a[i][j]:
                g[j]='?'

print(g)