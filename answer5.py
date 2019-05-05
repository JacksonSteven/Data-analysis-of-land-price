import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
sns.set_style("darkgrid",{"font.sans-serif":['KaiTi', 'Arial']})

#导入数据
df = pd.read_excel('answer1.xlsx')
df.head()

#插入2007-2018缺失年份，向前填充
df['city_name'].fillna(method="ffill", inplace=True)
import numpy as np
city = df["city_name"].values 
for i in city:
    year = list(df[df["city_name"] == i]["year"].values)
    count = len(year)
    tmp = set()

    if year[0]>2007 or year[-1]<2019:
        for k in range(12):
            year[0]=2007
            year_i = year[0] + k
            tmp.add(year_i)
        cont = tmp - set(year)
        if len(cont) != 0:
            for j in cont:
                d = {"city_name": i, "year": j, "unit_price": np.nan}
                df = df.append(d, ignore_index=True)
df = df.sort_values(by=["city_name", "year"])
df["unit_price"].fillna(method="ffill", inplace=True)



#提取2007-2018年数据，整理数据框为合适格式
df=df[(df.year==2007)|(df.year==2008)|(df.year==2009)|(df.year==2010)|(df.year==2011)|(df.year==2012)|(df.year==2013)|(df.year==2014)|(df.year==2015)|(df.year==2016)|(df.year==2017)|(df.year==2018)]
df2 = df.groupby(['city_name','year']).sum()
g = df2.unstack('year',fill_value=0)

#画图，保存
fig=sns.heatmap(g);
fig.get_figure().savefig('T5.png')
