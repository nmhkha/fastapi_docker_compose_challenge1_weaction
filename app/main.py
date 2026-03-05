import os
from fastapi import FastAPI
from app.routers import api
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AI Sentiment Service", version="1.0.0")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/mydb")
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:8000").split(",")

# Tránh lỗi #7: Chỉ cho phép domain cụ thể (ví dụ localhost để test)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Kết nối router
app.include_router(api.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Welcome to AI Service. Go to /docs for Swagger UI"}