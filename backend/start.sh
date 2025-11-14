#!/bin/bash
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Migrations completed. Starting gunicorn..."
exec gunicorn core.wsgi --log-file - "$@"
