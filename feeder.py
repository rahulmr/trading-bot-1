####### todo:
#
# fazer metodo chamar o run em packs de 2h, a cada 2 candles de 15 min (novo pack a cada 2 horas)
# pegar o resultado das 2h após o pack e os parametros de medias de 8 e 80 dos graficos de 2h
# se for positivo, manda o feedback disso p AI
# se for negativo manda o feedback negativo
# e alimenta com 2h, OHLCV
#   FEATURE: EMA 8, EMA 80, SLOPE 8, SLOPE 80, DELTA 8 E 80, OHLCV
# import sys; sys.exit()

import pandas as pd
import numpy as np
import pandas_ta as ta
from assets import *

eth = get_eth()
eth.ta.ema(length = 8, append = True)
eth.ta.ema(length = 80, append = True)
eth.ta.ema_slope(length = 8, append = True)
eth.ta.ema_slope(length = 80, append = True)
eth.drop(eth.index[0:80], inplace=True)

# for row in range(81, len(eth)+80):
#   eth.loc[row,'EMA_SLOPE'] = eth.loc[row,'EMA_80'] - eth.loc[row-1,'EMA_80']

print(eth)
import sys; sys.exit()


# def runStrategy(asset):
#     for row in asset:
        
        

# def callTest(batch):
