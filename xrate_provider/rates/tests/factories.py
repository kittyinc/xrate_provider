import factory
from rates.models import Rate
from django.utils import timezone


class RateFactory(factory.django.DjangoModelFactory):

    provider = "DOF"
    last_updated = factory.LazyFunction(timezone.now)
    last_updated_provider = factory.LazyFunction(timezone.now)

    value = 20.774400
    variant = 1

    class Meta:
        model = Rate
