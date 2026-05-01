# Design Decisions

## 1. Cache-First Architecture

### Decision
Use a cache-first approach instead of computing analytics on every API request.

### Reason
- Computing from ETF price data is expensive and slow
- Portfolio analytics involve multiple steps (returns, volatility, drawdown)
- Recomputing for every user request would not scale

### Outcome
- Fast API responses
- Predictable performance
- Reduced dependency on external data sources

---

## 2. Bucket-Level Aggregation

### Decision
Compute returns at the bucket level instead of directly at ETF level during runtime.

### Reason
- Each bucket contains multiple ETFs
- ETFs inside a bucket are equally weighted
- Precomputing bucket return series simplifies runtime logic

### Outcome
- Reduced computation at runtime
- Cleaner separation of logic
- Faster recomputation when weights change

---

## 3. Separation of Batch vs Runtime

### Decision
Split system into:
- Batch layer (data pipeline)
- Runtime layer (API)

### Reason
- Market data fetching should not happen during API calls
- Heavy computations should be precomputed
- APIs should only read or lightly recompute

### Outcome
- Stable and fast APIs
- Easier debugging
- Clear system boundaries

---

## 4. No Real-Time Market Data in MVP

### Decision
Avoid live market data fetching during user requests.

### Reason
- External APIs are unreliable and slow
- Adds latency and failure points
- Not required for MVP

### Outcome
- System remains deterministic
- Easier to test and demo
- Lower operational complexity

---

## 5. Equal Weighting Within Buckets

### Decision
All ETFs inside a bucket are equally weighted.

### Reason
- Simplifies calculations
- Avoids complex weight management
- Good enough for MVP accuracy

### Outcome
- Clean bucket return computation
- Less configuration overhead

---

## 6. Precomputed Analytics Cache

### Decision
Store precomputed portfolio analytics in JSON cache.

### Reason
- Avoid recomputing full history repeatedly
- Faster initial API responses
- Enables UI to load instantly

### Outcome
- Improved user experience
- Reduced compute cost

---

## 7. Lightweight Runtime Recompute

### Decision
Allow recomputation only at bucket level when user adjusts weights.

### Reason
- Full recomputation from ETF level is expensive
- Bucket-level recompute is fast enough

### Outcome
- Real-time feel without heavy computation
- Efficient scaling

---

## 8. Rule-Based Recommendation System

### Decision
Map risk level directly to portfolio_id.

### Reason
- No training data available
- ML is unnecessary for MVP
- Simple mapping is sufficient

### Outcome
- Predictable behavior
- Easy to maintain and extend

---

## 9. Historical Analytics Only

### Decision
System only shows historical performance (no predictions).

### Reason
- Avoid misleading users
- Forecasting requires complex modeling
- Out of MVP scope

### Outcome
- Clear and honest analytics
- Reduced system complexity