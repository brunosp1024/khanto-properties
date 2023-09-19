from rest_framework import serializers
from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'property_id', 'property_code', 'guest_limit',
            'bathroom_count', 'pets_allowed', 'cleaning_fee',
            'activation_date', 'created_at', 'updated_at'
        ]