# Exchange Rate Provider API

Provides USD to MXN exchange rate from various sources and agregates them in a single request.


## Features:

#### Per User Token Authentication:

Each user has only one api token, must send it as ```Authorization: Token <TOKEN>```.


#### Rate Limiting:

Each user is rate limited to 2 requests per minute for demo purposes.


## TODO

- ~Models~
- ~Serializers~
- ~Authentication~ missing single token only.
- ~Views~
- ~Scrapping~
- ~Tests~
- Indexing
- I18N/L10N
- Admin customization

## Missing

- Missing parametrization for throttling.
- Missing currency Codes?
- Missing correct Docker configuration (Delete App volume, use dockerignore)
- Missing development instructions
- Missing deployment instructions
- Missing some documentation
