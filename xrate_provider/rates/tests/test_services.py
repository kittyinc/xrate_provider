from rates.dof import get_dof_variant_all
from rates.services import get_fixer_variant_1
from rates.tests.data.jsons import FIXER_VALID_RESPONSE

from django.conf import settings

import codecs

class MockResponse:
    def __init__(self, content, status_code):
        self.content = content
        self.status_code = status_code

    def json(self):
        return self.content

def test_get_dof_variant_all(mocker):
    expected_url = settings.BANXICO_SETTINGS["url"] # "https://www.banxico.org.mx/tipcamb/tipCamMIAction.do"

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
    print(output)

    assert output == "steve"

    # ASSERT HERE
    mocked_method.assert_called_once_with(expected_url)


def test_get_fixer_variant_1(mocker):
    expected_url = settings.FIXER_SETTINGS["url"]
    api_key = settings.FIXER_SETTINGS["api_key"]

    mocked_method = mocker.patch(
        'rates.dof.requests.get',
        return_value=MockResponse(FIXER_VALID_RESPONSE, 200)
    )

    output = get_fixer_variant_1()
    # assert output == "steve"
    mocked_method.assert_called_once_with(
        expected_url,
        params={
            "access_key": api_key,
            "base": "USD",
            "symbols": "MXN",
        }
)

