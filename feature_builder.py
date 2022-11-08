import pandas as pd
import numpy as np
import pandas_ta as ta
from pre_processor import *
from trading_bot import go

def getIndicators(data):

    data.ta.ema(length=8, append=True)
    data.ta.ema(length=80, append=True)

    return data

def searchTrade(candle,trades):

    entry = trades[trades['EntryBar'].between(candle,candle+8)]
    exit = trades[trades['ExitBar'].between(candle,candle+8)]

    if exit['ExitBar'].any() and (entry['ReturnPct']<0).any():
        return 0
    else:
        return 1

def buildFeature(asset):

    trades = go(asset)
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