import pytest
from django.urls import reverse

@pytest.fixture
def rate_url():
    return reverse("rates")

# @pytest.mark.django_db
# def test_rates(api_client, rate, rate_url):
#     response = api_client.get(rate_url)
#     response_json = response.json()



#     expected_response = [{
#         'provider_id': 'DOF',
#         'provider_verbose_name': 'Diaro Oficial de la Federación',
#         'rates': [{
#             'last_updated': "2022-01-18T05:21:58.818654Z",
#             'last_updated_provider': "2022-01-18T05:21:58.818654Z",
#             'value': '20.774400',
#             'variant': 1,
#             'variant_name': 'default'
#         }]
#     }, {
#         'provider_id': 'FXR',
#         'provider_verbose_name': 'Fixer',
#         'rates': []
#     }, {
#         'provider_id': 'BXO',
#         'provider_verbose_name': 'Banxico',
#         'rates': []
#     }]

#     assert response.status_code == 200
#     assert response_json[0]

@pytest.mark.django_db
def test_throttling(api_client, rate_url):

    response = api_client.get(rate_url)
    assert response.status_code == 200

    response = api_client.get(rate_url)
    assert response.status_code == 200

    response = api_client.get(rate_url)
    assert response.status_code == 429
