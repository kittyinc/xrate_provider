from .base import * 
from os import environ

import dj_database_url

DEBUG = True
ALLOWED_HOSTS = []

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_RESULT_BACKEND = 'django-db'


try:
    SECRET_KEY = environ["SECRET_KEY"]
except KeyError as e:
    print("SECRET_KEY env variable not set") # CHANGE TO logger.error
    raise e

try:
    DATABASE_URL = environ["DATABASE_URL"]
except KeyError as e:
    print("DATABASE_URL env variable not set") # CHANGE TO logger.error
    raise e

try:
    CELERY_BROKER_URL = environ["CELERY_BROKER_URL"]
except KeyError as e:
    print("CELERY_BROKER_URL env variable not set") # CHANGE TO logger.error
    raise e


DATABASES = {}
DATABASES['default'] = dj_database_url.config(
    default=DATABASE_URL, 
    conn_max_age=600
)



