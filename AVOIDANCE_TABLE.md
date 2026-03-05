1. Dùng python:latest làm base image
Cách xử lý: Sử dụng python:3.11-slim kết hợp Multi-stage build để tối ưu dung lượng image từ ~1GB xuống còn khoảng 200MB (chưa tính model weights).

Minh chứng:
FROM python:3.11-slim AS builder
# ... build stage
FROM python:3.11-slim
# ... runtime stage

2. Không có .dockerignore
Cách xử lý: Loại bỏ các file rác, môi trường ảo và cache để giảm build context.

Minh chứng (.dockerignore):
day1/
__pycache__/
.git/
.env

3. Hardcode connection string / password
Cách xử lý: Sử dụng biến môi trường (Environment Variables) để quản lý thông tin nhạy cảm.

Minh chứng:
environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb

4. Không cấu hình healthcheck cho PostgreSQL
Cách xử lý: Ép API chỉ khởi động khi Database thực sự sẵn sàng nhận kết nối.

Minh chứng:
epends_on:
      db:
        condition: service_healthy

5. Nhét toàn bộ logic vào 1 file (Monolith)
Cách xử lý: Tách cấu trúc theo chuẩn FastAPI: routers (điều hướng), models (định dạng dữ liệu), services (logic AI).

Minh chứng


6. Không dùng Pydantic để validate input/output
Cách xử lý: Định nghĩa Schema rõ ràng, giúp FastAPI tự động trả lỗi 422 nếu dữ liệu sai định dạng thay vì gây lỗi 500.

Minh chứng:
class SentimentRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=500, examples=["Hôm nay tôi rất vui"])

7. Cấu hình CORS wildcard allow_origins=["*"]
Cách xử lý: Chỉ cho phép các domain tin cậy được truy cập vào API.

Minh chứng:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000"],)

8. Chạy container với user root
Cách xử lý: Tạo user không có quyền quản trị (non-root user) để hạn chế rủi ro nếu container bị tấn công.

Minh chứng:
RUN useradd -m aiuser && chown -R aiuser /app
USER aiuser