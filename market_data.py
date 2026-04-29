import yfinance as yf

def fetch_etf_data(symbol):
    data = yf.download(symbol, period="1y")
    return data

def calculate_returns(df):
    df["Return"] = df["Close"].pct_change()
    return df

def get_latest_return(symbol):
    df = fetch_etf_data(symbol)
    df = calculate_returns(df)
    return df["Return"].iloc[-1]