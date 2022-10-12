import pandas as pd
import pandas_ta as ta
import numpy as np
import json

####### get data

file = open('./data/ADA.json')

asset_data = json.load(file)

df = pd.DataFrame(asset_data, columns=['timestamp', 'open','high','low','close','volume','x1','x2','x3','x4','x5','x6'])

df = df.drop(columns=['x1','x2','x3','x4','x5','x6'])

df = df.astype(float)
df['timestamp'] = df['timestamp'].astype(int)

################ build dataframe with indicators

df.reset_index()
df.ta.ema(length = 80, append = True)
df.ta.bbands(length = 20, std = 0.38, append = True)

df.drop(df.index[0:80], inplace=True)

for row in range(81, len(df)+80):
  df.loc[row,'EMA_SLOPE'] = df.loc[row,'EMA_80'] - df.loc[row-1,'EMA_80']

#####################
### Requirements: ###
# se ema pra cima e open entre BBands e close > banda superior = 1   OK
# se ema pra baixo e open entre BBands e close < banda inferir = -1   OK
# se já estiver numa operação, não pode entrar em outra
# se entrar em uma operação, precisa setar stop e gain
# identificar topos e fundos anteriores


