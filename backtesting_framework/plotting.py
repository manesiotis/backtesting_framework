# plotting.py

import matplotlib.pyplot as plt
import os

def plot_equity_curve(equity_curve, title="Equity Curve", save_path="plots/equity_curve.png"):
    """
    Plots and saves the equity curve (portfolio value over time).

    Parameters:
    - equity_curve: Series with the portfolio value over time
    - title: Title of the plot
    - save_path: Path to save the plot as PNG file
    """
    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    # Create the plot
    plt.figure(figsize=(10, 5))
    plt.plot(equity_curve, label='Equity Curve')
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save the plot to the specified path
    plt.savefig(save_path)
    plt.close()
