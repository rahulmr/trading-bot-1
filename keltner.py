from xmlrpc.server import resolve_dotted_attribute
from backtesting import Backtest, Strategy
from assets import *
import pandas as pd
import pandas_ta as ta
import numpy as np
import json

# acima da keltner superior por ao menos 3 candles
#
# VENDA:
# Kelner caindo
# preco abaixo das keltners
# rsi acima de 80
# conda activate mlp => deactivate

kelt_trigger = 0

def keltner(data):
    keltner = ta.kc(high=data.High.s, low=data.Low.s,
                    close=data.Close.s, length=21, scalar=0.38)
    return keltner.to_numpy().T[:3]

def rsi(data):
    rsi = ta.rsi(close=data.Close.s, length=2)
    return rsi.to_numpy()

def ema8(data):
    ema = ta.ema(close=data.Close.s, length=64)
    return ema.to_numpy()

def ema80(data):
    ema = ta.ema(close=data.Close.s, length=640)
    return ema.to_numpy()

class TradingBot(Strategy):

    low_rsi = 20
    high_rsi = 80

    def init(self):
        self.keltner = self.I(keltner, self.data)
        self.rsi = self.I(rsi, self.data)
        self.ema8 = self.I(ema8, self.data)
        self.ema80 = self.I(ema80, self.data)


    def next(self):
        lower_band = self.keltner[0]
        upper_band = self.keltner[2]
        price = self.data.Close
        kelter_width = 100 * (1 - lower_band/upper_band) 

        # define previuos bottom
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

        # define previous top
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
            # opens a long position
            if kelter_width > kelt_trigger/10 and self.rsi[-1] < self.low_rsi and self.data.Open > self.data.Close and self.data.Close > upper_band:
                take = price + (price - previous_bottom)*2
                if(take != previous_bottom):
                    self.buy(tp=take, sl=previous_bottom)

            # opens a short positon
            if kelter_width > kelt_trigger/10 and self.rsi[-1] > self.high_rsi and self.data.Open < self.data.Close and self.data.Close < lower_band:
                take = price - (previous_top - price)*2
                if(take != previous_top):
                    self.sell(tp=take, sl=previous_top)

# running strategy
print("************************ADA STATS************************")
kelt_trigger = 3
ada = Backtest(get_ada(), TradingBot, cash=100000)
ada_stats = ada.run()
print(ada_stats)
ada.plot()

print("************************BNB STATS************************")
kelt_trigger = 0
bnb = Backtest(get_bnb(), TradingBot, cash=100000)
bnb_stats = bnb.run()
print(bnb_stats)
bnb.plot()

print("************************BTC STATS************************")
kelt_trigger = 4
btc = Backtest(get_btc(), TradingBot, cash=100000)
btc_stats = btc.run()
print(btc_stats)
btc.plot()

print("************************DOGE STATS************************")
kelt_trigger = 3
doge = Backtest(get_doge(), TradingBot, cash=100000)
doge_stats = doge.run()
print(doge_stats)
doge.plot()

print("************************ETH STATS************************")
kelt_trigger = 8
eth = Backtest(get_eth(), TradingBot, cash=100000)
eth_stats = eth.run()
print(eth_stats)
eth.plot()


#### optimize:

# ada_stats = ada.optimize(
#   kelt_trigger=range(0,15,1)
# )
# bnb_stats = bnb.optimize(
#   kelt_trigger=range(0,15,1)
# )
# btc_stats = btc.optimize(
#   kelt_trigger=range(0,15,1)
# )
# doge_stats = doge.optimize(
#   kelt_trigger=range(0,15,1)
# )
# eth_stats = eth.optimize(
#   kelt_trigger=range(0,15,1)
# )

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
