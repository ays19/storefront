release: python3 manage.py migrate
web: gunicorn storefront.wsgi
worker: celery -A storefront worker