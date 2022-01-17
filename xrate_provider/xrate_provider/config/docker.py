from .base import * 
from os import environ

import dj_database_url

DEBUG = True

ALLOWED_HOSTS = []

try:
    SECRET_KEY = environ["SECRET_KEY"]
except KeyError as e:
    print("SECRET_KEY env variable not set") # CHANGE TO LOGGING
    raise e

try:
    DATABASE_URL = environ["DATABASE_URL"]
except KeyError as e:
    print("DATABASE_URL env variable not set") # CHANGE TO LOGGING


DATABASES = {}
DATABASES['default'] = dj_database_url.config(
    default=DATABASE_URL, 
    conn_max_age=600
)



