# AI Sentiment Service

Dự án mẫu FastAPI cung cấp dịch vụ phân tích cảm xúc (sentiment analysis) sử dụng Transformers.

Đường dẫn chính:
- Source app: [Day_1/ai_service_kha/app/main.py](Day_1/ai_service_kha/app/main.py) — chạy FastAPI app [`app.main.app`](Day_1/ai_service_kha/app/main.py)  
- Router API: [Day_1/ai_service_kha/app/routers/api.py](Day_1/ai_service_kha/app/routers/api.py) — router [`app.routers.api.router`](Day_1/ai_service_kha/app/routers/api.py)  
- Logic AI: [Day_1/ai_service_kha/app/serviecs/core.py](Day_1/ai_service_kha/app/serviecs/core.py) — classifier [`app.serviecs.core.classifier`](Day_1/ai_service_kha/app/serviecs/core.py) và hàm [`app.serviecs.core.analyze_sentiment`](Day_1/ai_service_kha/app/serviecs/core.py)  
- Schemas Pydantic: [Day_1/ai_service_kha/app/models/schemas.py](Day_1/ai_service_kha/app/models/schemas.py) — [`app.models.schemas.SentimentRequest`](Day_1/ai_service_kha/app/models/schemas.py), [`app.models.schemas.SentimentReponse`](Day_1/ai_service_kha/app/models/schemas.py), [`app.models.schemas.HealthReponse`](Day_1/ai_service_kha/app/models/schemas.py)

Tài liệu liên quan:
- Yêu cầu Python: [Day_1/ai_service_kha/requirements.txt](Day_1/ai_service_kha/requirements.txt)  
- Dockerfile: [Day_1/ai_service_kha/docker/Dockerfile](Day_1/ai_service_kha/docker/Dockerfile)  
- Docker Compose: [Day_1/ai_service_kha/docker/docker-compose.yml](Day_1/ai_service_kha/docker/docker-compose.yml)  
- Docker ignore: [Day_1/ai_service_kha/.dockerignore](Day_1/ai_service_kha/.dockerignore)  
- Git ignore: [Day_1/ai_service_kha/.gitignore](Day_1/ai_service_kha/.gitignore)  
- Các best-practice / checklist: [Day_1/ai_service_kha/AVOIDANCE_TABLE.md](Day_1/ai_service_kha/AVOIDANCE_TABLE.md)

Requirements
- Python 3.11+ (hoặc dùng Docker)
- Pip packages: xem [requirements.txt](Day_1/ai_service_kha/requirements.txt)

Chạy local (virtualenv)
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r [requirements.txt](http://_vscodecontentref_/0)
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000