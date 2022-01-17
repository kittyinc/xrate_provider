from rest_framework.authentication import TokenAuthentication
from authentication.models import APIToken

class APITokenAuthentication(TokenAuthentication): # Needs test for unauthenticated, inactive, expired users
    model = APIToken