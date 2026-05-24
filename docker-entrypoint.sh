#!/bin/bash

echo "Applying database migrations..."
python manage.py migrate

echo "Seeding database..."
python manage.py seed_db

echo "Creating superuser..."
python manage.py create_superuser_env

echo "Starting server..."
gunicorn storefront.wsgi:application --bind 0.0.0.0:8000 --workers 2 --timeout 120
