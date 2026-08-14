from google import genai
from google.genai import types
from app.models import BusinessRequest
from app.utils.logger import logger

def run_ingest_agent(client: genai.Client, request: BusinessRequest) -> str:
    logger.info("Executing Agent 1: Ingestion & Schema Extraction (Gemini 2.5 Flash)")
    
    prompt = f"""
    Extract key criteria from the following raw request:
    Client: {request.client_name}
    Request: {request.raw_prompt}
    
    Return a clean JSON object with:
    - client_name
    - core_objective
    - parsed_requirements (array of strings)
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.1
        )
    )
    return response.text
