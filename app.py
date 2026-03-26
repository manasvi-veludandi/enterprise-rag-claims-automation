from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_engine import ClaimsRAGEngine

app = FastAPI(title="Claims Automation API")

class ClaimRequest(BaseModel):
    claim_id: str
    description: str

@app.post("/v1/process-claim")
async def process_claim(request: ClaimRequest):
    try:
        # In a real scenario, API keys would be in environment variables
        engine = ClaimsRAGEngine(api_key="dummy", index_name="prod-claims")
        summary = engine.process_claim(request.description, [])
        return {"claim_id": request.claim_id, "summary": summary, "status": "processed"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "claims-automation"}
