###knn alogorithm..//
import pandas as pd
import numpy as  np
data=pd.read_csv(r"C:\Users\LENOVO\Desktop\aiml\iris.csv")
##print(data.head())#reading the data
data.dropna(inplace=True)

x=np.array(data.iloc[:,:-1])
y=data.iloc[:,-1].values
print(x)

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=9)

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=3)

model.fit(xtrain,ytrain)

ypred=model.predict(xtest)

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred)*100)





