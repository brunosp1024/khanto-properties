from rest_framework import serializers
from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            'reservation_id', 'advertisement', 'reservation_code',
            'check_in_date', 'check_out_date', 'total_price',
            'comment', 'num_guests', 'created_at', 'updated_at'
        ]