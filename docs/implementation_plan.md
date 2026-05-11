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

Move portfolio definitions into backend config (`portfolio_config.json`).

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
    },
    {
      "bucket_id": "dividend_low_vol",
      "weight": 0.15,
      "symbols": ["VIG", "SCHD", "USMV"]
    },
    {
      "bucket_id": "real_estate",
      "weight": 0.15,
      "symbols": ["VNQ", "SCHH"]
    },
    {
      "bucket_id": "gold",
      "weight": 0.10,
      "symbols": ["GLD", "IAU"]
    },
    {
      "bucket_id": "cash_cash_like",
      "weight": 0.15,
      "symbols": ["BIL", "SHV", "SGOV"]
    }
  ]
}
---

## Step 3: Build recommendation API

Create API endpoint:

```text
POST /recommendation
Input:
{
  "risk_level": "medium"
}