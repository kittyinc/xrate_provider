# Exchange Rate API

Provides USD to MXN exchange rate from various sources and agregates them in a single request.


#### Authentication:

Each user has only one active API token. The token must be sent as a header:

```Authorization: Token <TOKEN>```


#### Rate Limiting:

Each user is rate limited to 2 requests per minute for demo purposes.


## Development Instructions:

You need to provide a valid ```.env``` file with the following environmental variables set:

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
2. Connect to ```xrate_provider_service``` container and change directory to ```xrate_provider```.
3. Execute ```python manage.py migrate```.
4. Execute ```python manage.py createsuperuser``` to create a Django admin superuser.
5. You need to add a Celery periodic task in the admin with task name ```update_rates_task```.


Service is available at [http://localhost:8000/service/v1/rates/](http://localhost:8000/service/)

Admin panel is available at [http://localhost:8000/admin/](http://localhost:8000/admin)

Service is deployed at: [https://xrate-provider.herokuapp.com/](https://xrate-provider.herokuapp.com/)


## Testing:

Unit tests are executed using pytest.

Tests are located under each app's tests directory.

1. Connect to ```xrate_provider_service``` container and change directory to to ```xrate_provider```.

2. Execute ```pytest```, use ```-vv``` flag for verbose output, use ```--flakes``` for linting.

## Endpoints:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/2214299-796bef2b-240f-4aec-9ec9-13c221b98656?action=collection%2Ffork&collection-url=entityId%3D2214299-796bef2b-240f-4aec-9ec9-13c221b98656%26entityType%3Dcollection%26workspaceId%3D105d3a0f-2400-4d3c-925f-14c5f74d4e93)


[GET] /service/v1/rates/

Headers:
- ```Authorization: Token <TOKEN>```


## Notes

- Error tracking is setup with my personal Sentry account at the moment.
- The project is currently missing throttling parametrization at runtime.
- I did not implement currency codes, due to the explicit USD to MXN requirement. 
- One of the specified providers, Fixer does NOT support currency conversion without a paid plan. I'm using the most basic paid plan.
- This project is deployed to Heroku as the challenge suggested, however, running more than 1 dyno or binding a custom domain name/SSL cert costs.
- To run my chosen task runner (Celery), I need 2 additional dynos, 1 for a worker and 1 for a scheduler, what this means is that rate updating does not work on the deployed instance at the moment.


## TODO

- DB Indexing
- I18N/L10N
- Admin customization

