import os
import requests
from dotenv import load_dotenv

# Force load environment variables from .env
load_dotenv(override=True)

class TatumService:
    def __init__(self, endpoint="https://base-mainnet.gateway.tatum.io"):
        self.endpoint = endpoint
        self.api_key = os.getenv("TATUM_API_KEY")
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "x-api-key": self.api_key
        }

    def rpc_call(self, method, params=[]):
        payload = {"jsonrpc": "2.0", "method": method, "params": params, "id": 1}
        response = requests.post(self.endpoint, json=payload, headers=self.headers)
        return response.json()

    def get_balance(self, address):
        return self.rpc_call("eth_getBalance", [address, "latest"])

    def get_gas_price(self):
        return self.rpc_call("eth_gasPrice", [])

if __name__ == "__main__":
    tatum = TatumService()
    test_address = "0x4200000000000000000000000000000000000006"
    
    print("Loaded Key Prefix:", str(tatum.api_key)[:6] if tatum.api_key else "None")
    print("Gas Price Response:", tatum.get_gas_price())
    print("Balance Response:", tatum.get_balance(test_address))
