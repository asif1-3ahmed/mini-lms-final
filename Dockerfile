# backend/Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# system deps required for psycopg2 / building wheels
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# copy requirements (Dockerfile is inside backend/)
COPY requirements.txt /app/requirements.txt

# install python deps
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache-dir -r /app/requirements.txt

# copy backend sources into container
COPY . /app/

# (optional) env so any manage.py import settings works — usually core.settings already set by project
ENV DJANGO_SETTINGS_MODULE=core.settings

# expose port (helpful for local debugging; Railway uses $PORT)
EXPOSE 8000

# Run migrations, create default superuser (if script exists) then start gunicorn.
# create_superuser script must be at backend/create_superuser.py
CMD sh -c "python3 manage.py migrate --noinput && \
           if [ -f create_superuser.py ]; then python3 manage.py shell < create_superuser.py || true; fi && \
           gunicorn core.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3"
