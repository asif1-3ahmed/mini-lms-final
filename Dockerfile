FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy backend requirements
COPY backend/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy backend folder
COPY backend /app/

# Run migrations + create superuser + start gunicorn
CMD sh -c "python manage.py migrate --noinput && \
           python create_superuser.py && \
           gunicorn core.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3"
