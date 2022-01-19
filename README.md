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
5. You need to add a Celery Periodic Task in the admin with task name ```update_rates_task```.

Service is available at [http://localhost:8000/service/v1/rates/](http://localhost:8000/service/v1/rates/)

Admin panel is available at [http://localhost:8000/admin/](http://localhost:8000/admin)

Service is deployed at: [https://xrate-provider.herokuapp.com/](https://xrate-provider.herokuapp.com/)


## Endpoints:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/2214299-796bef2b-240f-4aec-9ec9-13c221b98656?action=collection%2Ffork&collection-url=entityId%3D2214299-796bef2b-240f-4aec-9ec9-13c221b98656%26entityType%3Dcollection%26workspaceId%3D105d3a0f-2400-4d3c-925f-14c5f74d4e93)


[GET] /service/v1/rates/

Headers:
- ```Authorization: Token <TOKEN>```


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

