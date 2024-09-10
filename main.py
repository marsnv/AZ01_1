import pandas as pd
df = pd.read_csv('DataAnalyst.csv')
print(df.head())
print(df.info())
print(df.describe())

print('*************************')
df = pd.read_csv('dz.csv')
df.fillna({'City':'Неизвестно', 'Salary':0}, inplace=True)
group = df.groupby('City')['Salary'].mean()
print(group)

