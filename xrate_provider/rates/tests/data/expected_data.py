from datetime import datetime
from django.utils.timezone import make_aware
from rates.services import BANXICO_TZ
from rates.dof import DOF_TZ

DEFAULT_FAILURE_OUTPUT = ([], True)

FIXER_VARIANT_1_VALID_OUTPUT = ([
    {
        'provider': 'FXR',
        'last_updated_provider' : make_aware(datetime.fromtimestamp(1642483143)),
        'value': 20.326596,
        'variant': 1
    }
], False)

BANXICO_VARIANT_1_VALID_OUTPUT = ([
    {
        'provider': 'BXO',
        'last_updated_provider': make_aware(datetime.strptime("17/01/2022", "%d/%m/%Y"), timezone=BANXICO_TZ, is_dst=None),
        'value': '20.3002',
        'variant': 1
    }
], False)


DOF_VARIANT_ALL_VALID_OUTPUT = ([
    {
        "provider": "DOF",
        "last_updated_provider": make_aware(datetime.strptime("14/01/2022", "%d/%m/%Y"), timezone=DOF_TZ, is_dst=None),
        "variant": 1,
        "variant_name": "FIX",
        "value": "20.3118",
    },
    {
        "provider": "DOF",
        "last_updated_provider": make_aware(datetime.strptime("17/01/2022", "%d/%m/%Y"), timezone=DOF_TZ, is_dst=None),
        "variant": 2,
        "variant_name": "Publicacion DOF",
        "value": "20.3118",
    },
    {
        "provider": "DOF",
        "last_updated_provider": make_aware(datetime.strptime("17/01/2022", "%d/%m/%Y"), timezone=DOF_TZ, is_dst=None),
        "variant": 3,
        "variant_name": "Para Pagos",
        "value": "20.3607",
    },
], False)
