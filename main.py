from fastapi import FastAPI, HTTPException
from schemas import LoanApplication, RiskAssessmentResponse
from risk_engine import CrediGuardEngine

app = FastAPI(
    title="CrediGuard AI - Autonomous BFSI Underwriting API",
    version="1.0.0",
    description="Real-time multi-agent underwriting and fraud risk scoring engine."
)

engine = CrediGuardEngine()

@app.get("/")
def read_root():
    return {"status": "online", "system": "CrediGuard AI Underwriting Engine v1.0"}

@app.post("/api/v1/evaluate", response_model=RiskAssessmentResponse)
def evaluate_loan(application: LoanApplication):
    try:
        result = engine.evaluate(application)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
