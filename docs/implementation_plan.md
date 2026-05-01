# Implementation Plan

## Goal
Build a backend portfolio recommendation system that takes quiz output, maps the user to a portfolio, and returns cached portfolio analytics.

---

## Step 1: Extract portfolio logic from frontend
Use the existing frontend logic as the source of truth.

Current portfolio types:
- Balanced Family Office
- Growth + Alternatives
- Real Asset Preservation

Each portfolio contains:
- buckets
- bucket weights
- ETF symbols
---

## Step 2: Store portfolio structure in backend
Move portfolio definitions into backend config.

Example:
```json
{
  "portfolio_id": "balanced_family_office_v1",
  "name": "Balanced Family Office",
  "buckets": [
    {
      "bucket_id": "broad_market_equities",
      "weight": 0.45,
      "symbols": ["VTI", "SPY", "IVV"]
    }
  ]
}
---

## Step 3: Build recommendation API
Create API endpoint:

```text
POST /recommendation
```

Input:

```json
{
  "risk_level": "medium"
}
```

Output:

```json
{
  "portfolio_id": "balanced_family_office_v1",
  "portfolio_return": 0.0021,
  "buckets": []
}
---

## Step 4: Build analytics pipeline
The pipeline will:
1. Fetch ETF price data
2. Compute daily ETF returns
3. Compute bucket returns across all ETFs
4. Compute portfolio-level weighted returns
5. Save results into cache
---

## Step 5: Use cache-first architecture

Correct flow:
Scheduled pipeline → cached analytics → API reads cache

Current cache:
portfolio_analytics.json

Future cache:
S3 or DynamoDB

---

## Step 6: Runtime recompute (future)
When users adjust bucket weights, recompute analytics using cached data instead of fetching new market data.

Future endpoint:

POST /portfolio-analytics

Input:
```json
{
  "portfolio_id": "balanced_family_office_v1",
  "weights": {
    "broad_market_equities": 0.50,
    "cash_cash_like": 0.10
  }
}
---

## Step 7: AWS plan
- S3 for cached analytics
- Lambda for scheduled jobs
- EventBridge for scheduling
- API Gateway + Lambda (or FastAPI deployment)

---

## MVP Scope

Included:
- predefined portfolios
- ETF-based analytics
- cached results
- recommendation API

Not included:
- live trading
- forecasting
- user-added symbols
- real-time API calls