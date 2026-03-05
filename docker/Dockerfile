# ── Stage 1: Builder ──────────────────────────────────────────────
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
# Ép cài đặt vào hệ thống gốc của builder
RUN pip install --no-cache-dir -r requirements.txt

# ── Stage 2: Runtime ──────────────────────────────────────────────
FROM python:3.11-slim
WORKDIR /app

# Copy TOÀN BỘ thư mục local - nơi chứa cả thư viện và file thực thi uvicorn
COPY --from=builder /usr/local /usr/local

# Copy source code (Đảm bảo đúng cấu trúc của Kha)
COPY . .

# Tránh lỗi #8: Non-root user
RUN useradd -m aiuser && chown -R aiuser /app
USER aiuser

# BỔ SUNG QUAN TRỌNG: Khai báo PATH rõ ràng cho aiuser
ENV PATH="/usr/local/bin:${PATH}"

EXPOSE 8000

# Dùng lệnh này để chắc chắn nhất
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]