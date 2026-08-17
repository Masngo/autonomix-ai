import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

app = FastAPI(title="Autonomix AI - Tatum Gateway")

class TatumService:
    def __init__(self, endpoint="https://base-mainnet.gateway.tatum.io"):
        self.endpoint = endpoint
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "x-api-key": os.getenv("TATUM_API_KEY")
        }

    def rpc_call(self, method, params=[]):
        payload = {"jsonrpc": "2.0", "method": method, "params": params, "id": 1}
        response = requests.post(self.endpoint, json=payload, headers=self.headers)
        return response.json()

tatum = TatumService()

@app.get("/")
def health_check():
    return {"status": "online", "network": "Base Mainnet"}

@app.get("/gas-price")
def get_gas_price():
    data = tatum.rpc_call("eth_gasPrice")
    if "result" in data:
        wei_value = int(data["result"], 16)
        return {"hex": data["result"], "wei": wei_value, "gwei": wei_value / 1e9}
    raise HTTPException(status_code=500, detail=data)

@app.get("/balance/{address}")
def get_balance(address: str):
    data = tatum.rpc_call("eth_getBalance", [address, "latest"])
    if "result" in data:
        wei_value = int(data["result"], 16)
        return {"address": address, "hex": data["result"], "wei": wei_value, "eth": wei_value / 1e18}
    raise HTTPException(status_code=500, detail=data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
