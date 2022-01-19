from .base import *  # noqa: F403 F401
from os import environ

import dj_database_url

DEBUG = True
ALLOWED_HOSTS = ["*"]

CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_RESULT_BACKEND = 'django-db'


try:
    SECRET_KEY = environ["SECRET_KEY"]
except KeyError as e:
    print("SECRET_KEY env variable not set")  # CHANGE TO logger.error
    raise e

try:
    DATABASE_URL = environ["DATABASE_URL"]
except KeyError as e:
    print("DATABASE_URL env variable not set")  # CHANGE TO logger.error
    raise e

try:
    CELERY_BROKER_URL = environ["CELERY_BROKER_URL"]
except KeyError as e:
    print("CELERY_BROKER_URL env variable not set")  # CHANGE TO logger.error
    raise e

try:
    FIXER_API_KEY = environ["FIXER_API_KEY"]
except KeyError as e:
    print("FIXER_API_KEY env variable not set")  # CHANGE TO logger.error
    raise e

try:
    BANXICO_API_KEY = environ["BANXICO_API_KEY"]
except KeyError as e:
    print("BANXICO_API_KEY env variable not set")  # CHANGE TO logger.error
    raise e


FIXER_SETTINGS = {
    "url": "https://data.fixer.io/api/latest",
    "api_key": FIXER_API_KEY
}

BANXICO_SETTINGS = {
    "url": "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/oportuno",  # noqa: E501
    "api_key": BANXICO_API_KEY
}

DOF_SETTINGS = {
    "url": "https://www.banxico.org.mx/tipcamb/tipCamMIAction.do"
}


DATABASES = {}
DATABASES['default'] = dj_database_url.config(
    default=DATABASE_URL,
    conn_max_age=600
)
