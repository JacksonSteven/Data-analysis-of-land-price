
import pandas as pd
input_file =r'land_data.xlsx'
df = pd.read_excel(input_file, sheetname='Sheet1')
grouped = df['unit_price'].groupby([df['city_name'],df['year']]).mean()
grouped.to_excel('answer1.xlsx', sheet_name='out')#导出表单名为"out"
