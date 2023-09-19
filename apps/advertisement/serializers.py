from rest_framework import serializers
from .models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = [
            'advertisement_id', 'property', 'platform_name', 
            'platform_fee', 'created_at', 'updated_at'
        ]