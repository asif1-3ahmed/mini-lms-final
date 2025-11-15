# ===============================
# Base Image
# ===============================
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ===============================
# System Dependencies
# ===============================
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean

# ===============================
# Work Directory
# ===============================
WORKDIR /app

# ===============================
# Install Python Requirements
# ===============================
# because Dockerfile is inside backend/
COPY backend/requirements.txt /app/requirements.txt

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r /app/requirements.txt

# ===============================
# Copy Backend Code
# ===============================
COPY . /app/
# Copies everything from backend folder into /app

# ===============================
# Environment
# ===============================
ENV DJANGO_SETTINGS_MODULE=core.settings

# ===============================
# Run Migrations + Create Superuser + Start Gunicorn
# ===============================
CMD sh -c "python3 manage.py migrate --noinput && \
           python3 manage.py shell < create_superuser.py || true && \
           gunicorn core.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3"
