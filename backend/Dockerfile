FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# System deps
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean

# App folder
WORKDIR /app

# Install dependencies
COPY backend/requirements.txt /app/requirements.txt
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r /app/requirements.txt

# Copy project
COPY backend /app/

# Start command (migrate + auto-superuser + gunicorn)
CMD sh -c "python3 manage.py migrate --noinput && \
           python3 manage.py shell < create_superuser.py && \
           gunicorn core.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3"
