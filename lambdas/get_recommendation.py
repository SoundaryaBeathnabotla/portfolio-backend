import json
import boto3

s3 = boto3.client("s3")

BUCKET_NAME = "aaronbux-portfolio-backend-dev"

PORTFOLIO_CONFIG_KEY = "config/portfolio_config.json"
PORTFOLIO_ANALYTICS_KEY = "portfolio_analytics/portfolio_analytics.json"


def load_portfolio_config():

    response = s3.get_object(
        Bucket=BUCKET_NAME,
        Key=PORTFOLIO_CONFIG_KEY
    )

    data = json.loads(
        response["Body"].read().decode("utf-8")
    )

    return data


def load_portfolio_analytics():

    response = s3.get_object(
        Bucket=BUCKET_NAME,
        Key=PORTFOLIO_ANALYTICS_KEY
    )

    data = json.loads(
        response["Body"].read().decode("utf-8")
    )

    return data


def lambda_handler(event, context):

    body = json.loads(event["body"])

    risk_level = body["risk_level"]

    portfolio_config = load_portfolio_config()

    portfolio_analytics = load_portfolio_analytics()

    risk_mapping = {
        "low": "income_stability_v1",
        "medium": "balanced_family_office_v1",
        "high": "growth_accelerated_v1"
    }

    portfolio_id = risk_mapping.get(risk_level)

    selected_portfolio = None

    for portfolio in portfolio_config["portfolios"]:

        if portfolio["portfolio_id"] == portfolio_id:
            selected_portfolio = portfolio
            break

    if not selected_portfolio:

        return {
            "statusCode": 404,
            "body": json.dumps({
                "error": "Portfolio not found"
            })
        }

    analytics = portfolio_analytics.get(
        portfolio_id,
        {}
    )

    response = {
        "recommended_portfolio": selected_portfolio,
        "analytics": analytics
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }


if __name__ == "__main__":

    test_event = {
        "body": json.dumps({
            "risk_level": "medium"
        })
    }

    result = lambda_handler(
        test_event,
        None
    )

    print(json.dumps(result, indent=2))