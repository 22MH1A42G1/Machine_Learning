# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:12:59 2023

@author: LENOVO
"""

#random forest regressor
import pandas as pd

d=pd.read_csv(r"C:\Users\LENOVO\Desktop\aiml\fires.csv")

d.head()
d.columns

d.shape
d.drop([124,122,123,168],axis=0,inplace=True)
d.shape

x=d.iloc[ : , :-1].values
y=d.iloc[: ,-1].values

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(criterion='entropy')
model.fit(xtrain,ytrain)


ypred=model.predict(xtest)
from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred))

print(model.predict([[2,	6,	2012,	29,	61,	13,	1.3,	64.4,	4.1,	7.6,	1,	3.9,	0.4]]))


sample = pd.read_csv(r"C:\Users\LENOVO\Desktop\aiml\fires2.csv")
sample.shape

p=model.predict(sample)
p

sample['status']=p


sample.to_csv(r'C:\Users\LENOVO\Desktop\aiml\predicted.csv')
