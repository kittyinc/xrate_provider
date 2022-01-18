from pytest_factoryboy import register
from rates.tests.factories import RateFactory
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from django.contrib.auth import get_user_model


import pytest

@pytest.fixture
def rate_dof_variant_fix(rate):
    rate.variant = 1
    rate.variant_name = "FIX"
    rate.save()
    return rate


@pytest.fixture
def api_client(token):
    # Include an appropriate `Authorization:` header on all requests.
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return client


@pytest.fixture
def token(user):
    token = Token.objects.create(user=user)
    return token


@pytest.fixture
def user():
    user = get_user_model().objects.create(
        username="Test User 1",
        email="test_user@emial.com",
    )
    return user

register(RateFactory)


    # rate_data = [
    # {
    #     "provider": "DOF",
    #     "last_updated_provider": "2022-01-17T06:00:00Z",
    #     "value": 20.300200,
    #     "variant": 1,
    #     "variant_name": "FIX"
    # },
    # {
    #     "provider": "DOF",
    #     "last_updated_provider": "2022-01-17T06:00:00Z",
    #     "value": 20.311800,
    #     "variant": 2,
    #     "variant_name": "Publicacion DOF"
    # }


#     rate_output = [
#     {
#         "provider_id": "DOF",
#         "provider_verbose_name": "Diaro Oficial de la Federación",
#         "rates": [
#             {
#                 "last_updated_provider": "2022-01-17T06:00:00Z",
#                 "value": "20.300200",
#                 "variant": 1,
#                 "variant_name": "FIX"
#             },
#             {
#                 "last_updated_provider": "2022-01-17T06:00:00Z",
#                 "value": "20.311800",
#                 "variant": 2,
#                 "variant_name": "Publicacion DOF"
#             },
#         ]
#     },
# ]