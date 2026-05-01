# Task Definition – Portfolio Recommendation System

## Goal
Build a backend system that recommends a portfolio based on user risk level and computes historical analytics for that portfolio.

---

## Portfolio Types

### 1. Balanced Family Office

| Bucket | Weight | ETFs |
|--------|--------|------|
| Broad Market Equities | 45% | VTI, SPY, IVV |
| Dividend / Low Vol Equities | 15% | VIG, SCHD, USMV |
| Real Estate (REITs) | 15% | VNQ, SCHH |
| Gold / Commodities | 10% | GLD, IAU |
| Cash / Cash-like | 15% | BIL, SHV, SGOV |

---

### 2. Growth + Alternatives

| Bucket | Weight | ETFs |
|--------|--------|------|
| Growth Equities | 50% | QQQ, VUG, SCHG |
| Broad Market Equities | 20% | VTI, SPY |
| Alternatives (Public Proxies) | 15% | VNQ, IGF, PAVE |
| Gold / Commodities | 5% | GLD, IAU |
| Cash / Cash-like | 10% | BIL, SGOV |

---

### 3. Real Asset Preservation

| Bucket | Weight | ETFs |
|--------|--------|------|
| Real Estate (REITs) | 35% | VNQ, SCHH |
| Gold / Commodities | 25% | GLD, IAU |
| Broad Market Equities | 20% | VTI, SPY |
| Infrastructure / Real Economy | 10% | IGF, PAVE |
| Cash / Cash-like | 10% | BIL, SHV, SGOV |

---

## Key Assumptions

- Each bucket contains multiple ETFs
- ETFs inside a bucket are equally weighted
- Bucket weights define overall portfolio allocation
- Historical lookback period is 3 years
- Adjusted close prices are used for return calculations

---

## System Responsibilities

### 1. Recommendation Layer
- Input: user risk level (low / medium / high)
- Output: portfolio_id
- Mapping is rule-based (no ML in MVP)

---

### 2. Data Pipeline
- Fetch ETF historical data
- Compute:
  - ETF returns
  - Bucket returns
  - Portfolio returns
- Store results in cache (JSON)

---

### 3. Analytics Engine
- Computes:
  - Portfolio return
  - Volatility
  - Max drawdown
  - Inflation-adjusted return (optional)

---

### 4. API Layer

#### POST /recommendation
- Input: risk_level
- Output: portfolio recommendation

#### GET /portfolio/{id}
- Returns:
  - portfolio structure
  - bucket details
  - ETF list
  - cached analytics

#### POST /portfolio-analytics
- Input:
  - portfolio_id
  - optional updated weights
- Output:
  - recalculated analytics

---

## Constraints (MVP Scope)

- No real-time market data fetching
- No future return predictions
- No user-added symbols
- No trading functionality
- All analytics are based on historical data

---

## Expected Outcome

- Fast API response using cached data
- Simple recomputation when user adjusts weights
- Clear separation between:
  - data pipeline (batch)
  - API layer (runtime)