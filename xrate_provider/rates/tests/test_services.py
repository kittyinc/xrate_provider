from rates.dof import get_dof_variant_all
from rates.services import get_fixer_variant_1, get_banxico_variant_1

from rates.tests.data.jsons import (
    FIXER_VALID_RESPONSE,
    BANXICO_VALID_RESPONSE,
)

from rates.tests.data.expected_data import (
    FIXER_VARIANT_1_VALID_OUTPUT,
    BANXICO_VARIANT_1_VALID_OUTPUT,
    DOF_VARIANT_ALL_VALID_OUTPUT,

    DEFAULT_FAILURE_OUTPUT,
)

from django.conf import settings

import codecs # Needed for invalid UTF-8 Decoding

class MockResponse:
    def __init__(self, content, status_code):
        self.content = content
        self.status_code = status_code

    def json(self):
        return self.content

# DIARIO OFICIAL DE LA FEDERACION

def test_get_dof_variant_all(mocker):
    ''' Tests DOF service parsing and assembly function for a valid HTML response'''
    expected_url = settings.DOF_SETTINGS["url"]

    f = codecs.open(
        f"rates/tests/data/diario_valid_response.html",
        "r",
        encoding="utf-8",
        errors="ignore"
    )
    
    mocked_method = mocker.patch(
        'rates.dof.requests.get',
        return_value=MockResponse(f.read(), 200)
    )
    
    f.close()
    
    output = get_dof_variant_all()
    mocked_method.assert_called_once_with(expected_url)
    
    assert output == DOF_VARIANT_ALL_VALID_OUTPUT


def test_get_dof_variant_all_failure(mocker):
    ''' Tests DOF service parsing and assembly function for an invalid response code'''
    expected_url = settings.DOF_SETTINGS["url"]

    mocked_method = mocker.patch(
        'rates.dof.requests.get',
        return_value=MockResponse(None, 500)
    )
    
    output = get_dof_variant_all()
    mocked_method.assert_called_once_with(expected_url)
    assert output == DEFAULT_FAILURE_OUTPUT



# FIXER

def test_get_fixer_variant_1(mocker):
    ''' Tests Fixer service parsing and assembly function for a valid JSON response'''
    expected_url = settings.FIXER_SETTINGS["url"]
    api_key = settings.FIXER_SETTINGS["api_key"]

    mocked_method = mocker.patch(
        'rates.dof.requests.get',
        return_value=MockResponse(FIXER_VALID_RESPONSE, 200)
    )

    output = get_fixer_variant_1()
    mocked_method.assert_called_once_with(
        expected_url,
        params={
            "access_key": api_key,
            "base": "USD",
            "symbols": "MXN",
        }
    )
    assert output == FIXER_VARIANT_1_VALID_OUTPUT

def test_get_fixer_variant_1_failure(mocker):
    ''' Tests Fixer service parsing and assembly function for an error response'''
    expected_url = settings.FIXER_SETTINGS["url"]
    api_key = settings.FIXER_SETTINGS["api_key"]

    mocked_method = mocker.patch(
        'rates.dof.requests.get',
        return_value=MockResponse(None, 500)
    )

    output = get_fixer_variant_1()
    mocked_method.assert_called_once_with(
        expected_url,
        params={
            "access_key": api_key,
            "base": "USD",
            "symbols": "MXN",
        }
    )
    assert output == DEFAULT_FAILURE_OUTPUT


# BANXICO

def test_get_banxico_variant_1(mocker):
    ''' Tests Banxico service parsing and assembly function for a valid JSON response'''
    expected_url = settings.BANXICO_SETTINGS["url"]
    api_key = settings.BANXICO_SETTINGS["api_key"]

    mocked_method = mocker.patch(
        'rates.services.requests.get',
        return_value=MockResponse(BANXICO_VALID_RESPONSE, 200)
    )

    output = get_banxico_variant_1()
    mocked_method.assert_called_once_with(
        expected_url,
        headers = {
            "Bmx-Token": api_key
        }

    )
    assert output == BANXICO_VARIANT_1_VALID_OUTPUT


def test_get_banxico_variant_1_failure(mocker):
    ''' Tests Banxico service parsing and assembly function for an error response code'''
    expected_url = settings.BANXICO_SETTINGS["url"]
    api_key = settings.BANXICO_SETTINGS["api_key"]

    mocked_method = mocker.patch(
        'rates.services.requests.get',
        return_value=MockResponse(None, 500)
    )

    output = get_banxico_variant_1()
    mocked_method.assert_called_once_with(
        expected_url,
        headers = {
            "Bmx-Token": api_key
        }

    )
    assert output == DEFAULT_FAILURE_OUTPUT
