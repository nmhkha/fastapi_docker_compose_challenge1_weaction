from fastapi import APIRouter, HTTPException
from app.models.schemas import SentimentRequest, SentimentReponse, HealthReponse
from app.serviecs.core import analyze_sentiment

router = APIRouter()

@router.get("/health", response_model=HealthReponse)
def health_check():
    return {"status", "healthy", "version", "1.0.0"}

@router.post("/predict", response_model=SentimentReponse)
async def predict(payload: SentimentRequest):
    try:
        #inference
        result = analyze_sentiment(payload.text)
        return {
            "label": result["label"],
            "score": result["score"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/history")
def get_history():
    # Placeholder cho kết nối Database
    return {"message": "Tính năng lưu Database sẽ được query tại đây", "data": []}