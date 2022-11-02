import pandas as pd
import numpy as np
import json

###################### 
# ADAUSDT

ada_file = open(f'./data/ADAUSDT.json')
ada_data = json.load(ada_file)

ada = pd.DataFrame(ada_data, columns=['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6'])
ada = ada.drop(columns=['x1', 'x2', 'x3', 'x4', 'x5', 'x6'])
ada['timestamp'] = pd.to_datetime(ada['timestamp'], unit='ms')
ada = ada.set_index('timestamp')
ada = ada.astype(float)

def get_ada():
    return ada

###################### 
# BNBUSDT

bnb_file = open(f'./data/BNBUSDT.json')
bnb_data = json.load(bnb_file)

bnb = pd.DataFrame(bnb_data, columns=['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6'])
bnb = bnb.drop(columns=['x1', 'x2', 'x3', 'x4', 'x5', 'x6'])
bnb['timestamp'] = pd.to_datetime(bnb['timestamp'], unit='ms')
bnb = bnb.set_index('timestamp')
bnb = bnb.astype(float)

def get_bnb():
    return bnb

###################### 
# BTCUSDT

btc_file = open(f'./data/BTCUSDT.json')
btc_data = json.load(btc_file)

btc = pd.DataFrame(btc_data, columns=['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6'])
btc = btc.drop(columns=['x1', 'x2', 'x3', 'x4', 'x5', 'x6'])
btc['timestamp'] = pd.to_datetime(btc['timestamp'], unit='ms')
btc = btc.set_index('timestamp')
btc = btc.astype(float)

def get_btc():
    return btc

###################### 
# DOGEUSDT

doge_file = open(f'./data/DOGEUSDT.json')
doge_data = json.load(doge_file)

doge = pd.DataFrame(doge_data, columns=['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6'])
doge = doge.drop(columns=['x1', 'x2', 'x3', 'x4', 'x5', 'x6'])
doge['timestamp'] = pd.to_datetime(doge['timestamp'], unit='ms')
doge = doge.set_index('timestamp')
doge = doge.astype(float)

def get_doge():
    return doge

###################### 
# ETHUSDT

eth_file = open(f'./data/ETHUSDT.json')
eth_data = json.load(eth_file)

eth = pd.DataFrame(eth_data, columns=['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6'])
eth = eth.drop(columns=['x1', 'x2', 'x3', 'x4', 'x5', 'x6'])
eth['timestamp'] = pd.to_datetime(eth['timestamp'], unit='ms')
eth = eth.set_index('timestamp')
eth = eth.astype(float)

def get_eth():
    return eth