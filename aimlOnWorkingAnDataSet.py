# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 14:00:48 2023

@author: Aditya

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv(r"C:\Users\LENOVO\Desktop\aiml\data.csv",encoding='latin1')

data = pd.read_csv(r"C:\Users\LENOVO\Desktop\aiml\data.csv", encoding='latin1')

data['timestamp'] = pd.to_datetime(data['timestamp'], errors='coerce')

data['timestamp'] = pd.to_datetime(data['timestamp'], format='%d-%m/%Y %H:%M:%S')

column_new = data.iloc[:,0]

db=pd.DataFrame({"year": column_new.dt.year,
              "month": column_new.dt.month,
              "day": column_new.dt.day,
              "hour": column_new.dt.hour,
              "dayofyear": column_new.dt.dayofyear,
              "dayofweek": column_new.dt.dayofweek,
              "weekday": column_new.dt.weekday,
              "quarter": column_new.dt.quarter,
             })

newdataset=data.drop('timestamp',axis=1)
data1=pd.concat([db,newdataset],axis=1)
data1=data1.dropna()
print(data1)
x_column_indices = [0, 1, 2, 3, 4, 5]  # Adjust these indices
y_column_indices = [6, 7, 8, 9, 10, 11]  # Adjust these indices

x = data1.iloc[:, x_column_indices].values
y = data1.iloc[:, y_column_indices].values



from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=9)
    
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=1)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)


from sklearn import metrics
print(metrics.accuracy_score(y_test,y_pred)*100)

from sklearn import metrics

for i in range(y.shape[1]):
    y_true_i = y_test[:, i]
    y_pred_i = y_pred[:, i]
    
    accuracy = metrics.accuracy_score(y_true_i, y_pred_i)
    print(f"Accuracy for target variable {i+1}: {accuracy*100:.2f}%")
from sklearn.metrics import hamming_loss

hamming_loss_value = hamming_loss(y_test, y_pred)
print(f"Hamming Loss: {hamming_loss_value}")
