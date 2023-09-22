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
def instance_reservation_dict():
    advertisement = baker.make('Advertisement')
    reservation = baker.prepare('Reservation')
    reservation.advertisement = advertisement
    reservation_dict = {
        'advertisement': str(reservation.advertisement.advertisement_id),
        'check_in_date': reservation.check_in_date,
        'check_out_date': reservation.check_out_date,
        'total_price': reservation.total_price,
        'comment': reservation.comment,
        'num_guests': reservation.num_guests
    }
    return reservation_dict
