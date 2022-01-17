from rest_framework import serializers
from rates.serializers import RateSerializer
from rates.models import PROVIDER_CHOICES

class RatesSerializer(serializers.Serializer):
    provider_id  = serializers.CharField(
        max_length=3,
    )
    provider_verbose_name = serializers.CharField(
        max_length="100"
    )

    rates = RateSerializer(many=True)