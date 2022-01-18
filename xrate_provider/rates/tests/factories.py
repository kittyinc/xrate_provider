import factory
from rates.models import Rate
from django.utils import timezone
from functools import partial
from datetime import datetime

class RateFactory(factory.django.DjangoModelFactory):
    
    provider = "DOF"
    last_updated = datetime(2022, 1, 18, 5, 21, 58, 818654)
    last_updated_provider = datetime(2022, 1, 18, 5, 21, 58, 818654)

    value = 20.774400
    variant = 1

    class Meta:
        model = Rate
