from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()


class RecommendationRequest(BaseModel):
    risk_level: str


def load_portfolio_config():
    with open("portfolio_config.json", "r") as f:
        return json.load(f)


def load_portfolio_analytics():
    with open("portfolio_analytics.json", "r") as f:
        return json.load(f)


@app.get("/")
def home():
    return {
        "message": "AaronBux Portfolio Recommendation API is running"
    }


@app.get("/portfolio-config")
def get_portfolio_config():
    config = load_portfolio_config()
    return config


@app.post("/recommendation")
def get_recommendation(request: RecommendationRequest):
    risk_level = request.risk_level.lower()

    risk_to_portfolio = {
        "low": "conservative_portfolio_v1",
        "medium": "balanced_family_office_v1",
        "high": "aggressive_growth_v1"
    }

    portfolio_id = risk_to_portfolio.get(risk_level)

    if not portfolio_id:
        return {
            "error": "Invalid risk_level. Use low, medium, or high."
        }

    analytics = load_portfolio_analytics()

    portfolio_data = analytics["portfolios"].get(portfolio_id)

    if not portfolio_data:
        return {
            "error": f"Portfolio analytics not found for {portfolio_id}"
        }

    return {
        "risk_level": risk_level,
        "portfolio_id": portfolio_id,
        "as_of_date": analytics["as_of_date"],
        "portfolio_return": portfolio_data["portfolio_return"],
        "buckets": portfolio_data["buckets"]
    }