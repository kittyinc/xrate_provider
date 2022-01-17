from django.conf import settings
from datetime import datetime
from django.utils.timezone import make_aware
from rates.models import Rate, PROVIDER_CHOICES

import requests


def get_fixer_variant_1(varinat_number):
    url = settings.FIXER_SETTINGS["url"]
    api_key = settings.FIXER_SETTINGS["api_key"]

    params = {
        "access_key": api_key,
        "base": "USD",
        "symbols": "MXN",
    }

    r = requests.get(url, params=params)

    if r.status_code != 200:
        return {}, True # Return error for retry,

    response = r.json() # might error out on breaking API change.
    # response = {'success': True, 'timestamp': 1642403943, 'base': 'USD', 'date': '2022-01-17', 'rates': {'MXN': 20.320402}}

    last_updated =  make_aware(
        datetime.fromtimestamp(response['timestamp'])
    )

    output = {
        "provider": PROVIDER_CHOICES[1][0], # might error out on PROVIDER_CHOICES change, needs test
        "last_updated": last_updated,
        "value": response["rates"]["MXN"],
        "variant": varinat_number
    }

    return output, False



providers = {
    "Fixer": [get_fixer_variant_1,]
}

def update_rates():
    for provider, variants in providers.items():
        for idx, variant in enumerate(variants): # variants might not always have the same number, needs change/test
            output, err = variant(idx + 1)
            if err:
                # queue this variant again for retry in a separate task. Log and Notify via Sentry on repeat threshold
                pass

            else:
                rate = Rate(**output)
                rate.save() # Needs to try to save the variant in case of error
