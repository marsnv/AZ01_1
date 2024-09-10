import pandas as pd
df = pd.read_csv('DataAnalyst.csv')
print(df.head())
print(df.info())
print(df.describe())
print(df['Location'])