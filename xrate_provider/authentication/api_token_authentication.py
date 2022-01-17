from rest_framework.authentication import TokenAuthentication
from authentication.models import APIToken

class APITokenAuthentication(TokenAuthentication):
    model = APIToken