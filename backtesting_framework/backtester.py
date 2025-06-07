# backtester.py

import pandas as pd

class Backtester:
    def __init__(self, prices: pd.Series, signals: pd.Series, initial_cash: float = 10000):
        """
        Initialize the backtester with price data and signals.

        Parameters:
        - prices: Series of adjusted close prices (index = dates)
        - signals: Series of trading signals (1 = long, 0 = cash)
        - initial_cash: Starting portfolio value
        """
        self.prices = prices
        self.signals = signals
        self.initial_cash = initial_cash
        self.results = None

    def run_backtest(self):
        """
        Run the backtest and compute daily portfolio value.

        Returns:
        - DataFrame with price, signals, returns, strategy returns, equity curve
        """
        # Daily percentage return of the asset
        returns = self.prices.pct_change().fillna(0)

        # Strategy return: apply signal (position) to the return
        strategy_returns = self.signals.shift(1).fillna(0) * returns

        # Cumulative portfolio value (equity curve)
        equity_curve = (1 + strategy_returns).cumprod() * self.initial_cash

        # Store results in a DataFrame
        self.results = pd.DataFrame({
            'Price': self.prices,
            'Signal': self.signals,
            'Return': returns,
            'Strategy Return': strategy_returns,
            'Equity Curve': equity_curve
        })

        return self.results
