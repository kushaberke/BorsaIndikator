import matplotlib.pyplot as plt
import yfinance as yf
from ta.volatility import BollingerBands
from ta.trend import MACD, EMAIndicator, SMAIndicator
from ta.momentum import RSIIndicator
import datetime

stock = "BIMAS.IS"

def download_data(op, start_date, end_date):
    df = yf.download(op, start=start_date, end=end_date, progress=False)
    return df

today = datetime.date.today()
duration = 3000
before = today - datetime.timedelta(days=duration)
start_date = before
end_date = today

data = download_data(stock,start_date,end_date)

def tech_indicators():

    # Bollinger bands
    bb_indicator = BollingerBands(data.Close)
    bb=data
    bb['bb_h'] = bb_indicator.bollinger_hband()
    bb['bb_l'] = bb_indicator.bollinger_lband()
    # Creating a new dataframe
    
    bb = bb[['Close', 'bb_h', 'bb_l']]
    # MACD
    macd = MACD(data.Close).macd()
    # RSI
    rsi = RSIIndicator(data.Close).rsi()
    # SMA
    sma = SMAIndicator(data.Close, window=14).sma_indicator()
    # EMA
    ema = EMAIndicator(data.Close).ema_indicator()

    print(rsi)

    # Assuming 'rsi' is your DataFrame with date index and RSI values
    rsi.plot(figsize=(12, 6), label='RSI')
    plt.title('RSI Over Time')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.grid(True)
    plt.show()

tech_indicators()


