# strategies/moving_average.py

import pandas as pd

def moving_average_crossover_strategy(prices: pd.Series, short_window=50, long_window=200):
    # Calculate the short-term moving average
    short_ma = prices.rolling(window=short_window).mean()

    # Calculate the long-term moving average
    long_ma = prices.rolling(window=long_window).mean()

    # Create a Series of 0s (default: no position)
    signal = pd.Series(0, index=prices.index)

    # Set signal to 1 (long) when short MA is above long MA
    signal[short_ma > long_ma] = 1

    # Return the signal series
    return signal
