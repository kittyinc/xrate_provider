from django.conf import settings
from datetime import datetime
from django.utils.timezone import make_aware
from rates.models import Rate, PROVIDER_CHOICES

import requests


def get_fixer_variant_1():
    variant_number = 1
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

    response = r.json() # might error out on breaking API change. Needs to plug in to a serializer, test the fucntion

    last_updated_provider =  make_aware(
        datetime.fromtimestamp(response['timestamp'])
    )

    output = {
        "provider": PROVIDER_CHOICES[1][0], # might error out on PROVIDER_CHOICES change, needs test
        "last_updated": last_updated,
        "value": response["rates"]["MXN"],
        "variant": variant_number
    }

    return output, False



providers = {
    "Fixer": [get_fixer_variant_1,]
}

def update_rates():
    for provider, variants in providers.items():
        for variant in variants:
            output, err = variant()
            if err:
                # queue this variant again for retry in a separate task. Log and Notify via Sentry on repeat threshold
                pass

            else:
                rate = Rate(**output)
                rate.save() # Needs to try to save the variant in case of error
