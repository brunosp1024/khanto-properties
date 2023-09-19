from django.contrib import admin
from .models import Advertisement


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('advertisement_id', 'property', 'platform_name', 'platform_fee')
    list_display_links = ('advertisement_id', 'property', 'platform_name')
    search_fields = ('property__property_code','platform_name')
    raw_id_fields = ('property',)
    list_per_page = 20


admin.site.register(Advertisement, AdvertisementAdmin)
