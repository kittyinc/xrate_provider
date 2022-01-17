from django.conf import settings
from datetime import datetime
from django.utils.timezone import make_aware
from rates.models import Rate, PROVIDER_CHOICES

import requests
import pytz
from rates.dof import get_dof_variant_all

BANXICO_TZ = pytz.timezone('America/Mexico_City')

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
        return [{}], True

    response = r.json()

    last_updated_provider =  make_aware(
        datetime.fromtimestamp(response['timestamp']) # Date in UTC according to API, same as server and spec.
    )

    # might error out on breaking API change. Needs to plug in to a serializer, test the fucntion
    # might error out on PROVIDER_CHOICES change, needs test
    output = {
        "provider": PROVIDER_CHOICES[1][0],
        "last_updated_provider": last_updated_provider,
        "value": response["rates"]["MXN"],
        "variant": variant_number
    }

    return [output], False



def get_banxico_variant_1():
    '''Reimplement with XML according to spec'''
    variant_number = 1
    url = settings.BANXICO_SETTINGS["url"]
    api_key = settings.BANXICO_SETTINGS["api_key"]

    headers = {
        "Bmx-Token": api_key
    }

    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        return [{}], True

    response = r.json()
    data = response["bmx"]["series"][0]["datos"][0] # should reasonably respond only one entry according to the API
    
    last_updated_provider = make_aware( 
        datetime.strptime(data["fecha"], "%d/%m/%Y"),
        timezone=BANXICO_TZ,
        is_dst=None # Banxico API does not specify timezone, need to test for it
    )
    
    output = {
        "provider": PROVIDER_CHOICES[2][0],
        "last_updated_provider": last_updated_provider,
        "value": data["dato"],
        "variant": variant_number
    }

    return [output], False



providers = {
    "Fixer": [get_fixer_variant_1,],
    "Banxico": [get_banxico_variant_1,],
    "Diario Oficial": [get_dof_variant_all,]
}

def update_rates():
    for provider, variants in providers.items():
        for variant in variants:
            output, err = variant() # logger.info

            if err:
                # queue this variant again for retry in a separate task. Log and Notify via Sentry on repeat threshold
                pass

            else:
                for o in output: # should bulk create
                    rate = Rate(**o)
                    rate.save() # Needs to try to save the variant in case of error
