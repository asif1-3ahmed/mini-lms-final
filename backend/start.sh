#!/usr/bin/env bash
set -e

# enter backend
cd backend

# install python deps
pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt

# run migrations (safe: --noinput)
python manage.py migrate --noinput

# collect static (optional, won't fail if not configured)
python manage.py collectstatic --noinput || true

# start gunicorn on Railway's $PORT
exec gunicorn core.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 3
