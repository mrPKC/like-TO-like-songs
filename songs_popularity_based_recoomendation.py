import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")

column = ['song_name', 'song_popularity']
df = pd.read_csv("songs recommendation\song_data.csv",
                 sep=",", header=None, skiprows=[0])

df = df[[0, 1]]
df.columns = column

dfn = df.set_index("song_name", drop=False)


def predict(x):
    a = np.array(dfn.loc[x])
    if(len(a) == 2):
        v = df.loc[df['song_popularity'] == a[1]].head(10)
    else:
        v = df.loc[df['song_popularity'] == a[0][1]].head(10)
    a = np.array(v)
    b = a.tolist()
    return b


# x = input()
# v = predict(x)
# v.reset_index(drop=True, inplace=True)
# print(v['song_name'].head())
