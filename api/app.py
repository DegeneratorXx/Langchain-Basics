"""
Historical Summary API Server

This FastAPI application provides an endpoint to generate brief historical 
summaries of cities and places using a local Ollama LLM model.
"""

from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from fastapi import FastAPI, HTTPException
from langchain_ollama import OllamaLLM  # Updated import to use the new package
from pydantic import BaseModel
import os
import uvicorn
import dotenv as env

# Load environment variables from .env file
env.load_dotenv()

# Initialize FastAPI application
app = FastAPI(
    title="Historical Summary API",
    version="1.0.0",
    description="An API server that generates brief historical summaries of cities and places using Ollama LLM"
)


@app.get("/health")
def health_check():
    """Health check endpoint to verify server status."""
    return {"status": "ok"}


# Define the request schema for historical summary endpoint
class HistoricalSummaryRequest(BaseModel):
    """Request model for historical summary generation."""
    place: str

# Set up the LangChain components
ollama_llm = OllamaLLM(model="gemma3:4b")
historical_prompt = ChatPromptTemplate.from_template(
    "Write me a historical overview of this city/place: {place}. The summary should not be too big just short summary in around 300-400 words. "
)

# Create the LangChain processing chain
historical_summary_chain = historical_prompt | ollama_llm

# --- Bypassing add_routes with a manual endpoint ---
@app.post("/history")
async def get_historical_summary(request: HistoricalSummaryRequest):
    """
    Generate a historical summary for a given place.
    
    Args:
        request: HistoricalSummaryRequest containing the place name
        
    Returns:
        dict: Contains the historical summary of the place
        
    Raises:
        HTTPException: If there's an error during summary generation
    """
    try:
        # Manually invoke the chain asynchronously
        result = await historical_summary_chain.ainvoke({"place": request.place})
        return {"historical_summary": result}
    except Exception as e:
        # If the chain fails, return a clear error message
        raise HTTPException(status_code=500, detail=f"Error generating historical summary: {str(e)}")
    

# The original add_routes approach is commented out due to OpenAPI schema generation issues:
# add_routes(
#     app,
#     historical_summary_chain.with_types(input_type=HistoricalSummaryRequest),
#     path="/history"
# )


# Server startup configuration
# Server startup configuration
if __name__ == "__main__":
    uvicorn.run(
        "app:app",  # Use import string format for reload to work
        host="localhost", 
        port=8000,
        reload=True  # Enable auto-reload during development
    )

    