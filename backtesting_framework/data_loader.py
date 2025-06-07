# data_loader.py

import yfinance as yf
import pandas as pd

def load_price_data(ticker, start, end):
    data = yf.download(ticker, start=start, end=end, auto_adjust=False)
    prices = data['Adj Close']
    return pd.DataFrame(prices).rename(columns={'Adj Close': ticker})

