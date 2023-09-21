import pytest
import base64

from rest_framework.test import APIClient
from model_bakery import baker
from django.contrib.auth.models import User
from apps.property.models import Property


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(django_user_model):
    user = django_user_model.objects.create_user(username='stranger', password='secret')
    return user


@pytest.fixture
def client(user, api_client):
    credentials = base64.b64encode('stranger:secret'.encode('utf-8')).decode('utf-8')
    api_client.credentials(HTTP_AUTHORIZATION='Basic ' + credentials)
    return api_client


@pytest.fixture
def instance_property_dict():
    property = baker.prepare(Property)
    property_dict = {
        'property_code': property.property_code,
        'guest_limit': property.guest_limit,
        'bathroom_count': property.bathroom_count,
        'pets_allowed': property.pets_allowed,
        'cleaning_fee': property.cleaning_fee,
        'activation_date': str(property.activation_date)
    }
    return property_dict


@pytest.fixture
def object_property_dict():
    property = baker.make(Property)
    property_dict = {
        'property_id': str(property.property_id),
        'property_code': property.property_code,
        'guest_limit': property.guest_limit,
        'bathroom_count': property.bathroom_count,
        'pets_allowed': property.pets_allowed,
        'cleaning_fee': property.cleaning_fee,
        'activation_date': str(property.activation_date)
    }
    return property_dict
