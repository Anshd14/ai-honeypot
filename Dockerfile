# Use official lightweight Python image
FROM python:3.10-slim
# Set working directory
WORKDIR /app
# Install system dependencies
RUN apt-get update && apt-get install -y \
         build-essential \
         && rm -rf /var/lib/apt/lists/*
# Copy project files
COPY requirements.txt .
COPY config.yaml .
COPY main.py .
COPY honeypot/ ./honeypot
COPY tests/ ./tests
COPY templates/ ./templates
COPY static/ ./static
# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Expose FastAPI port
EXPOSE 8000
# Run FastAPI app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
