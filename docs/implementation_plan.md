## Concrete Example (from frontend logic)

Example Portfolio: Balanced Family Office

Buckets:
- Broad Market Equities – 45% (VTI, SPY, IVV)
- Dividend / Low Vol – 15% (VIG, SCHD, USMV)
- Real Estate – 15% (VNQ, SCHH)
- Gold / Commodities – 10% (GLD, IAU)
- Cash – 15% (BIL, SHV, SGOV)

Backend Representation (JSON):

{
  "portfolio_id": "balanced",
  "buckets": [
    {
      "name": "broad_market_equities",
      "weight": 45,
      "etfs": ["VTI", "SPY", "IVV"]
    },
    {
      "name": "dividend_low_vol",
      "weight": 15,
      "etfs": ["VIG", "SCHD", "USMV"]
    }
  ]
}