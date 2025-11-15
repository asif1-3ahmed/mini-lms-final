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
# Working Directory
# ===============================
WORKDIR /app

# ===============================
# Install Python Requirements
# ===============================
COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# ===============================
# Copy Backend
# ===============================
COPY . /app/

# ===============================
# Run Migrations + Create Superuser + Start Gunicorn
# ===============================
CMD sh -c "python3 manage.py migrate --noinput && \
           python3 manage.py shell < create_superuser.py && \
           gunicorn core.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3"
