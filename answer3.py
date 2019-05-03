import pandas as pd
impor numpy as np

df = pd.read_excel("answer1.xlsx")
city = df["city_name"].values
df["city_name"].fillna(method="ffill", inplace=True) 
for i in city:
    year = list(df[df["city_name"] == i]["year"].values)
    count = len(year)
    tmp = set()
    for k in range(count):
        year_i = year[0] + k
        tmp.add(year_i)
    cont = tmp - set(year)
    if len(cont) != 0:
        print(i)
        for j in cont:
            d = {"city_name": i, "year": j, "unit_price": np.nan}
            df = df.append(d, ignore_index=True)
df = df.sort_values(by=["city_name", "year"])
df["unit_price"].fillna(method="ffill", inplace=True)
df.to_excel("answer3.xlsx", index=None)
