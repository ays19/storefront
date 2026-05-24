release: python manage.py migrate && python manage.py collectstatic --noinput
web: python manage.py collectstatic --noinput && gunicorn storefront.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --timeout 120
worker: celery -A storefront.celery worker --pool=solo -l info