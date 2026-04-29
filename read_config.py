import json

def get_portfolio(portfolio_id):
    with open("portfolio_config.json", "r") as file:
        data = json.load(file)

    for portfolio in data["portfolios"]:
        if portfolio["portfolio_id"] == portfolio_id:
            return portfolio

    return {"error": "Portfolio not found"}


# simulate API call
result = get_portfolio("balanced_family_office_v1")

print("\nAPI Response:")
print(result)