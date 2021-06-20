import os 
import pandas as pd

# read excels and concat dataframe
xls = os.listdir("data")
dfs = []
for i in xls:
    df = pd.read_excel(f"data/{i}", index_col=0, dtype={"code": str})
    dfs.append(df)
df = pd.concat(dfs)


# filter
cond = df['day'] == "12월 결산"
df = df[cond]

# screening
cond = (df['gp/a'] >0) & (df['pbr'] > 0)
df2 = df[cond].copy()
df2['rank1'] = df2['gp/a'].rank(ascending=False)    # gp/a는 높으면 1등
df2['rank2'] = df2['pbr'].rank()                    # pbr는 낮은면 1등 
df2['rank'] = df2['rank1'] + df2['rank2']
df2.set_index('code', inplace=True)
df2.sort_values(by='rank').head(n=30).to_excel("output.xlsx")