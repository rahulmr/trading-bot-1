from backtesting import Backtest, Strategy
import pandas as pd
import pandas_ta as ta
import numpy as np
import json

COIN = 'BTC'

file = open(f'./data/{COIN}USDT.json')

asset_data = json.load(file)

df = pd.DataFrame(asset_data, columns=[
                  'timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6'])

df = df.drop(columns=['x1', 'x2', 'x3', 'x4', 'x5', 'x6'])

df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

df = df.set_index('timestamp')

df = df.astype(float)

df_t = df
df_t.ta.ema(length=80, append=True)
df_t['slope'] = np.degrees(np.arctan(df_t['EMA_80'].diff()/20))
# print(df_t.to_string())

# buy and sell logic


# acima da keltner superior por ao menos 3 candles
#
# VENDA:
# Kelner caindo
# preco abaixo das keltners
# rsi acima de 80
#
#

def keltner(data):
    keltner = ta.kc(high=data.High.s, low=data.Low.s,
                    close=data.Close.s, length=21, scalar=0.38)
    return keltner.to_numpy().T[:3]

def rsi(data):
    rsi = ta.rsi(close=data.Close.s, length=2)
    return rsi.to_numpy()

class TradingBot(Strategy):

    def init(self):
        self.keltner = self.I(keltner, self.data)
        self.rsi = self.I(rsi, self.data)

    def next(self):
        lower_band = self.keltner[0]
        upper_band = self.keltner[2]
        price = self.data.Close

        
        # opens a long position
        if self.rsi < 30:
            if not self.position:
                self.buy()
            else:
                self.close()
                self.buy()

        # opens a short positon
        if self.rsi > 70:
            if not self.position:
                self.sell()
            else:
                self.close()
                self.sell()

# running strategy
bt = Backtest(df, TradingBot, cash=10_000)
stats = bt.run()
print(stats)
bt.plot()