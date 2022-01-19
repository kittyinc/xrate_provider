from api.tests.data.expected_data import VIEWS_V1_RATES_VALID_OUTPUT

from django.urls import reverse
from django.utils.dateparse import parse_datetime

import pytest

# views_v1


@pytest.fixture
def rate_url():
    return reverse("rates")


# freeze_gun is not playing nice with REST Framework's Throttling
@pytest.mark.django_db
def test_rates(api_client, rate_dof_variant_fix, rate_url):
    ''' Tests v1/rates/ output'''  # Should load data from fixture.

    response = api_client.get(rate_url)
    response_json = response.json()

    assert response.status_code == 200

    for rate in response_json:
        for variant in rate["rates"]:
            if "last_updated" in variant:
                del(variant["last_updated"])
            if "last_updated_provider" in variant:
                del(variant["last_updated_provider"])

    assert response_json == VIEWS_V1_RATES_VALID_OUTPUT


@pytest.mark.django_db
def test_rates_ordering(
        api_client,
        rate_dof_variant_fix_early,
        rate_dof_variant_fix_late,
        rate_url):
    ''' Tests v1/rates/ output for correct latest rate variant ordering'''

    response = api_client.get(rate_url)
    response_json = response.json()

    response_date = parse_datetime(
        response_json[0]["rates"][0]["last_updated"])

    # Assert were getting the same provider variant
    assert response_json[0]["provider_id"] == \
        rate_dof_variant_fix_late.provider

    assert response_json[0]["rates"][0]["variant"] == \
        rate_dof_variant_fix_late.variant

    # Assert were getting the latest entry for a specific provider variant
    assert response_date != rate_dof_variant_fix_early.last_updated
    assert response_date == rate_dof_variant_fix_late.last_updated

    assert response.status_code == 200


@pytest.mark.django_db
def test_throttling(api_client, rate_url):
    ''' Tests v1/rates/ throttling rate (i.e: 2/min = 3 quick calls)'''
    response = api_client.get(rate_url)
    assert response.status_code == 200

    response = api_client.get(rate_url)
    assert response.status_code == 200

    response = api_client.get(rate_url)
    assert response.status_code == 429
