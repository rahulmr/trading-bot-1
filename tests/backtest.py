from asyncio.proactor_events import _ProactorBasePipeTransport
from backtesting import Backtest, Strategy
import pandas as pd
import pandas_ta as ta
import numpy as np
import json
import datetime
from pre_processor import *

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
  slope = np.degrees(np.arctan(ema.diff()/20))
  return slope

class TradingBot(Strategy):

  p_slope = 5
  take_factor = 7
  stop_factor = 5

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
      previous_bottom = self.data.Low - (self.data.High - self.data.Low)*0.4


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
      previous_top = self.data.High + (self.data.High - self.data.Low)*0.4


    if not self.position:

      #opens a long position
      # if self.slope > self.p_slope/10 and self.data.Open < upper_band and self.data.Close > upper_band:
      #   change = (1 - (self.data.Open / self.data.Close)) * 100
      #   if change > 3.5:
      #     take = price + (self.data.Close - self.data.Open)*self.take_factor/10
      #     stop = price - (self.data.Close - self.data.Open)*self.stop_factor/10
      #     self.buy(tp=take, sl=stop)
      #   else:  
      #     take = price + (price - previous_bottom)*1.5
      #     self.buy(tp=take, sl=previous_bottom)

      # #opens a short positon
      # elif self.slope < self.p_slope/10*-1 and self.data.Open > lower_band and self.data.Close < lower_band:
      #   change = (1 - (self.data.Close / self.data.Open)) * 100
      #   if change > 3.5:
      #     take = price - (self.data.Open - self.data.Close)*self.take_factor/10
      #     stop = price + (self.data.Open - self.data.Close)*self.stop_factor/10
      #     self.sell(tp=take, sl=stop)
      #   else:
      #     take = price - (previous_top - price)*1.5
      #     self.sell(tp=take, sl=previous_top)

      if self.data.Open < upper_band and self.data.Close > upper_band:
        change = (1 - (self.data.Open / self.data.Close)) * 100
        if change > 3.5:
          take = price + (self.data.Close - self.data.Open)*self.take_factor/10
          stop = price - (self.data.Close - self.data.Open)*self.stop_factor/10
          self.buy(tp=take, sl=stop)
        else:  
          take = price + (price - previous_bottom)*1.5
          self.buy(tp=take, sl=previous_bottom)

      #opens a short positon
      elif self.data.Open > lower_band and self.data.Close < lower_band:
        change = (1 - (self.data.Close / self.data.Open)) * 100
        if change > 3.5:
          take = price - (self.data.Open - self.data.Close)*self.take_factor/10
          stop = price + (self.data.Open - self.data.Close)*self.stop_factor/10
          self.sell(tp=take, sl=stop)
        else:
          take = price - (previous_top - price)*1.5
          self.sell(tp=take, sl=previous_top)


# se ema pra cima e open entre BBands e close > banda superior = 1   OK
# se ema pra baixo e open entre BBands e close < banda inferir = -1   OK
# se já estiver numa operação, não pode entrar em outra
# se entrar em uma operação, precisa setar stop e gain
# identificar topos e fundos anteriores

######### running strategy

# running strategy
print("************************ADA STATS************************")
ada = Backtest(get_ada(), TradingBot, cash=100000)
ada_stats = ada.run()
# print(ada_stats)
ada.plot()

print("************************BNB STATS************************")
bnb = Backtest(get_bnb(), TradingBot, cash=100000)
bnb_stats = bnb.run()
# print(bnb_stats)
bnb.plot()

print("************************BTC STATS************************")
btc = Backtest(get_btc(), TradingBot, cash=100000)
btc_stats = btc.run()
# btc_stats = btc.optimize(
#   scale=range(10,40,2)
# )
print(btc_stats)
btc.plot()

print("************************DOGE STATS************************")
doge = Backtest(get_doge(), TradingBot, cash=100000)
doge_stats = doge.run()
# print(doge_stats)
doge.plot()

print("************************ETH STATS************************")
eth = Backtest(get_eth(), TradingBot, cash=100000)
eth_stats = eth.run()
# print(eth_stats)
eth.plot()

print("************************FINAL STATS************************")
result = ada_stats[4] + bnb_stats[4] + btc_stats[4] + doge_stats[4] + eth_stats[4]
profit = (result/500000 - 1)*100
print("ADA: ", "{:.2f}".format(ada_stats[4]))
print("BNB: ", "{:.2f}".format(bnb_stats[4]))
print("BTC: ", "{:.2f}".format(btc_stats[4]))
print("DOGE: ", "{:.2f}".format(doge_stats[4]))
print("ETH: ", "{:.2f}".format(eth_stats[4]))
print("Result:", "{:.2f}".format(result))
print("Profit", "{:.2f}".format(profit), "%")