from django.db.models import OuterRef, Subquery

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rates.serializers import RateSerializer
from api.serializers import RatesSerializer
from api.throttling import APIThrottle

from rates.models import Rate, PROVIDER_CHOICES

class rates(APIView):
    '''Returns latest rates for all providers and all provider variants''' # Needs test 

    throttle_classes = [APIThrottle] # Needs test.
    def get(self, request):

        providers = []

        # I can't make this block work in a single DB query while matching the serializer output.
        for provider in PROVIDER_CHOICES:

            output = {}
            
            output["provider_id"] = provider[0]
            output["provider_verbose_name"] = provider[1]
            
            rates = Rate.objects.filter(provider=provider[0])\
                .order_by("variant", "-last_updated")\
                .distinct("variant")

            output["rates"] = rates
            
            providers.append(output)

        ser = RatesSerializer(providers, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
