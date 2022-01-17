from django.contrib import admin
from authentication.models import XrateApiUser, APIToken


class XrateApiUserAdmin(admin.ModelAdmin):
    pass

class APITokenAdmin(admin.ModelAdmin):
    pass


admin.site.register(XrateApiUser, XrateApiUserAdmin)
admin.site.register(APIToken, APITokenAdmin)

