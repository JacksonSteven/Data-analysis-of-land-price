import pandas as pd

df = pd.read_excel('answer3.xlsx')
df['city_name'].fillna(method='ffill', inplace=True)
df=df.groupby(['city_name']).unit_price.describe()
df.to_excel("answer5.xlsx")
