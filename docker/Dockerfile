# ==========================================
# Stage 1: Builder
# ==========================================
FROM python:3.11-slim AS builder
WORKDIR /app

# Khởi tạo môi trường ảo (virtual environment)
RUN python -m venv /opt/venv

# Kích hoạt môi trường ảo 
ENV PATH="/opt/venv/bin:$PATH"

# Copy file requirements và cài đặt dependencies vào .venv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ==========================================
# Stage 2: Runtime
# ==========================================
FROM python:3.11-slim
WORKDIR /app

#
COPY --from=builder /opt/venv /opt/venv

# Kích hoạt môi trường ảo stage runtime
ENV PATH="/opt/venv/bin:$PATH"

# Tránh lỗi #8: Tạo và sử dụng non-root user
RUN useradd -m aiuser && chown -R aiuser /app
USER aiuser

# Copy toàn bộ source code vào
COPY . .

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]