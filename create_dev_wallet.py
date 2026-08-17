import os
import uuid
import requests
from dotenv import load_dotenv

load_dotenv()

CIRCLE_API_KEY = os.getenv("CIRCLE_API_KEY")

headers = {
    "Authorization": f"Bearer {CIRCLE_API_KEY}",
    "Content-Type": "application/json",
    "accept": "application/json"
}

# 1. Create a Wallet Set
ws_payload = {
    "idempotencyKey": str(uuid.uuid4()),
    "name": "Autonomix Wallet Set"
}

print("Creating Wallet Set...")
ws_res = requests.post("https://api.circle.com/v1/w3s/developer/walletSets", json=ws_payload, headers=headers)
ws_data = ws_res.json()

if "data" in ws_data and "walletSet" in ws_data["data"]:
    wallet_set_id = ws_data["data"]["walletSet"]["id"]
    print(f"✅ Created Wallet Set ID: {wallet_set_id}")

    # 2. Create Developer-Controlled Wallet in Set
    w_payload = {
        "idempotencyKey": str(uuid.uuid4()),
        "blockchains": ["ETH-SEPOLIA"],
        "count": 1,
        "walletSetId": wallet_set_id
    }

    print("Creating Wallet...")
    w_res = requests.post("https://api.circle.com/v1/w3s/developer/wallets", json=w_payload, headers=headers)
    w_data = w_res.json()
    
    print("\nWallet Creation Response:")
    print(w_data)
else:
    print("❌ Failed to create wallet set:")
    print(ws_data)
