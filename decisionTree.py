# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 13:58:57 2023

Ques: Write a program to demonstrate the working of the decision tree classifier. Use appropriate dataset 
for building the decision tree and apply this knowledge to classify a new sample

@author: _aditya
"""

import pandas as pd

data=pd.read_csv(r"C:\Users\LENOVO\Desktop\aiml\iris.csv")
#print(data.head())
data.dropna(inplace=True)

x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=4)

#DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(criterion='entropy')

##RandomForestClassifier
##from sklearn.ensemble import RandomForestClassifier
##model=RandomForestClassifier()

##LogisticRegression
##from sklearn.linear_model import LogisticRegression
##model=LogisticRegression()

##SupportVector
##from sklearn.svm import SVC
##model=SVC()

##naive_bayes
##from sklearn.naive_bayes import GaussianNB
##model=GaussianNB()

model.fit(xtrain,ytrain)

ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred)*100)
#3--

(model.predict([[1.2,2.1,4.5,6.1]]))

#print(x)
