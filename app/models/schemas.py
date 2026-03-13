from pydantic import BaseModel, Field
from typing import Optional

class SentimentRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=500, examples=["I am verry happy today"])

class SentimentReponse(BaseModel):
    label: str
    score: float
    status: str = "succes"

class HealthReponse(BaseModel):
    status: str
    version: str