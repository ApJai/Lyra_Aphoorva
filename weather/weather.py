import pandas as pd

df = pd.read_csv('weather.dat',sep='\s+')
df = df.iloc[:-1 , :]

cols = ['MxT', 'MnT']
for col in cols:
    df[col] = df[col].map(lambda x: str(x).lstrip('*').rstrip('*')).astype(int)


df['spread'] = df['MxT'] - df['MnT']
max_spread = df[["Dy","spread"]].max()
print(max_spread)
