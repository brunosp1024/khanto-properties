from django.contrib import admin
from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'reservation_id', 'advertisement', 'reservation_code',
        'check_in_date', 'check_out_date'
    )
    list_display_links = ('reservation_id', 'advertisement', 'reservation_code')
    search_fields = ('reservation_code',)
    raw_id_fields = ('advertisement',)
    list_per_page = 20


admin.site.register(Reservation, ReservationAdmin)
