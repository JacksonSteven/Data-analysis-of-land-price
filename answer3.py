import pandas as pd

df = pd.read_excel("answer1.xlsx")
df.head()
df['city_name'].fillna(method='ffill', inplace=True)
df=df.groupby(['city_name','year']).sum()
df=df.unstack('year')
df.fillna(method='ffill',axis=1 ,inplace=True)
df=df.stack('year')
df.to_excel("answer3.xlsx")
