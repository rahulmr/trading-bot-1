from asyncio.proactor_events import _ProactorBasePipeTransport
from backtesting import Backtest, Strategy
import pandas as pd
import pandas_ta as ta
import numpy as np
import json
import datetime

file = open('./data/ADA.json')

asset_data = json.load(file)

df = pd.DataFrame(asset_data, columns=['timestamp', 'Open','High','Low','Close','Volume','x1','x2','x3','x4','x5','x6'])

df = df.drop(columns=['x1','x2','x3','x4','x5','x6'])

df['timestamp'] = pd.to_datetime(df['timestamp'],unit='ms')

df = df.set_index('timestamp')

df = df.astype(float)

df_t = df
df_t.ta.ema(length = 80, append = True)
df_t['slope'] = np.degrees(np.arctan(df_t['EMA_80'].diff()/20))
# print(df_t.to_string())

################## buy and sell logic 

def bbands(data):
  bbands = ta.bbands(close = data.Close.s, length = 20, std = 0.38)
  return bbands.to_numpy().T[:3]

def ema(data):
  ema = ta.ema(close = data.Close.s, length = 80)
  return ema.to_numpy()

def ema20(data):
  ema = ta.ema(close = data.Close.s, length = 8)
  return ema.to_numpy()

def slope(data):
  ema = ta.ema(close = data.Close.s, length = 80)
  slope = np.degrees(np.arctan(ema.diff()/20))*10000
  print(slope.to_string())
  return slope

class TradingBot(Strategy):

  def init(self):
    self.bbands = self.I(bbands, self.data)
    self.ema = self.I(ema,self.data)
    # self.ema20 = self.I(ema20,self.data)
    self.slope = self.I(slope,self.data)

  def next(self):
    lower_band = self.bbands[0]
    upper_band = self.bbands[2]
    price = self.data.Close[-1]

    #define previuos bottom
    if self.data.Low[-3] < self.data.Low[-2] and self.data.Low[-3] < self.data.Low[-1] and self.data.Low[-3] < self.data.Low:
      previous_bottom = self.data.Low[-3]
    elif self.data.Low[-2] < self.data.Low[-3] and self.data.Low[-2] < self.data.Low[-1] and self.data.Low[-2] < self.data.Low:
      previous_bottom = self.data.Low[-2]
    elif self.data.Low[-2] > self.data.Low[-1] and self.data.Low > self.data.Low[-1]:
      previous_bottom = self.data.Low[-1]
    elif self.data.Low[-1] < self.data.Low:
      previous_bottom = self.data.Low[-1]
    else:
      previous_bottom = self.data.Low

    #define previous top
    if self.data.High[-3] > self.data.High[-2] and self.data.High[-3] > self.data.High[-1] and self.data.High[-3] > self.data.High:
      previous_top = self.data.High[-3]
    elif self.data.High[-2] > self.data.High[-3] and self.data.High[-2] > self.data.High[-1] and self.data.High[-2] > self.data.High:
      previous_top = self.data.High[-2]
    elif self.data.High[-2] < self.data.High[-1] and self.data.High < self.data.High[-1]:
      previous_top = self.data.High[-1]
    elif self.data.High[-1] > self.data.High:
      previous_top = self.data.High[-1]
    else:
      previous_top = self.data.High    

    if not self.position:
      #opens a long position
      # if self.slope > 3.5 and self.data.Open >= lower_band and self.data.Open <= upper_band and self.data.Close > upper_band:
      if self.slope > 3 and self.data.Open < upper_band and self.data.Close > upper_band:
        take = price + (price - previous_bottom)*1.5
        self.buy(tp=take, sl=previous_bottom)

      #opens a short positon
      elif self.slope < -3 and self.data.Open > lower_band and self.data.Close < lower_band:
      # elif self.data.Open >= lower_band and self.data.Open <= upper_band and self.data.Close < lower_band:  
        take = price - (previous_top - price)*1.5
        self.sell(tp=take, sl=previous_top)


# se ema pra cima e open entre BBands e close > banda superior = 1   OK
# se ema pra baixo e open entre BBands e close < banda inferir = -1   OK
# se já estiver numa operação, não pode entrar em outra
# se entrar em uma operação, precisa setar stop e gain
# identificar topos e fundos anteriores

######### running strategy

bt = Backtest(df, TradingBot, cash = 10_000)
stats = bt.run()
print(stats)
bt.plot()