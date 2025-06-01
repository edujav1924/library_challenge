#!/bin/bash
set -e
source /etc/environment
cd /app
python manage.py migrate --noinput
python manage.py collectstatic --noinput 
{
    python manage.py createsuperuser --noinput
} || echo "createsuperuser failed, continuing..."
python manage.py import_initial_data
exec "$@"