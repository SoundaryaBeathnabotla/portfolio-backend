# Architecture Breakdown

## Goal
Build a portfolio recommendation system based on user risk level.

---

## Components

### 1. Quiz (Frontend)
- User answers questions
- Outputs risk level (low / medium / high)

### 2. Backend API (FastAPI)
- Endpoint: POST /recommendation
- Input: risk_level
- Maps to portfolio_id
- Returns portfolio recommendation

### 3. Data Pipeline
- Fetches ETF data using yfinance
- Computes daily returns
- Aggregates into:
  - Bucket-level returns (multiple ETFs)
  - Portfolio-level returns (weighted)

### 4. Cache Layer
- Stores computed analytics
- Current: JSON file
- Future: S3

---

## Data Flow

Quiz → API → Cached Analytics → Response

---

## Key Design Decision

Cache-first architecture:
- No real-time market calls inside API
- Faster and more stable responses

---

## Future Improvements

- Move cache to S3
- Add scheduled job (daily updates)
- Deploy API to AWS