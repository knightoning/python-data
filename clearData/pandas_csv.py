import pandas as pd

data = pd.read_csv('2022-1.csv')

data.head()

print(data)

print(data['CardNo'])

print(data[['CardNo','Status']])

print(data['CardNo'][:6])

print(data['Id'] < 116512)