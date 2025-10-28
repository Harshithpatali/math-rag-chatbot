# 🧠 Base image: small and Python 3.10 optimized
FROM python:3.10-slim

# Avoid Python buffering issues
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (FAISS & others)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency file first for caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Streamlit specific environment
ENV STREAMLIT_PORT=8080

# Expose Streamlit port
EXPOSE 8080

# 🏃 Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
