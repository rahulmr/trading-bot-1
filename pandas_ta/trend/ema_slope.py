# -*- coding: utf-8 -*-
import numpy as np
from pandas_ta.overlap import ema
from pandas_ta.utils import get_offset, verify_series


def ema_slope(close, length=None, **kwargs):
    """Indicator: Detrend Price Oscillator (DPO)"""
    # Validate Arguments
    length = int(length) if length and length > 0 else 20
    close = verify_series(close, length)

    if close is None: return

    # Calculate Result
    ma = ema(close, length)

    ema_slope = np.degrees(np.arctan(ma.diff()/20))

    ema_slope.name = f"EMA_SLOPE_{length}"
    ema_slope.category = "trend"

    return ema_slope

