import json
import pytest

from model_bakery import baker
from apps.advertisement.models import Advertisement


pytestmark = pytest.mark.django_db

class TestAdvertisementEndpoints:

    endpoint = '/api/v1/advertisements/'

    def test_list_all_advertisements(self, client):        
        baker.make(Advertisement, _quantity=3)
        response = client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)['results']) == 3

    def test_create_new_advertisement(self, client, instance_advertisement_dict):
        response = client.post(
            self.endpoint,
            data=instance_advertisement_dict,
            format='json'
        )
        response_dict = json.loads(response.content.decode('utf-8'))
        assert response.status_code == 201
        assert all(
            item in response_dict.items() 
            for item in instance_advertisement_dict.items()
        ) == True

    def test_retrieve_one_advertisement(self, client, object_advertisement_dict):
        url = f'{self.endpoint}{object_advertisement_dict["advertisement_id"]}/'
        response = client.get(url)
        response_dict = json.loads(response.content.decode('utf-8'))
        assert response.status_code == 200
        assert all(
            item in response_dict.items() 
            for item in object_advertisement_dict.items()
        ) == True

    def test_update_advertisement(self, rf, client, instance_advertisement_dict):
        old_advertisement = baker.make(Advertisement)
        url = f'{self.endpoint}{old_advertisement.advertisement_id}/'
        response = client.put(
            url,
            instance_advertisement_dict,
            format='json'
        )
        response_dict = json.loads(response.content.decode('utf-8'))
        assert response.status_code == 200
        assert all(
            item in response_dict.items() 
            for item in instance_advertisement_dict.items()
            ) == True

    @pytest.mark.parametrize('field', [('property'), ('platform_name'), ('platform_fee')])
    def test_partial_update(self, field, client, instance_advertisement_dict):
        advertisement = baker.make(Advertisement)
        valid_field = instance_advertisement_dict[field]
        url = f'{self.endpoint}{advertisement.advertisement_id}/'
        response = client.patch(
            url,
            {field: valid_field},
            format='json'
        )
        assert response.status_code == 200
        assert json.loads(response.content)[field] == valid_field
