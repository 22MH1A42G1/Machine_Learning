import pandas as pd
names = []
for i in "abcdefghijklmno":
    names.append(i)
data=pd.read_csv(r"C:\Users\LENOVO\Desktop\aiml\income.csv")
data.head()
data.shape()

data.isna().sum()

data['b'].value_counts()
data['b']=data['b'].replace(to_replace=' ?',value = ' Private')

from sklearn.preprocessing import LableEncoder
le = LableEncoder()
for i in 'bdfghijn':
    data[i]=le.fit_transform(data[i])
x = data.iloc[:,:-1].values
y = data.iloc[:,:-1].values

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(x, y, test_size = 0.2, random_state = 0)

from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(criterion='entropy')
model.fit(xtrain,ytrain)

ypred = model.predict(xtest)

from sklearn.metrics import accuracy_score
print(accuracy_score(ytest,ypred))
