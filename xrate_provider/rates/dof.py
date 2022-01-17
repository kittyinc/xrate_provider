from django.conf import settings
from django.utils.timezone import make_aware


from bs4 import BeautifulSoup
from datetime import datetime
from rates.models import PROVIDER_CHOICES

import requests
import pytz


DOF_TZ = pytz.timezone('America/Mexico_City')


def check_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# This function can be massively imporved
def get_dof_variant_all():
    url = settings.DOF_SETTINGS["url"]
    r = requests.get(url)

    if r.status_code != 200:
        return [], True

    soup = BeautifulSoup(r.content, "html5lib")

    evens = soup.find_all("tr", {"class": "renglonPar"})
    odds = soup.find_all("tr", {"class": "renglonNon"})

    raw_values = evens + odds
    values = []

    for item in raw_values:
        values.append([c.text.strip() for c in item.find_all("td")])

    for value in values:
        value[0] = make_aware(
            datetime.strptime(value[0], "%d/%m/%Y"),
            timezone=DOF_TZ,
            is_dst=None
        )

    values.sort(reverse=True)

    variants = [
        ("FIX", 1),
        ("Publicacion DOF", 2),
        ("Para Pagos", 3),
    ]

    output = []

    for idx, variant in enumerate(variants):
        for value in values:
            rate = None

            if check_float(value[idx + 1]):
                rate = value[idx + 1]
                pub_date = value[0]
                break

        if rate is not None:
            output.append(
                {   
                    "provider": PROVIDER_CHOICES[0][0],
                    "last_updated_provider": pub_date,
                    "variant": variant[1],
                    "variant_name": variant[0],
                    "value": rate,
                }
            )
    return output, False