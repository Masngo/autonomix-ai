from google import genai
from google.genai import types
from app.utils.logger import logger

def run_strategy_agent(client: genai.Client, ingestion_json: str) -> str:
    logger.info("Executing Agent 2: Strategy & Asset Generation (Gemini 2.5 Pro)")
    
    prompt = f"""
    You are Autonomix Strategy Agent. Build a complete operational proposal and service agreement draft based on these structured requirements:
    {ingestion_json}
    
    Include executive summary, scope of work, timeline, and deliverables.
    """
    
    response = client.models.generate_content(
        model='gemini-2.5-pro',
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.2
        )
    )
    return response.text
