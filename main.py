"""
main.py
Created: 2026-01-01T11:21:50+09:00
"""

import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
import os
from models.legal_advisor_model import get_legal_model
from utils.text_processor import clean_text
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Legal AI Model & Solution Studio",
    description="Domain-specific AI for providing high-accuracy legal advice and document analysis.",
    version="1.0.0"
)

# Request Models
class AdviceRequest(BaseModel):
    question: str
    category: str = "general"

class AdviceResponse(BaseModel):
    question: str
    advice: str
    status: str = "success"

@app.get("/", response_class=HTMLResponse)
async def root():
    template_path = os.path.join("templates", "index.html")
    with open(template_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.post("/legal/advise", response_model=AdviceResponse)
async def get_legal_advice(request: AdviceRequest):
    """
    Provides legal advice based on the provided question using RAG.
    """
    try:
        logger.info(f"Received legal advice request for question: {request.question[:50]}...")
        # Clean the input question
        cleaned_question = clean_text(request.question)
        
        # Get legal advisor model
        advisor = get_legal_model()
        
        # Get advice from the model
        advice = advisor.get_advice(cleaned_question)
        
        logger.info("Advice generated successfully.")
        return AdviceResponse(
            question=cleaned_question,
            advice=advice
        )
    except Exception as e:
        import traceback
        error_detail = f"{str(e)}\n{traceback.format_exc()}"
        logger.error(f"Error processing legal advice: {error_detail}")
        raise HTTPException(status_code=500, detail=error_detail)

if __name__ == "__main__":
    # Use 8001 to avoid frequent port 8000 conflicts
    logger.info("=== Starting Legal AI Studio server ===")
    logger.info("Access the web UI at: http://127.0.0.1:8001")
    uvicorn.run(app, host="127.0.0.1", port=8001, log_level="info")
