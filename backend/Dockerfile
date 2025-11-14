# Use official Python image
FROM python:3.11-slim

# Environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Expose port (optional)
EXPOSE 8000

# Run migrations + start Gunicorn (must use Railway $PORT)
CMD ["sh", "-c", "python3 manage.py migrate --noinput && gunicorn core.wsgi:application --bind 0.0.0.0:$PORT --workers 3"]
