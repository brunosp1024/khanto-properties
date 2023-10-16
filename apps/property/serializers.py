from rest_framework import serializers

from apps.property.validators import *
from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'property_id', 'property_code', 'guest_limit',
            'bathroom_count', 'pets_allowed', 'cleaning_fee',
            'activation_date', 'created_at', 'updated_at'
        ]

    def validate(self, data):
        if not validate_property_code(data['property_code']):
            raise serializers.ValidationError(
                {'property_code': 'property_code deve ter 10 caracteres.'}
            )
        if not validate_cleaning_fee(data['cleaning_fee']):
            raise serializers.ValidationError(
                {'cleaning_fee': 'O valor deve ser maior ou igual a 0'}
            )
        return data