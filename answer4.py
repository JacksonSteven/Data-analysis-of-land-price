import pandas as pd


df = pd.read_excel("answer1.xlsx")
df["city_name"].fillna(method="ffill", inplace=True)
city = set(df["city_name"].values)
def std(x, min, max):
    return (x - min) / (max - min)
li = []
for i in city:
    city_val = list(df[df.city_name == i]["unit_price"].values)
    max_v = max(city_val)
    min_v = min(city_val)
    df_ = df[df["city_name"] == i].copy()
    df_["unit_price"] = df_["unit_price"].apply(lambda x: std(x, max_v, min_v))
    li.append(df_)
    
df_suc = pd.concat(li)
df_suc.to_excel("test.xlsx", index=False)
