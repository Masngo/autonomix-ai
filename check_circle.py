import os
import requests
from dotenv import load_dotenv

load_dotenv()

CIRCLE_API_KEY = os.getenv("CIRCLE_API_KEY")

if not CIRCLE_API_KEY:
    print("Error: CIRCLE_API_KEY is missing from environment variables or .env file.")
    exit(1)

headers = {
    "Authorization": f"Bearer {CIRCLE_API_KEY}",
    "Content-Type": "application/json",
    "accept": "application/json"
}

print("Checking Circle Developer-Controlled Wallets...")
wallets_resp = requests.get("https://api.circle.com/v1/w3s/wallets", headers=headers)
print("Wallets Response:\n", wallets_resp.json())

print("\nFetching Latest Transactions...")
tx_resp = requests.get("https://api.circle.com/v1/w3s/transactions?pageSize=1&order=DESC", headers=headers)
print("Transactions Response:\n", tx_resp.json())
