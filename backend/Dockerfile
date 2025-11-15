# ===============================
# Base Image
# ===============================
FROM python:3.11-slim

# ===============================
# Environment
# ===============================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ===============================
# System dependencies
# ===============================
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean

# ===============================
# Work directory
# ===============================
WORKDIR /app

# ===============================
# Install Python dependencies
# ===============================
COPY backend/requirements.txt /app/requirements.txt
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r /app/requirements.txt

# ===============================
# Copy backend project
# ===============================
COPY backend /app/

# ===============================
# Run migrations + create superuser + start server  
# ===============================
CMD sh -c "python3 manage.py migrate --noinput && \
           python3 create_superuser.py && \
           gunicorn core.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3"
