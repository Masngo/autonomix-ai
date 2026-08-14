from google import genai
from google.genai import types
from app.utils.logger import logger

def run_audit_agent(client: genai.Client, proposal_text: str) -> str:
    logger.info("Executing Agent 3: Compliance & Verification Auditor (Gemini 2.5 Flash)")
    
    prompt = f"""
    Audit the following generated proposal for operational feasibility, formatting, and completeness:
    {proposal_text}
    
    Return JSON format with:
    - status (PASS or FAIL)
    - compliance_score (0.0 to 1.0)
    - reasoning (short explanation)
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
