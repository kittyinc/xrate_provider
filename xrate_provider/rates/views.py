from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from json import dumps # DELETE ME

class rates(APIView):

    def get(self, request):
        return Response("OK", status=status.HTTP_200_OK)




# MOCKED
class rates(APIView):

    def get(self, request):
        payload = {
            "rates": [
                {
                    "provider_name": "Diaro Oficial de la Federación",
                    "last_updated": "2022-01-14T19:59:60.511Z",
                    "value": 20.4722
                },
                {
                    "provider_name": "Fixer",
                    "last_updated": "2022-01-14T19:59:60.511Z",
                    "value": 20.4122
                },
                {
                    "provider_name": "Banxico",
                    "last_updated": "2022-01-14T19:59:60.511Z",
                    "value": 21.001
                },
            ]
        }
        return Response(dumps(payload), status=status.HTTP_200_OK)