import json
from fastapi import FastAPI, HTTPException
from google import genai
from app.config import settings
from app.models import BusinessRequest, WorkflowResult
from app.agents.ingest_agent import run_ingest_agent
from app.agents.strategy_agent import run_strategy_agent
from app.agents.audit_agent import run_audit_agent
from app.utils.logger import logger

app = FastAPI(title="Autonomix AI Multi-Agent Engine", version="1.0.0")

@app.get("/")
def health_check():
    return {"status": "online", "system": "Autonomix AI Engine"}

@app.post("/api/v1/execute", response_model=WorkflowResult)
def execute_workflow(request: BusinessRequest):
    try:
        # Initialize Google GenAI Client
        client = genai.Client(api_key=settings.GEMINI_API_KEY)
        
        # 1. Ingestion Agent (Flash)
        ingest_res = run_ingest_agent(client, request)
        ingest_data = json.loads(ingest_res)
        
        # 2. Strategy Agent (Pro)
        proposal_res = run_strategy_agent(client, ingest_res)
        
        # 3. Audit Agent (Flash)
        audit_res = run_audit_agent(client, proposal_res)
        audit_data = json.loads(audit_res)
        
        logger.info("Multi-Agent Execution Pipeline Completed Successfully")
        
        return WorkflowResult(
            client_name=request.client_name,
            ingestion=ingest_data,
            proposal=proposal_res,
            audit=audit_data
        )
    except Exception as e:
        logger.error(f"Pipeline execution failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
