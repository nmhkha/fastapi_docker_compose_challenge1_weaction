from pydantic import BaseModel, Field
from typing import Optional

class SentimentRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=500, examples=["Hôm nay tôi rất vui"])

class SentimentReponse(BaseModel):
    label: str
    score: float
    status: str = "succes"

class HealthReponse(BaseModel):
    status: str
    version: str