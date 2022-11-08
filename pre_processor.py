import pandas as pd
import numpy as np
import json

def process_data(data):

    df = pd.DataFrame(data, columns=['timestamp', 'Open', 'High', 'Low', 'Close', 'Volume', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6'])
    df = df.drop(columns=['x1', 'x2', 'x3', 'x4', 'x5', 'x6'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df = df.set_index('timestamp')
    df = df.astype(float) 

    return df

###################### 
# ADAUSDT

def get_ada():
    ada_file = open(f'./data/ADAUSDT.json')
    ada = process_data(json.load(ada_file))
    return ada

def get_ada_test():
    ada_file = open(f'./data/TEST_ADAUSDT.json')
    ada = process_data(json.load(ada_file))
    return ada

###################### 
# BNBUSDT

def get_bnb():
    bnb_file = open(f'./data/BNBUSDT.json')
    bnb = process_data(json.load(bnb_file))
    return bnb

def get_bnb_test():
    bnb_file = open(f'./data/TEST_BNBUSDT.json')
    bnb = process_data(json.load(bnb_file))
    return bnb

###################### 
# BTCUSDT

def get_btc():
    btc_file = open(f'./data/BTCUSDT.json')
    btc = process_data(json.load(btc_file))
    return btc

def get_btc_test():
    btc_file = open(f'./data/TEST_BTCUSDT.json')
    btc = process_data(json.load(btc_file))
    return btc

###################### 
# SOLUSDT

def get_sol():
    sol_file = open(f'./data/SOLUSDT.json')
    sol = process_data(json.load(sol_file))
    return sol

def get_sol_test():
    sol_file = open(f'./data/TEST_SOLUSDT.json')
    sol = process_data(json.load(sol_file))
    return sol

###################### 
# ETHUSDT

def get_eth():
    eth_file = open(f'./data/ETHUSDT.json')
    eth = process_data(json.load(eth_file))
    return eth

def get_eth_test():
    eth_file = open(f'./data/TEST_ETHUSDT.json')
    eth = process_data(json.load(eth_file))
    return eth