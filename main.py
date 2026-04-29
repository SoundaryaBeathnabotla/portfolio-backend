from fastapi import FastAPI
from pydantic import BaseModel
import json
import pandas as pd

app = FastAPI()


# ----------------------------
# Load portfolio config
# ----------------------------
def load_data():
    with open("portfolio_config.json", "r") as file:
        return json.load(file)


# ----------------------------
# Load cached bucket returns
# ----------------------------
def load_bucket_returns():
    df = pd.read_csv("bucket_returns.csv")
    return df


# ----------------------------
# Input schema
# ----------------------------
class QuizInput(BaseModel):
    risk_level: str


# ----------------------------
# Home endpoint
# ----------------------------
@app.get("/")
def home():
    return {"message": "Portfolio backend is running"}


# ----------------------------
# Get all portfolios
# ----------------------------
@app.get("/portfolios")
def get_all_portfolios():
    data = load_data()
    return data["portfolios"]


# ----------------------------
# Get portfolio by ID
# ----------------------------
@app.get("/portfolio/{portfolio_id}")
def get_portfolio(portfolio_id: str):
    data = load_data()

    for portfolio in data["portfolios"]:
        if portfolio["portfolio_id"] == portfolio_id:
            return portfolio

    return {"error": "Portfolio not found"}


# ----------------------------
# Cached bucket returns API
# ----------------------------
@app.get("/bucket-returns")
def get_bucket_returns():
    df = load_bucket_returns()
    return df.tail(5).to_dict(orient="records")


# ----------------------------
# Recommendation API
# ----------------------------
@app.post("/recommendation")
def get_recommendation(input: QuizInput):
    risk = input.risk_level.lower()

    # Read latest cached bucket return
    df = load_bucket_returns()
    latest_return = df.iloc[-1]["Bucket_Return"]

    if risk == "low":
        return {
            "portfolio_id": "real_asset_preservation_v1",
            "market_return": float(latest_return)
        }

    elif risk == "medium":
        return {
            "portfolio_id": "balanced_family_office_v1",
            "market_return": float(latest_return)
        }

    elif risk == "high":
        return {
            "portfolio_id": "growth_alternatives_v1",
            "market_return": float(latest_return)
        }

    else:
        return {"error": "Invalid risk level"}