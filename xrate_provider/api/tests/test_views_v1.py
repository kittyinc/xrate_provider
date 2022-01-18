import pytest
from django.urls import reverse
from api.tests.data.expected_data import VIEWS_V1_RATES_VALID_OUTPUT

# views_v1

@pytest.fixture
def rate_url():
    return reverse("rates")

@pytest.mark.django_db
def test_rates(api_client, rate_dof_variant_fix, rate_url):
    ''' Tests v1/rates/ output''' # Should load data from fixture.
    
    response = api_client.get(rate_url)

    assert response.status_code == 200
    assert response.json() == VIEWS_V1_RATES_VALID_OUTPUT



# @pytest.mark.django_db
# def test_rates_ordering(api_client, rate, rate_url):
#     ''' Tests v1/rates/ output for correct latest rate variant ordering'''
#     pass

@pytest.mark.django_db
def test_throttling(api_client, rate_url):
    ''' Tests v1/rates/ throttling rate (i.e: 2/min = 3 calls in quick succession)''' # should load throttling rate from view class.
    response = api_client.get(rate_url)
    assert response.status_code == 200

    response = api_client.get(rate_url)
    assert response.status_code == 200

    response = api_client.get(rate_url)
    assert response.status_code == 429
