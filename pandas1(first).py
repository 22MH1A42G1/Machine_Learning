import pandas as pd

data = pd.read_csv(r"C:\Users\LENOVO\Desktop\aiml\IMDB-Movie-Data.csv", encoding='latin1')

print(data['Year'].value_counts())
print(data.shape)
print(data.size)
##data.ndim
##data.head(10)
##data.tail()
##data.columns
##data['Genre']
##data['Revenue (Millions)'].max()
##data['Revenue (Millions)'].min()
##data['Revenue (Millions)'].mean()
##data['Revenue (Millions)'].sum()
##data['Year'].unique()
##data.describe()
##print(data['Year'].count())
##data.isna()
##data.isna().sum()
##data.dropna(inplace=True)
##data.drop(['Revenue (Millions)','Metascore'],axis=1,inplace=True)
# data.shape##
##data=data.append(data)
##data=pd.concat(data,data)
##data=pd.concat(data)
##data._append(data)
##data.drop_duplicates(inplace=True)
##data[data['Year'] == 2016].count()
