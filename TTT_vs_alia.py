# %%
# import libraries
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import matplotlib.dates as mdates
import pandas as pd
from datetime import date
import matplotx
import math

# %%
# import data
today = date.today()

# semi supply chain
nvidia = yf.download('NVDA', start='2023-01-01', end=today)
intel = yf.download('INTC', start='2023-01-01', end=today)
tsmc = yf.download('TSM', start='2023-01-01', end=today)
asml = yf.download('ASML', start='2023-01-01', end=today)
samsung = yf.download('SMSN.IL', start='2023-01-01', end=today)
# compute / models
amazon = yf.download('AMZN', start='2023-01-01', end=today)
alphabet = yf.download('GOOG', start='2023-01-01', end=today)
microsoft = yf.download('MSFT', start='2023-01-01', end=today)
alibaba = yf.download('BABA', start='2023-01-01', end=today)
baidu = yf.download('BIDU', start='2023-01-01', end=today)
tencent = yf.download('TCEHY', start='2023-01-01', end=today)
# short rates
ttt = yf.download('TTT', start='2023-01-01', end=today)

# %%
# normalise prices
assets = [nvidia, intel, tsmc, asml, samsung, amazon, alphabet, microsoft, alibaba, baidu, tencent, ttt]
asset_tickers = ["NVDA", "INTC", "TSM", "ASML", "SMSN.IL", "AMZN", "GOOG", "MSFT", "BABA", "BIDU", "TCEHY", "TTT"]

for asset in assets:
    asset["Normalised"] = asset["Adj Close"] / asset.iloc[0]["Adj Close"] * 100
                
# %%
# making plots
custom_style = {"axes.spines.right": False, "axes.spines.top": False, "axes.xmargin": 0,}

with plt.style.context(custom_style):
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(16, 9))
        ax.spines["right"].set_visible(False)
        for asset, ticker in zip(assets, asset_tickers):
                ax.plot(asset["Normalised"], label=ticker)
                matplotx.line_labels()

        plt.xlim([date(2023, 1, 1), today])
        plt.figtext(0.9, 0.02, 'Made by @tmychow', ha='right', va='bottom', fontsize=12, color='blue')
        plt.title("Trading on AGI (Indexed to 100 on 2023-01-01)")
        plt.xlabel("Date")
        plt.ylabel("Normalised Price")
        plt.show()

# %%
