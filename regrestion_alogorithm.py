##Regrestion Alogorithm
import pandas as pd
import numpy as  np
##import matplotlib.pyplot as plt
a=[i for i in 'abcdefghijklmn']

data=pd.read_csv(r"C:\Users\LENOVO\Desktop\aiml\boston.csv")
x=np.array(data.iloc[:,:-1])
y=data.iloc[:,-1].values
print(x)

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=2)

from sklearn.linear_model import LinearRegression
model = LinearRegression()

