from dateutil import parser

from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Reservation
from .serializers import ReservationSerializer


class ReservationViewSet(ModelViewSet):
    """ Implements actions to reservations: list, create, retrieve e delete """

    serializer_class = ReservationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    http_method_names = ['get', 'post', 'delete']

    def create(self, request):
        try:
            check_in = parser.parse(request.data['check_in_date'])
            check_out = parser.parse(request.data['check_out_date'])
            if check_in > check_out:
                return Response(
                    {'message': 'Check-in cannot be later than check-out'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as ex:
            return Response(
                    {'message': f'Failed to create reservation. Error: {ex}'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        return super().create(request)
