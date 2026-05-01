# AaronBux Portfolio Backend

## Overview
Backend system for portfolio recommendation using a cache-first architecture.

## How it works
1. Data pipeline fetches ETF data and computes returns  
2. Bucket-level returns are calculated across multiple ETFs  
3. Portfolio-level returns are computed using weights  
4. Results are stored in a cached JSON file  
5. API reads from cache and returns recommendation  

## Key files
- data_pipeline.py → computes analytics  
- portfolio_analytics.json → cached data  
- main.py → FastAPI API  
- portfolio_config.json → portfolio definitions  

## Run locally

Run pipeline:
python data_pipeline.py

Run API:
uvicorn main:app --reload

Open Swagger:
http://127.0.0.1:8000/docs

## Next steps
- Move cache to S3  
- Add scheduled job  
- Deploy on AWS  