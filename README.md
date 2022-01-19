# Exchange Rate Provider API

Provides USD to MXN exchange rate from various sources and agregates them in a single request.


## Features:

#### Per User Token Authentication:

Each user has only one api token, must send it as ```Authorization: Token <TOKEN>```.


#### Rate Limiting:

Each user is rate limited to 2 requests per minute for demo purposes.


## Development Instructions:

You need to provide a valid .env file with the following parameters:

```.env
POSTGRES_DB
POSTGRES_USER
POSTGRES_PASSWORD
DATABASE_URL

RABBITMQ_DEFAULT_USER
RABBITMQ_DEFAULT_PASS
RABBITMQ_DEFAULT_VHOST
CELERY_BROKER_URL

DJANGO_SETTINGS_MODULE
SECRET_KEY
FIXER_API_KEY
BANXICO_API_KEY
```

1. Run ```docker-compose --up``` in your terminal.
2. Connect to ```xrate_provider_service``` container and change directory to to ```xrate_provider```.
3. Execute ```python manage.py migrate```.
4. Execute ```python manage.py createsuperuser``` to create a Django admin superuser.

Service is available at [http://localhost:8000/service/v1/rates/](http://localhost:8000/service/v1/rates/)
Admin panel is available at [http://localhost:8000/admin/](http://localhost:8000/admin)


## Missing

- Missing parametrization for throttling.
- Missing currency Codes ?
- Missing correct Docker configuration (Delete App volume to use .dockerignore).
- Missing deployment instructions.

## TODO

- ~Models~
- ~Serializers~
- ~Authentication~
- ~Views~
- ~Scrapping~
- ~Tests~
- ~Linting~

- Indexing
- I18N/L10N
- Admin customization

