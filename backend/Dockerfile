# ===== Use official Python image =====
FROM python:3.11-slim

# ===== Environment settings =====
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ===== Install system libs (needed for psycopg2 + Django) =====
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean

# ===== Set work directory =====
WORKDIR /app

# ===== Install Python dependencies =====
COPY backend/requirements.txt /app/requirements.txt
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r /app/requirements.txt

# ===== Copy Django backend =====
COPY backend /app/

# ===== Expose port for debugging (Railway will set the real port) =====
EXPOSE 8000

# ===== Start command =====
# Runs migrations + starts gunicorn
CMD ["sh", "-c", "python3 manage.py migrate --noinput && gunicorn core.wsgi:application --bind 0.0.0.0:$PORT --workers 3"]
