FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

WORKDIR /app

# Install Python dependencies
COPY backend/requirements.txt /app/requirements.txt
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r /app/requirements.txt

# Copy Django project
COPY backend /app/

CMD ["sh", "-c", "python3 manage.py migrate --noinput && gunicorn core.wsgi:application --bind 0.0.0.0:$PORT --workers 3"]
