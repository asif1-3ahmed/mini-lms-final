FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# System deps
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean

# Work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r /app/requirements.txt

# Copy ENTIRE backend folder (core/, accounts/, manage.py, etc.)
COPY . /app/

# Expose port
EXPOSE 8000

# Run migrations + start Gunicorn
CMD sh -c "python3 manage.py migrate --noinput && \
           gunicorn core.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3"
