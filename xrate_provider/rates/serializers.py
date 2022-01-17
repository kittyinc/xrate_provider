from rest_framework import serializers
from rates.models import Rate

class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = [
            "last_updated",
            "last_updated_provider",
            "value",
            "variant",
        ]
