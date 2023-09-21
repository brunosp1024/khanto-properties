import json
import pytest

from model_bakery import baker
from apps.property.models import Property


class TestPropertyEndpoints:

    endpoint = '/api/v1/properties/'

    def test_list_all_properties(self, client):        
        baker.make(Property, _quantity=3)
        response = client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)['results']) == 3

    def test_create_new_property(self, client, instance_property_dict):
        response = client.post(
            self.endpoint,
            data=instance_property_dict,
            format='json'
        )
        response_dict = json.loads(response.content.decode('utf-8'))
        assert response.status_code == 201
        assert all(item in response_dict.items() for item in instance_property_dict.items()) == True

    def test_retrieve_one_property(self, client, object_property_dict):
        url = f'{self.endpoint}{object_property_dict["property_id"]}/'
        response = client.get(url)
        response_dict = json.loads(response.content.decode('utf-8'))
        assert response.status_code == 200
        assert all(item in response_dict.items() for item in object_property_dict.items()) == True

    def test_update_property(self, rf, client, instance_property_dict):
        old_property = baker.make(Property)
        url = f'{self.endpoint}{old_property.property_id}/'
        response = client.put(
            url,
            instance_property_dict,
            format='json'
        )
        response_dict = json.loads(response.content.decode('utf-8'))
        assert response.status_code == 200
        assert all(item in response_dict.items() for item in instance_property_dict.items()) == True

    @pytest.mark.parametrize('field', [
        ('property_code'), ('guest_limit'), ('bathroom_count'),
        ('pets_allowed'), ('cleaning_fee'), ('activation_date'),
    ])
    def test_partial_update(self, field, client, instance_property_dict):
        property = baker.make(Property)
        valid_field = instance_property_dict[field]
        url = f'{self.endpoint}{property.property_id}/'
        response = client.patch(
            url,
            {field: valid_field},
            format='json'
        )
        assert response.status_code == 200
        assert json.loads(response.content)[field] == valid_field

    def test_delete(self, client):
        property = baker.make(Property)
        url = f'{self.endpoint}{property.property_id}/'
        response = client.delete(url)
        assert response.status_code == 204
        assert Property.objects.all().count() == 0
