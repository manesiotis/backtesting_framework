# 📊 Project 4: Backtesting Framework from Scratch

This project implements a simple backtesting engine for testing trading strategies on historical stock data. It includes tools for signal generation, strategy evaluation, performance metrics, and plotting the equity curve.

---

## 📁 Project Structure

```
backtesting_framework/
│
├── strategies/
│   └── moving_average.py       # Moving Average Crossover Strategy
│
├── backtester.py               # Core backtesting logic
├── data_loader.py              # Loads historical stock prices from Yahoo Finance
├── metrics.py                  # Calculates performance metrics (Sharpe, drawdown, etc.)
├── plotting.py                 # Plots and saves the equity curve
├── run_backtest.py             # Main script to execute backtest
│
├── plots/
│   └── aapl_ma_equity.png      # Output plot for AAPL strategy
│
└── README.md                   # Project description
```

---

## 🚀 How to Run

1. **Install the required libraries** (if you haven't already):

```bash
pip install yfinance pandas matplotlib
```

2. **Run the main script**:

```bash
python run_backtest.py
```

This will:
- Download price data (AAPL)
- Apply the moving average crossover strategy
- Run the backtest
- Output key performance metrics
- Save the equity curve to the `plots/` folder

---

## 📈 Strategy Example: Moving Average Crossover

- **Buy signal**: when the short-term moving average crosses above the long-term one
- **Exit**: when the short-term falls below the long-term

Parameters used:
- Short window: 50 days
- Long window: 200 days

---

## 📊 Output Metrics (example)

```
Cumulative Return:      +102.45%
Annualized Return:      +18.70%
Volatility:             22.10%
Sharpe Ratio:           0.84
Max Drawdown:          -17.90%
```

---

## ✅ Features

- Modular design (plug in different strategies)
- Works with any stock ticker supported by Yahoo Finance
- Easily extendable with new strategies or risk metrics

---

## 📌 Next Steps

- Add more strategies (momentum, mean reversion, etc.)
- Improve risk management (e.g. position sizing, stop-loss)
- Add portfolio backtesting for multiple assets

---

## 👨‍💻 Author

Konstantinos Manesiotis  
Project 4 of Quant Trading Series
