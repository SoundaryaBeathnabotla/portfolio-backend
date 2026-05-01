# Analytics Logic

## Overview

This system computes historical portfolio analytics using a 3-year lookback period based on ETF price data.

All calculations are based on **adjusted close prices**.

---

## Key Assumptions

- ETFs inside each bucket are equally weighted
- Bucket weights define portfolio allocation
- 3-year historical window is used
- No future projections are made

---

## Step 1: ETF Daily Returns

For each ETF:

Return = (Price_t / Price_(t-1)) - 1

Where:
- Price_t = adjusted close price at time t

---

## Step 2: Bucket Returns

Each bucket contains multiple ETFs.

Bucket return is the **average of ETF returns**:

Bucket Return = (r1 + r2 + ... + rn) / n

Where:
- r = daily return of each ETF

---

## Step 3: Portfolio Returns

Portfolio return is the weighted sum of bucket returns:

Portfolio Return = Σ (bucket_weight × bucket_return)

---

## Step 4: Cumulative Return (3-Year)

Cumulative Return = Π (1 + daily_return) - 1

Where:
- Π = product over all days in 3 years

---

## Step 5: Volatility

Volatility is the annualized standard deviation of daily returns:

Volatility = std(daily_returns) × √252

---

## Step 6: Max Drawdown

1. Compute cumulative value series:
   Value_t = Π (1 + returns)

2. Track running peak:
   Peak_t = max(Value_0 ... Value_t)

3. Drawdown:
   Drawdown_t = (Value_t - Peak_t) / Peak_t

Max Drawdown = minimum of Drawdown_t

---

## Step 7: Inflation-Adjusted Return (Optional)

Real Return = (1 + nominal_return) / (1 + inflation) - 1

Where:
- inflation derived from CPI data

---

## Step 8: $1000 Growth Illustration

Final Value = 1000 × (1 + cumulative_return)

Used for visualization only.

---

## Optimization Strategy

To improve performance:

- Precompute bucket return series
- Cache bucket-level data
- At runtime:
  - recompute portfolio using bucket weights only

This avoids recomputing from ETF prices every time.

---

## Summary Flow

ETF Prices → ETF Returns → Bucket Returns → Portfolio Returns → Metrics