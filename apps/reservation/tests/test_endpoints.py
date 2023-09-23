import json
import pytest

from datetime import datetime
from model_bakery import baker
from rest_framework import status
from apps.reservation.models import Reservation


pytestmark = pytest.mark.django_db

class TestReservationEndpoints:

    endpoint = '/api/v1/reservations/'

    def test_list_all_reservations(self, client):        
        baker.make(Reservation, _quantity=3)
        response = client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)['results']) == 3

    @pytest.mark.parametrize("check_in, check_out, expected_status_code", [
        (datetime(2023, 9, 23, 8, 0), datetime(2023, 9, 25, 12, 0), 201),  # valid datetime
        (datetime(2023, 9, 26, 11, 30), datetime(2023, 9, 25, 7, 10), 400),  # invalid datetime
    ])
    def test_create_new_reservation(self, client, instance_reservation_dict, 
                                    check_in, check_out, expected_status_code):
        instance_reservation_dict['check_in_date'] = check_in
        instance_reservation_dict['check_out_date'] = check_out
        response = client.post(
            self.endpoint,
            data=instance_reservation_dict,
            format='json'
        )
        assert response.status_code == expected_status_code
    
    def test_create_reservation_conflict(self, client):
        # create the models and their relationship.
        property = baker.make('Property')
        advertisement = baker.make('Advertisement', property=property)
        check_in_date = datetime(2023, 10, 1)
        check_out_date = datetime(2023, 10, 5)
        baker.make(
            Reservation,
            advertisement=advertisement,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
        )

        # Simulate a request that would create a conflict with the existing reservation.
        conflicting_check_in_date = datetime(2023, 10, 3)
        conflicting_check_out_date = datetime(2023, 10, 7)
        data = {
            'advertisement': advertisement.advertisement_id,
            'check_in_date': conflicting_check_in_date.isoformat(),
            'check_out_date': conflicting_check_out_date.isoformat(),
        }
        response = client.post(self.endpoint, data, format='json')
        print(response)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {'message': 'There is already a reservation for this property.'}

    def test_retrieve_one_reservation(self, client):
        reservation = baker.make('reservation.Reservation')
        url = f'{self.endpoint}{reservation.reservation_id}/'
        response = client.get(url)
        assert response.status_code == 200
    
    def test_delete_reservation(self, client):
        reservation = baker.make('reservation.Reservation')
        url = f'{self.endpoint}{reservation.reservation_id}/'
        response = client.delete(url)
        assert response.status_code == 204
        assert Reservation.objects.all().count() == 0
