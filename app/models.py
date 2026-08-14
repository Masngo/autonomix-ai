from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class BusinessRequest(BaseModel):
    client_name: str = Field(..., example="Acme Corp")
    raw_prompt: str = Field(..., example="Automate customer intake and tailored proposal generation")
    metadata: Optional[Dict[str, Any]] = None

class IngestionOutput(BaseModel):
    client_name: str
    core_objective: str
    parsed_requirements: list[str]

class AuditOutput(BaseModel):
    status: str
    compliance_score: float
    reasoning: str

class WorkflowResult(BaseModel):
    client_name: str
    ingestion: Dict[str, Any]
    proposal: str
    audit: Dict[str, Any]
