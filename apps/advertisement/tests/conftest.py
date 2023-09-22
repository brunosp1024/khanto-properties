import pytest
import base64

from rest_framework.test import APIClient
from model_bakery import baker


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
def instance_advertisement_dict():
    property = baker.make('Property')
    advertisement = baker.prepare('Advertisement')
    advertisement.property = property
    advertisement_dict = {
        'property': str(advertisement.property.property_id),
        'platform_name': advertisement.platform_name,
        'platform_fee': advertisement.platform_fee
    }
    return advertisement_dict


@pytest.fixture
def object_advertisement_dict():
    advertisement = baker.make('advertisement.Advertisement')
    advertisement_dict = {
        'advertisement_id': str(advertisement.advertisement_id),
        'property': str(advertisement.property.property_id),
        'platform_name': advertisement.platform_name,
        'platform_fee': advertisement.platform_fee
    }
    return advertisement_dict
