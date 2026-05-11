import json
import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Your bucket + file path
BUCKET_NAME = "aaronbux-portfolio-backend-dev"
FILE_KEY = "config/portfolio_config.json"


def get_portfolio(portfolio_id):
    try:
        # Fetch file from S3
        response = s3.get_object(Bucket=BUCKET_NAME, Key=FILE_KEY)

        # Read and parse JSON
        data = json.loads(response['Body'].read().decode('utf-8'))

        # Find portfolio
        for portfolio in data["portfolios"]:
            if portfolio["portfolio_id"] == portfolio_id:
                return portfolio

        return {"error": "Portfolio not found"}

    except Exception as e:
        return {"error": str(e)}


# 🔹 Test (simulate API call)
if __name__ == "__main__":
    result = get_portfolio("balanced_family_office_v1")
    print("\nAPI Response:")
    print(json.dumps(result, indent=2))