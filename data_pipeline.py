import yfinance as yf
import pandas as pd
import json


def load_config():
    with open("portfolio_config.json", "r") as f:
        return json.load(f)


def fetch_returns(symbol):
    df = yf.download(symbol, period="1y", auto_adjust=False)

    if df.empty:
        raise ValueError(f"No data found for symbol: {symbol}")

    df["Return"] = df["Close"].pct_change()
    return df[["Return"]]


def compute_bucket_returns():
    config = load_config()
    all_bucket_data = {}

    for portfolio in config["portfolios"]:
        for bucket in portfolio["buckets"]:
            bucket_name = bucket["bucket_id"]
            symbols = bucket["symbols"]

            print(f"\nProcessing bucket: {bucket_name}")
            print(f"Symbols: {symbols}")

            combined_df = pd.DataFrame()

            for symbol in symbols:
                print(f"Fetching {symbol}...")

                df = fetch_returns(symbol)
                df = df.rename(columns={"Return": symbol})

                if combined_df.empty:
                    combined_df = df
                else:
                    combined_df = combined_df.join(df, how="outer")

            combined_df["Bucket_Return"] = combined_df[symbols].mean(axis=1)

            all_bucket_data[bucket_name] = combined_df

            filename = f"{bucket_name}_returns.csv"
            combined_df.to_csv(filename)

            latest_return = combined_df["Bucket_Return"].dropna().iloc[-1]

            print(f"Saved {filename}")
            print(f"Latest Bucket_Return for {bucket_name}: {latest_return}")

    return all_bucket_data


def compute_portfolio_analytics(all_bucket_data):
    config = load_config()

    result = {
        "as_of_date": pd.Timestamp.today().strftime("%Y-%m-%d"),
        "portfolios": {}
    }

    for portfolio in config["portfolios"]:
        portfolio_id = portfolio["portfolio_id"]

        portfolio_return = 0
        bucket_results = []

        for bucket in portfolio["buckets"]:
            bucket_name = bucket["bucket_id"]
            weight = bucket["target_weight"]

            df = all_bucket_data[bucket_name]

            latest_bucket_return = df["Bucket_Return"].dropna().iloc[-1]

            portfolio_return += latest_bucket_return * weight

            bucket_results.append({
                "bucket_id": bucket_name,
                "weight": weight,
                "bucket_return": float(latest_bucket_return)
            })

        result["portfolios"][portfolio_id] = {
            "portfolio_return": float(portfolio_return),
            "buckets": bucket_results
        }

    with open("portfolio_analytics.json", "w") as f:
        json.dump(result, f, indent=2)

    print("\nSaved portfolio_analytics.json")


if __name__ == "__main__":
    all_bucket_data = compute_bucket_returns()
    compute_portfolio_analytics(all_bucket_data)