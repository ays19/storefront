import pymysql
pymysql.install_as_MySQLdb()

from .celery import celery as celery_app
__all__ = ('celery_app',)
