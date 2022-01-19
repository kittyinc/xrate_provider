from pytest_factoryboy import register
from rates.tests.factories import RateFactory
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from django.contrib.auth import get_user_model
from django.utils.timezone import make_aware
from datetime import datetime

import pytest


@pytest.fixture
def rate_dof_variant_fix(rate):
    rate.variant = 1
    rate.variant_name = "FIX"
    rate.save()
    return rate


@pytest.fixture
def rate_dof_variant_fix_early():
    rate = RateFactory()
    rate.variant = 1
    rate.variant_name = "FIX"
    rate.value = 1
    rate.last_updated = make_aware(datetime.strptime("17/01/2022", "%d/%m/%Y"))
    rate.save()
    return rate


@pytest.fixture
def rate_dof_variant_fix_late():
    rate = RateFactory()
    rate.variant = 1
    rate.variant_name = "FIX"
    rate.value = 2
    rate.last_updated = make_aware(datetime.strptime("18/01/2022", "%d/%m/%Y"))
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
