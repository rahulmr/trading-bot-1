# todo:
#  =>>>> os dados precisam começar 20 horas antes pra poder ter as médias
# fazer metodo chamar o run em packs de 2h, a cada 2 candles de 15 min (novo pack a cada 2 horas)
# pegar o resultado das 2h após o pack e os parametros de medias de 8 e 80 dos graficos de 2h
# se for positivo, manda o feedback disso p AI
# se for negativo manda o feedback negativo
# e alimenta com 2h, OHLCV
#   FEATURE: EMA 8, EMA 80, SLOPE 8, SLOPE 80, OHLCV
# import sys; sys.exit()

import sys
import pandas as pd
import numpy as np
import pandas_ta as ta
from pre_processor import *
from trading_bot import go


def getIndicators(data):

    data.ta.ema(length=8, append=True)
    data.ta.ema(length=80, append=True)
    # data.ta.ema_slope(length=8, append=True)
    # data.ta.ema_slope(length=80, append=True)
    # data.drop(data.index[0:80], inplace=True)

    return data

def searchTrade(candle,trades):

    entry = trades[trades['EntryBar'].between(candle,candle+8)]
    exit = trades[trades['ExitBar'].between(candle,candle+8)]

    if exit['ExitBar'].any() and (entry['ReturnPct']<0).any():
        return 0
    else:
        return 1

def buildFeature(asset, trigger):

    trades = go(asset, trigger)
    asset.reset_index(inplace=True,drop=True)
    asset = getIndicators(asset)
    asset.drop('Volume', axis=1, inplace=True)

    features = []
    results = []

    i = 0

    while i < len(asset) - 7:
        features.append(asset.iloc[i:i+8])
        results.append(searchTrade(i, trades))
        i+=2

    del features[:40]
    del results[:40]

    return features, results

# features, labels = buildFeature(get_btc(), 3)

# print(features)
# print(labels)

# sys.exit()
# two, target = buildFeature(get_eth(), 8)
# two = pd.DataFrame(two)

# two.ta.ema(length=8, append=True)
# two.ta.ema(length=80, append=True)
# two.ta.ema_slope(length=8, append=True)
# two.ta.ema_slope(length=80, append=True)
# two.drop(two.index[0:80], inplace=True)

# gain = 0
# loss = 0
# total = 0

# for row in target:
#     total += row
#     if row > 0.0:
#         gain += 1
#     elif row < 0.0:
#         loss += 1
# # print(two)
# print("################################")
# print(gain)
# print(loss)
# print(total)
