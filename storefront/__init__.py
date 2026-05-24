import pymysql
pymysql.version_info = (2, 2, 1, "final", 0)
pymysql.install_as_MySQLdb()

from .celery import celery as celery_app
__all__ = ('celery_app',)
