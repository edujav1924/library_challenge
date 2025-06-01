#!/bin/bash
set -e

pip install -r src/requirements.txt
pip install --upgrade pip

python src/core/manage.py migrate --noinput
python src/core/manage.py import_initial_data
{
    python src/core/manage.py createsuperuser --noinput
} || echo "createsuperuser failed, continuing..."
exec "$@"