import pandas as pd

data = pd.read_csv(r"C:\Users\LENOVO\Desktop\aiml\IMDB-Movie-Data.csv", encoding='latin1')
# data=data._append(data,data)
# data.drop_duplicates(inplace=True)
# data.shape

print(data[data['Year'] == 2016].count())

print(data[data['Revenue (Millions)'] > 250])

var = data[(data['Year'] == 2016) & (data['Revenue (Millions)'] > 250)]
print(var)

