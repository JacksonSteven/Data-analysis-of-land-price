import pandas as pd

#拆分之后再求商
df = pd.read_excel('answer1.xlsx')
grouped_price = df['price'].groupby([df['city_name'],df['year']]).sum()
grouped_area = df['area'].groupby([df['city_name'],df['year']]).sum()
merge=grouped_price.div(grouped_area)
merge.to_excel('answer2.xlsx', sheet_name='out')
