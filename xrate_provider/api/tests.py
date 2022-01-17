from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rates.models import Rate

# Should load from fixture.
rate_output = [
    {
        "provider_id": "DOF",
        "provider_verbose_name": "Diaro Oficial de la Federación",
        "rates": [
            {
                "last_updated_provider": "2022-01-17T06:00:00Z",
                "value": "20.300200",
                "variant": 1,
                "variant_name": "FIX"
            },
            {
                "last_updated_provider": "2022-01-17T06:00:00Z",
                "value": "20.311800",
                "variant": 2,
                "variant_name": "Publicacion DOF"
            },
        ]
    },
]

rate_data = [
    {
        "provider": "DOF",
        "last_updated_provider": "2022-01-17T06:00:00Z",
        "value": 20.300200,
        "variant": 1,
        "variant_name": "FIX"
    },
    {
        "provider": "DOF",
        "last_updated_provider": "2022-01-17T06:00:00Z",
        "value": 20.311800,
        "variant": 2,
        "variant_name": "Publicacion DOF"
    }
]


class RatesTestCase(TestCase):
    def setUp(self):
        pass


    def test_rate_ordering:
        pass

    def test_rate_new:
        pass