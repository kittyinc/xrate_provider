from rest_framework.throttling import UserRateThrottle


class APIThrottle(UserRateThrottle):
    scope = 'default'
