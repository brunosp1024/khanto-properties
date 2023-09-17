from django.contrib import admin
from .models import Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('property_id', 'property_code', 'activation_date')
    list_display_links = ('property_id', 'property_code')
    search_fields = ('property_code',)
    list_per_page = 20


admin.site.register(Property, PropertyAdmin)
