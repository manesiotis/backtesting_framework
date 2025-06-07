# run_backtest.py

from data_loader import load_price_data
from backtester import Backtester
from strategies.moving_average import moving_average_crossover_strategy
from metrics import (
    calculate_cumulative_return,
    calculate_annualized_return,
    calculate_annualized_volatility,
    calculate_sharpe_ratio,
    calculate_max_drawdown
)
from plotting import plot_equity_curve

# === 1. Load historical price data ===
ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2024-12-31'

data = load_price_data(ticker, start=start_date, end=end_date)
prices = data[ticker]

# === 2. Generate trading signals using strategy ===
signals = moving_average_crossover_strategy(prices, short_window=50, long_window=200)

# === 3. Run the backtest ===
bt = Backtester(prices, signals)
results = bt.run_backtest()

# === 4. Calculate performance metrics ===
equity = results['Equity Curve']
strategy_returns = results['Strategy Return']

print(f"Cumulative Return: {calculate_cumulative_return(equity):.2%}")
print(f"Annualized Return: {calculate_annualized_return(equity):.2%}")
print(f"Volatility: {calculate_annualized_volatility(strategy_returns):.2%}")
print(f"Sharpe Ratio: {calculate_sharpe_ratio(strategy_returns):.2f}")
print(f"Max Drawdown: {calculate_max_drawdown(equity):.2%}")

# === 5. Plot and save equity curve ===
plot_equity_curve(
    equity,
    title=f"{ticker} MA Strategy",
    save_path=f"plots/{ticker.lower()}_ma_equity.png"
)
