from backtesting import Backtest, Strategy
from pre_processor import *
import pandas as pd
import pandas_ta as ta
import numpy as np

# COMPRA:
# preciso acima das keltners
# rsi abaixo de 20
# distancia das bandas > que x
# 
# VENDA:
# preco abaixo das keltners
# rsi acima de 80
# distancia das bandas > que x
#
# conda activate mlp => deactivate

kelt_trigger = 0
trades = []

CRYPTO = 'sol'

if CRYPTO == 'ada':
    kelt_trigger = 21
elif CRYPTO == 'bnb':
    kelt_trigger = 45
elif CRYPTO == 'btc':
    kelt_trigger = 35
elif CRYPTO == 'eth':
    kelt_trigger = 39
elif CRYPTO == 'sol':
    kelt_trigger = 46

labels = np.loadtxt('cryptos/'+CRYPTO+'/test_lbl_bot.txt',dtype ='int32')

def keltner(data):
    keltner = ta.kc(high=data.High.s, low=data.Low.s,
                    close=data.Close.s, length=21, scalar=0.38)
    return keltner.to_numpy().T[:3]

def rsi(data):
    rsi = ta.rsi(close=data.Close.s, length=2)
    return rsi.to_numpy()

class TradingBot(Strategy):

    low_rsi = 20
    high_rsi = 80
    count = 0
    label_index = 0
    trade = True

    print(kelt_trigger)
    def init(self):
        self.keltner = self.I(keltner, self.data)
        self.rsi = self.I(rsi, self.data)

    def next(self):
        self.count += 1

        if self.count == 8:
            if labels[self.label_index] == 1:
                self.trade = True
            else:
                self.trade = False

            self.label_index += 1
            if(self.label_index == len(labels)): self.label_index -= 1
            self.count -= 2

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

        if not self.position and self.trade:
        # if not self.position:
            if len(self.closed_trades) > 0:
                trades.append(self.closed_trades)

            # opens a long position
            if kelter_width > kelt_trigger/100 and self.rsi[-1] < self.low_rsi and self.data.Open > self.data.Close and self.data.Close > upper_band:
                take = price + (price - previous_bottom)*2
                if(take != previous_bottom):
                    self.buy(tp=take, sl=previous_bottom)

            # opens a short positon
            if kelter_width > kelt_trigger/100 and self.rsi[-1] > self.high_rsi and self.data.Open < self.data.Close and self.data.Close < lower_band:
                take = price - (previous_top - price)*2
                if(take != previous_top):
                    self.sell(tp=take, sl=previous_top)

def go(data):
    test = Backtest(data,TradingBot, cash=100000)
    stats = test.run()
    print(stats)
    return stats[29]


# import sys; sys.exit()

# running strategy
# print("************************ADA STATS************************")
# kelt_trigger = 21
# df = get_ada_test().iloc[59:]
# ada = Backtest(df, TradingBot, cash=100000)
# ada_stats = ada.run()
# print(ada_stats)
# # ada.plot()

# print("************************BNB STATS************************")
# kelt_trigger = 45
# df = get_bnb_test().iloc[59:]
# bnb = Backtest(df, TradingBot, cash=100000)
# bnb_stats = bnb.run()
# print(bnb_stats)
# # bnb.plot()

# print("************************BTC STATS************************")
# kelt_trigger = 35
# df = get_btc_test().iloc[59:]
# btc = Backtest(df, TradingBot, cash=100000)
# btc_stats = btc.run()
# print(btc_stats)
# # btc.plot()

# print("************************ETH STATS************************")
# kelt_trigger = 39
# df = get_eth_test().iloc[59:]
# eth = Backtest(df, TradingBot, cash=100000)
# eth_stats = eth.run()
# print(eth_stats)
# # eth.plot()

# print("************************SOL STATS************************")
# kelt_trigger = 46
# df = get_sol_test().iloc[59:]
# sol = Backtest(df, TradingBot, cash=100000)
# sol_stats = sol.run()
# print(sol_stats)
# sol.plot()

#### optimize:

# ada_stats = ada.optimize(
#   kelt_trigger=range(0,55,1)
# )
# bnb_stats = bnb.optimize(
#   kelt_trigger=range(0,55,1)
# )
# btc_stats = btc.optimize(
#   kelt_trigger=range(0,55,1)
# )
# sol_stats = sol.optimize(
#   kelt_trigger=range(0,55,1)
# )
# eth_stats = eth.optimize(
#   kelt_trigger=range(0,55,1)
# )
# ada.plot()
# bnb.plot()
# btc.plot()
# sol.plot()
# eth.plot()

# print(ada_stats)
# print(bnb_stats)
# print(btc_stats)
# print(sol_stats)
# print(eth_stats)

# print("************************FINAL STATS************************")
# result = ada_stats[4] + bnb_stats[4] + btc_stats[4] + sol_stats[4] + eth_stats[4]
# profit = (result/500000 - 1)*100
# result -= 500000
# print("ADA: ", "{:.2f}".format(ada_stats[4]))
# print("BNB: ", "{:.2f}".format(bnb_stats[4]))
# print("BTC: ", "{:.2f}".format(btc_stats[4]))
# print("SOL: ", "{:.2f}".format(sol_stats[4]))
# print("ETH: ", "{:.2f}".format(eth_stats[4]))
# print("Result:", "{:.2f}".format(result))
# print("Profit", "{:.2f}".format(profit), "%")
