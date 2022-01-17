from django.contrib import admin
from rates.models import Rate


class RateAdmin(admin.ModelAdmin):
    list_display = ('provider', 'value', 'variant', 'last_updated', 'last_updated_provider')    



admin.site.register(Rate, RateAdmin)