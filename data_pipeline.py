import yfinance as yf


def fetch_etf_data(symbol):
    data = yf.download(symbol, period="1y")
    return data


def calculate_returns(df):
    df["Return"] = df["Close"].pct_change()
    return df


def calculate_bucket_returns(all_data, bucket_symbols):
    bucket_df = None

    for symbol in bucket_symbols:
        df = all_data[symbol][["Return"]].rename(columns={"Return": symbol})

        if bucket_df is None:
            bucket_df = df
        else:
            bucket_df = bucket_df.join(df, how="inner")

    bucket_df["Bucket_Return"] = bucket_df.mean(axis=1)

    return bucket_df


if __name__ == "__main__":
    symbols = ["VTI", "SPY", "QQQ"]

    all_data = {}

    for symbol in symbols:
        print(f"\nFetching data for {symbol}")

        df = fetch_etf_data(symbol)
        df = calculate_returns(df)

        all_data[symbol] = df

    growth_bucket = ["QQQ", "SPY"]

    bucket_df = calculate_bucket_returns(all_data, growth_bucket)

    print("\nBucket Returns:")
    print(bucket_df.head())

    bucket_df.to_csv("bucket_returns.csv")
    print("Saved bucket_returns.csv")