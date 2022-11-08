import pandas as pd
import numpy as np
import pandas_ta as ta
from pre_processor import *
from trading_bot import go


trades = go(get_ada_test().iloc[59:])
trades = np.savetxt("labels.txt",trades,fmt='%s')